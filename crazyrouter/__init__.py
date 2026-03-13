"""
Crazyrouter Python SDK — One API key for 300+ AI models.

Drop-in replacement for the OpenAI Python SDK.
Access GPT-5, Claude Opus 4, Gemini 3, DeepSeek V3 and more.

Usage:
    from crazyrouter import Crazyrouter

    client = Crazyrouter(api_key="sk-xxx")

    response = client.chat.completions.create(
        model="gpt-5.4",
        messages=[{"role": "user", "content": "Hello!"}]
    )

Website: https://crazyrouter.com
Pricing: https://crazyrouter.com/pricing
Models: https://crazyrouter.com/models
"""

from openai import OpenAI

__version__ = "1.0.0"
__all__ = ["Crazyrouter", "chat", "list_models"]

DEFAULT_BASE_URL = "https://crazyrouter.com/v1"


class Crazyrouter(OpenAI):
    """
    Crazyrouter client — drop-in replacement for OpenAI Python SDK.

    One API key for 300+ AI models: GPT-5, Claude Opus 4, Gemini 3,
    DeepSeek V3, and more. Up to 50% cheaper than going direct.

    Args:
        api_key: Your Crazyrouter API key (get one at https://crazyrouter.com)
        base_url: API base URL (default: https://crazyrouter.com/v1)
        **kwargs: Additional arguments passed to OpenAI client

    Example:
        >>> from crazyrouter import Crazyrouter
        >>> client = Crazyrouter(api_key="sk-xxx")
        >>> response = client.chat.completions.create(
        ...     model="claude-opus-4-6",
        ...     messages=[{"role": "user", "content": "Hello!"}]
        ... )
    """

    def __init__(self, api_key: str, base_url: str = DEFAULT_BASE_URL, **kwargs):
        super().__init__(api_key=api_key, base_url=base_url, **kwargs)


def chat(api_key: str, model: str, message: str) -> str:
    """Quick one-liner chat helper.

    Args:
        api_key: Crazyrouter API key
        model: Model name (e.g., "gpt-5.4", "claude-opus-4-6")
        message: User message

    Returns:
        Assistant's response text
    """
    client = Crazyrouter(api_key=api_key)
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": message}],
    )
    return response.choices[0].message.content or ""


def list_models(api_key: str) -> list:
    """List all available models.

    Args:
        api_key: Crazyrouter API key

    Returns:
        Sorted list of model IDs
    """
    client = Crazyrouter(api_key=api_key)
    models = client.models.list()
    return sorted([m.id for m in models])
