New Release:CrewAI v0.159.0 is out! :police_car_light:

## Core Improvements & Fixes
- New streaming pipeline with backpressure; smoother throughput and reduced memory spikes.
- Cancellation support added; hotfix resolves orphan tasks reported by community.
- Unified memory provider abstraction overhauled for reliability and lifecycle clarity.
- OpenAI-compatible SSE streaming multiplexing; improves interoperability across SDKs.
- [BREAKING] Memory config keys renamed; migrate to memory.provider and memory.params.
- [BREAKING] on_error signature updated; adjust custom handlers or wrappers accordingly.
- [BREAKING] execute_tool behaviour adjusted; review custom tool adapters during migration.

## New Features & Enhancements
- tool_strategy introduced; clear agent defaults with simple per-task overrides.
- Deprecates tool_choice alias; warnings guide migration without immediate breakage.
- Streaming controls tuned for stability; better backpressure and cancellation coordination.

## Documentation & Guides
- Migration to 0.159: rename memory keys; adopt tool_strategy for tools. [https://docs.crewai.com/migration/0.159]
- Tool Strategy guide: agent defaults and per-task overrides with examples. [https://docs.crewai.com/agents/tool-strategy]
- Memory Providers guide covers pluggable providers and safe shutdown patterns. [https://docs.crewai.com/memory/providers]

Full release notes here - [[https://github.com/crewAIInc/crewAI/releases]