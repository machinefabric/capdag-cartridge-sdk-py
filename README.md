# MachineFabric cartridge SDK for Python

This public Python package mirrors the Rust `machfab-cartridge-sdk`. It is for
Python cartridge authors who need the canonical request, stream, vocabulary and
model-information records, the media and cap URNs that carry them, the
prompt-strategy decision, and the shared page-selection grammar.

## Install

```bash
pip install machfab-cartridge-sdk
```

The cartridge runtime itself — the bifaci host loop, cap registration, the
manifest, peer calls — is [capdag](https://pypi.org/project/capdag/)'s. A
cartridge installs both and imports each for what it owns; this package
declares no dependency on capdag, so a release of one never waits on the other.

## Layout

| Module | Contract |
| --- | --- |
| `machfab_cartridge_sdk.llm` | LLM request, stream, vocabulary and model-information records, media URNs, cap URNs, and `backend_for_model_spec` classification. |
| `machfab_cartridge_sdk.prompt` | Prompt-strategy classification and the shared default system prompt. |
| `machfab_cartridge_sdk.pages` | One-based page/index selection with ordered, deduplicated, clamped ranges. |

The reference also ships `net_retry` (a retry policy written directly on
reqwest's types) and `structured_queries` (a Tera-rendered query registry).
Neither is in this mirror, and neither is stubbed: a function that exists and
does nothing is worse than one that is absent, because it is discovered at
runtime rather than at import.

## Usage

```python
from machfab_cartridge_sdk.llm import (
    BACKEND_GGUF,
    CAP_LLM_INFERENCE_GGUF,
    LlmGenerationRequest,
    backend_for_model_spec,
)

request = LlmGenerationRequest.with_defaults(
    "Summarize this document",
    "hf:Qwen/Qwen2.5-0.5B-Instruct",
)
print(request.to_json())

if backend_for_model_spec(request.model_spec) == BACKEND_GGUF:
    ...  # dispatch to CAP_LLM_INFERENCE_GGUF
```

Preparing a prompt for whichever model was downloaded:

```python
from machfab_cartridge_sdk.prompt import (
    DEFAULT_SYSTEM_PROMPT,
    ChatTemplated,
    RefinedDims,
    classify_prompt,
)

strategy = classify_prompt(
    RefinedDims(chat_template=dims["chat_template"]),
    user_text,
    DEFAULT_SYSTEM_PROMPT,
)
if isinstance(strategy, ChatTemplated):
    ...  # render through the model's own chat template, specials parsed
else:
    ...  # tokenize strategy.text verbatim
```

## Verify changes

```bash
PYTHONPATH=src python -m pytest tests/ -q
```

The Rust SDK is authoritative for MachineFabric-specific wire types, and the
numbered tests here are the reference's numbers: `test0001`–`test0010` are its
`llm` tests, `test0011`–`test0016` its `prompt` tests, and `test0060`–`test0062`
its `pages` tests. A change to a shared wire type or a prompt decision is
mirrored here — implementation and same-numbered tests — in the same change.
Language-neutral runtime behavior belongs to the
[CapDAG specification](../capdag/docs/01-overview.md).
