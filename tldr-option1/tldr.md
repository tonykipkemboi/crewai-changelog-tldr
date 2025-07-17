:police_car_light:CrewAI 0.148.0 is out! :police_car_light:

Here’s what you need to know about this release, with direct links and actionable recommendations for the community.

---

## Core Improvements & Fixes

- **Agent Knowledge Handling Improvements:**  
  Addresses persistent bugs where agents “forget” or mishandle stored knowledge. Targeted fixes were shipped ([#3169](https://github.com/crewAIInc/crewAI/issues/3169)), but not all causes are yet resolved—watch for updates.

- **Thread-Safe Agent Evaluation:**  
  The new `AgentEvaluator` is now thread-safe, supporting more robust concurrent or multi-agent scenarios.

- **Bug Fixes for LLM and Task Parameters:**  
  Core bug around LLM–agent integration fixed; issues with Task parameters and agent base classes received attention.

- **neatlogs Integration:**  
  Core logging is now compatible with `neatlogs`, improving traceability and observability in your CrewAI projects.

- **Ongoing Security Review:**  
  While 0.148.0 advances stability, security blockers like the `embedchain` dependency are still open ([#334](https://github.com/crewAIInc/crewAI-tools/issues/334)). This remains an enterprise barrier.

See changelog: [CrewAI 0.148.0 Release](https://github.com/joaomdmoura/crewAI/releases/tag/0.148.0)

---

## New Features & Enhancements

- **Agent Evaluation Functions:**  
  Official evaluation tools introduced to measure agent performance and outputs. Responds to growing demand for better benchmarking.

- **Workflow Guardrail Events:**  
  Expanded guardrail attributes and event types support more nuanced control and oversight of agent actions—aligning with both developer and compliance needs.

- **Enhanced Context Tracking:**  
  Agent and LLM context flows now better captured, boosting transparency and reliability in complex, multi-step tasks.

- **Structured Output Progress:**  
  While structured agent response support for all LLMs is not fully cross-compatible, groundwork enhancements lay a path for upcoming releases ([#3174](https://github.com/crewAIInc/crewAI/issues/3174)).

- **Improved Session Management:**  
  Reliability added for concurrent use cases, particularly where agent tasks and tools execute in overlapping environments.

---

## Documentation & Guides

- **New Guides on Guardrail Attributes & Events:**  
  Detailed docs with practical code samples—start using the new workflow controls right away:  
  [Guardrail Attributes Doc](https://docs.crewai.com/guardrails/)

- **neatlogs Integration Walkthrough:**  
  Step-by-step integration notes show how to plug CrewAI output into neatlogs for enhanced auditability:  
  [neatlogs in CrewAI](https://docs.crewai.com/logging/neatlogs/)

- **Agent Repository & Kickoff Methods:**  
  Updated pages clarify new agent repo logic and invocation methods, aiming to unblock onboarding for large teams:  
  [Agent Repository Doc](https://docs.crewai.com/agents/repo/)

- **Expanded Usage Examples:**  
  Community-requested code snippets for guardrail configuration and monitoring; easier for newcomers and scaling teams.

---

Full release notes here – [https://github.com/crewAIInc/crewAI/releases](https://github.com/crewAIInc/crewAI/releases)

---

## Community Insights

- **Ongoing High-Priority Issues:**  
  - LLM integration (especially local Ollama support on Windows) is still problematic ([#3176](https://github.com/crewAIInc/crewAI/issues/3176)).
  - Security/compliance blockers (such as unresolved embedchain vulnerabilities) prevent some enterprise deployments.
  - Tool usability (e.g., DirectoryReadTool over-listing; SeleniumScrapingTool sessions) is a recurring pain.
  - Structured output and advanced param support (like “extra_headers”) are widely requested; implementation is ongoing.

- **Positive Trends:**  
  - Documentation now closely follows feature updates; “docs-first” approach is winning praise.
  - Introduction of agent evaluation is highly anticipated—encouraging project-level quality management.
  - Community workaround sharing is active; suggestions to formalise these into the codebase are recommended.

## Calls to Action

- If you hit open bugs (memory, integrations, security), please file reproducible reports with your system info.
- Share detailed feedback and use case examples on the most-wanted enhancements (e.g., output formatting, LLM compatibility).
- Contribute docs or suggest PRs for common workarounds—check the “help wanted” GitHub tags.
- For enterprise or regulated use, verify impact of unresolved security advisories before upgrading.
- Stay involved via [forum](https://github.com/crewAIInc/crewAI/discussions) and [GitHub Issues](https://github.com/crewAIInc/crewAI/issues).

---

Thank you for driving CrewAI’s progress—your feedback and community collaboration power each release. Let’s keep building together!

---

*Release data as of 2025-07-17. Reach out on the forum or next community call for deeper questions or to help shape the roadmap.*