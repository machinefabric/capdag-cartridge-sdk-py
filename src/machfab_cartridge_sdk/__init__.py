"""MachFab Cartridge SDK for Python.

Shared data contracts for MachineFabric cartridges written in Python. The Rust
``machfab-cartridge-sdk`` is the reference; this mirror carries the same wire
types, the same defaults and the same decisions, because a cap answered by a
Python cartridge must be indistinguishable on the wire from the same cap
answered by a Rust one.

Modules:

- :mod:`machfab_cartridge_sdk.llm` — the LLM request, stream, vocabulary and
  model-information records, their media URNs, the cap URNs that carry them,
  and model-spec → backend classification.
- :mod:`machfab_cartridge_sdk.prompt` — prompt-strategy classification and the
  shared default system prompt.
- :mod:`machfab_cartridge_sdk.pages` — the 1-based page/index selection
  grammar, ordered, deduplicated and clamped.

# What this mirror does NOT carry

The reference also ships ``net_retry`` (a retry policy expressed directly on
reqwest's types) and ``structured_queries`` (a Tera-rendered query registry).
Neither is here, and neither is stubbed: a function that exists and does
nothing is worse than one that is absent, because a cartridge author writes
against it and finds out at runtime.

The cartridge RUNTIME — the bifaci host loop, cap registration, the manifest,
peer calls — is capdag's, not this package's. A Python cartridge imports
``capdag`` for those directly; this package deliberately does not re-export
them, so its release never has to wait on capdag's.
"""

from . import llm, pages, prompt

__all__ = ["llm", "pages", "prompt"]
