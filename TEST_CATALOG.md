# Test catalogue — capdag-cartridge-sdk-py

Generated from the test catalogue. Edit the tests, not this file.

19 tests: 19 numbered, 0 unnumbered.

## Numbered

| Number | Repository | Language | Test | Location | Description |
|---|---|---|---|---|---|
| TEST1 | capdag-cartridge-sdk-py | python | `test_0001_generation_request_round_trip` | tests/test_llm.py:27 | TEST0001: a generation request round-trips to equivalent content. |
| TEST2 | capdag-cartridge-sdk-py | python | `test_0002_stream_message_token_round_trip` | tests/test_llm.py:38 | TEST0002: a token message round-trips to itself, byte for byte. |
| TEST3 | capdag-cartridge-sdk-py | python | `test_0003_stream_message_complete_round_trip` | tests/test_llm.py:49 | TEST0003: Stream message complete round trip. |
| TEST4 | capdag-cartridge-sdk-py | python | `test_0004_stream_message_error_round_trip` | tests/test_llm.py:59 | TEST0004: Stream message error round trip. |
| TEST5 | capdag-cartridge-sdk-py | python | `test_0005_vocab_response_round_trip` | tests/test_llm.py:69 | TEST0005: Vocab response round trip. |
| TEST6 | capdag-cartridge-sdk-py | python | `test_0006_model_info_round_trip` | tests/test_llm.py:77 | TEST0006: Model info round trip. |
| TEST7 | capdag-cartridge-sdk-py | python | `test_0007_constraint_spec_tags` | tests/test_llm.py:90 | TEST0007: Constraint spec tags. |
| TEST8 | capdag-cartridge-sdk-py | python | `test_0008_backend_for_model_spec_gguf` | tests/test_llm.py:115 | TEST0008: Backend for model spec gguf. |
| TEST9 | capdag-cartridge-sdk-py | python | `test_0009_backend_for_model_spec_mlx` | tests/test_llm.py:125 | TEST0009: Backend for model spec mlx. |
| TEST10 | capdag-cartridge-sdk-py | python | `test_0010_backend_for_model_spec_candle` | tests/test_llm.py:138 | TEST0010: Backend for model spec candle. |
| TEST11 | capdag-cartridge-sdk-py | python | `test_0011_jinja_template_yields_chat_templated` | tests/test_prompt.py:21 |  |
| TEST12 | capdag-cartridge-sdk-py | python | `test_0012_short_name_template_yields_chat_templated` | tests/test_prompt.py:35 |  |
| TEST13 | capdag-cartridge-sdk-py | python | `test_0013_absent_template_yields_raw` | tests/test_prompt.py:46 |  |
| TEST14 | capdag-cartridge-sdk-py | python | `test_0014_whitespace_only_system_prompt_dropped_for_chat_templated` | tests/test_prompt.py:61 |  |
| TEST15 | capdag-cartridge-sdk-py | python | `test_0015_unknown_chat_template_value_yields_raw` | tests/test_prompt.py:74 |  |
| TEST16 | capdag-cartridge-sdk-py | python | `test_0016_default_system_prompt_is_task_agnostic` | tests/test_prompt.py:87 |  |
| TEST60 | capdag-cartridge-sdk-py | python | `test_0060_index_range_grammar` | tests/test_pages.py:13 |  |
| TEST61 | capdag-cartridge-sdk-py | python | `test_0061_index_range_clamps_past_end` | tests/test_pages.py:26 |  |
| TEST62 | capdag-cartridge-sdk-py | python | `test_0062_index_range_hard_errors` | tests/test_pages.py:35 | A single page past the end is a start-past-end error, not a clamp (see TEST0062) — clamping only widens a range that STARTS in bounds. |

