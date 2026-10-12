# Crazyrouter Python SDK

An OpenAI SDK wrapper that defaults to `https://crazyrouter.com/v1`.

[![PyPI version](https://badge.fury.io/py/crazyrouter.svg)](https://pypi.org/project/crazyrouter/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Installation

```bash
pip install crazyrouter
```

## Quick Start

```python
from crazyrouter import Crazyrouter

client = Crazyrouter(api_key="sk-xxx")

# GPT-5.4
response = client.chat.completions.create(
    model="gpt-5.4",
    messages=[{"role": "user", "content": "Explain quantum computing"}]
)

# Claude Opus 4.6 — Chat Completions-compatible text example
response = client.chat.completions.create(
    model="claude-opus-4-6",
    messages=[{"role": "user", "content": "Explain quantum computing"}]
)
```

## Migration from OpenAI SDK

```diff
- from openai import OpenAI
+ from crazyrouter import Crazyrouter

- client = OpenAI(api_key="sk-openai-xxx")
+ client = Crazyrouter(api_key="sk-crazyrouter-xxx")

# Verify the model ID, endpoint and supported parameters before migrating.
```

## Links

- 🌐 [Website](https://crazyrouter.com)
- 💰 [Pricing](https://crazyrouter.com/pricing)
- 🤖 [Models](https://crazyrouter.com/models)
- 💬 [Telegram](https://t.me/crzrouter)

## License

MIT © [Crazyrouter](https://crazyrouter.com)

## Version and billing scope

The wrapper uses the OpenAI SDK version range declared in the package manifest. It does not promise that all features of newer SDK versions are available. Check [current prices](https://crazyrouter.com/en/pricing); there is no universal discount.
