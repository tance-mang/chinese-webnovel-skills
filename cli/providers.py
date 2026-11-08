"""Explicit model selection. SDK exceptions never reach logs or the UI verbatim."""
import math
import os
from urllib.parse import urlsplit


class ProviderError(RuntimeError):
    pass


def error_message(exc):
    if isinstance(exc, ProviderError):
        return str(exc)
    status = getattr(exc, 'status_code', None)
    code = getattr(exc, 'code', None)
    if code in ('insufficient_quota', 'billing_hard_limit_reached') or status == 402:
        return '额度或付费状态不足，请检查服务账号。'
    if code in ('content_policy_violation', 'content_filter'):
        return '服务拒绝生成该内容，请调整请求。'
    if status == 401:
        return '认证失败，请检查 API Key。'
    if status in (403, 404):
        return '无权访问或找不到模型／接口，请检查配置。'
    if status == 429:
        return '服务限流，请稍后手动重试。'
    if 'Timeout' in type(exc).__name__ or isinstance(exc, TimeoutError):
        return '请求超时，请检查网络或调整 timeout。'
    if 'Connection' in type(exc).__name__ or isinstance(exc, OSError):
        return '无法连接服务，请检查地址和网络。'
    return f'请求失败（HTTP {status}）。' if isinstance(status, int) else '请求失败，请检查服务配置。'


class ProviderRouter:
    def __init__(self, cfg, client_factory):
        self.legacy = {**cfg, 'api_mode': 'chat'}
        self.client_factory = client_factory
        self.profiles = cfg.get('providers', {})
        if not isinstance(self.profiles, dict) or 'legacy' in self.profiles:
            raise ProviderError('providers 必须是对象，legacy 为保留名称。')
        self.active = cfg.get('provider') or 'legacy'
        self.usage = None
        self.estimated_cost = None
        self.spec(self.active)

    def spec(self, name):
        if name == 'legacy':
            return self.legacy
        profile = self.profiles.get(name)
        if not isinstance(profile, dict):
            raise ProviderError('找不到该模型配置。')
        kind = profile.get('kind', 'compatible')
        defaults = {'compatible': (None, 'chat'), 'xai': ('https://api.x.ai/v1', 'responses'),
                    'ollama': ('http://localhost:11434/v1', 'chat')}
        if not isinstance(kind, str) or kind not in defaults:
            raise ProviderError('未知服务类型。')
        url, mode = defaults[kind]
        url = profile.get('base_url') or url
        mode = profile.get('api_mode', mode)
        env = profile.get('api_key_env') or ('XAI_API_KEY' if kind == 'xai' else None)
        model = profile.get('model')
        if not isinstance(model, str) or not model.strip() or mode not in ('chat', 'responses') or not isinstance(url, str):
            raise ProviderError('模型配置需要有效的 model、base_url 和 api_mode。')
        try:
            parsed = urlsplit(url)
        except ValueError:
            raise ProviderError('base_url 格式错误。') from None
        if parsed.scheme not in ('http', 'https') or not parsed.hostname or parsed.username or parsed.password or parsed.query or parsed.fragment:
            raise ProviderError('base_url 必须是无凭据、无查询参数的 HTTP(S) 地址。')
        local = parsed.hostname in ('localhost', '127.0.0.1', '::1')
        if env is not None and not isinstance(env, str):
            raise ProviderError('api_key_env 必须是环境变量名称。')
        key = os.environ.get(env, '') if env else ''
        if not key and kind == 'ollama' and local:
            key = 'ollama'
        return {**profile, 'base_url': url, 'model': model, 'api_mode': mode, 'api_key': key}

    def client(self, spec):
        if not spec.get('api_key'):
            raise ProviderError('未配置 API Key，请设置服务对应的环境变量。')
        timeout = spec.get('timeout', 90)
        if not isinstance(timeout, (int, float)) or not 0 < timeout <= 600:
            raise ProviderError('timeout 需在 0 到 600 秒之间。')
        return self.client_factory(base_url=spec['base_url'], api_key=spec['api_key'],
                                   timeout=timeout, max_retries=0)

    def health(self, name):
        spec = self.spec(name)
        models = self.client(spec).models.list()
        return any(model.id == spec['model'] for model in models)

    def stream(self, model, messages, profile=None):
        self.usage = None
        self.estimated_cost = None
        spec = self.spec(profile or self.active)
        client = self.client(spec)
        model = model or spec['model']
        usage = None
        if spec['api_mode'] == 'responses':
            stream = client.responses.create(model=model, input=messages, stream=True, store=False)
            with stream as events:
                complete = False
                for event in events:
                    if event.type == 'response.output_text.delta':
                        yield event.delta
                    elif event.type == 'response.refusal.delta':
                        raise ProviderError('服务拒绝生成该内容，请调整请求。')
                    elif event.type in ('response.failed', 'response.incomplete', 'error'):
                        raise ProviderError('服务未完成本轮生成。')
                    elif event.type == 'response.completed':
                        complete = True
                        usage = getattr(event.response, 'usage', None)
                if not complete:
                    raise ProviderError('流式连接提前结束，未保存本轮回复。')
        else:
            options = {'stream_options': {'include_usage': True}} if spec.get('report_usage') else {}
            stream = client.chat.completions.create(model=model, messages=messages, stream=True,
                                                    temperature=0.8, **options)
            with stream as chunks:
                for chunk in chunks:
                    usage = getattr(chunk, 'usage', None) or usage
                    if not chunk.choices:
                        continue
                    choice = chunk.choices[0]
                    delta = choice.delta
                    if getattr(choice, 'finish_reason', None) == 'content_filter' or getattr(delta, 'refusal', None):
                        raise ProviderError('服务拒绝生成该内容，请调整请求。')
                    if delta and delta.content:
                        yield delta.content
        if usage is not None:
            self.usage = (getattr(usage, 'input_tokens', getattr(usage, 'prompt_tokens', None)),
                          getattr(usage, 'output_tokens', getattr(usage, 'completion_tokens', None)))
            rates = (spec.get('usd_input_per_million'), spec.get('usd_output_per_million'))
            if model == spec['model'] and all(isinstance(n, (int, float)) and math.isfinite(n) and n >= 0
                                               for n in (*self.usage, *rates)):
                self.estimated_cost = sum(n * rate for n, rate in zip(self.usage, rates)) / 1_000_000
