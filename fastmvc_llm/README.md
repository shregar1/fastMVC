# fastmvc_llm

LLM provider abstraction for FastMVC: OpenAI, Anthropic, Ollama. Built on `fastmvc_core` services.

Config: `config/llm/config.json` via `fastmvc_core.LLMConfiguration`.

Optional: `pip install fastmvc_llm[openai]`, `[anthropic]`, `[ollama]`.

```python
from fastmvc_llm import build_llm_service

llm = build_llm_service()
if llm:
    reply = await llm.generate("Hello", max_tokens=100)
```
