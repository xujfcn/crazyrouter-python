# Crazyrouter Python SDK

**One API key for 300+ AI models.** Drop-in replacement for the OpenAI Python SDK.

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

# Claude Opus 4.6 — same API, just change the model name
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

# Everything else stays the same!
```

## Links

- 🌐 [Website](https://crazyrouter.com)
- 💰 [Pricing](https://crazyrouter.com/pricing)
- 🤖 [Models](https://crazyrouter.com/models)
- 💬 [Telegram](https://t.me/crzrouter)

## License

MIT © [Crazyrouter](https://crazyrouter.com)
