New Release: CrewAI v0.157.0 is out! 🚨

## Core Improvements & Fixes

- New `crewai config` CLI command group for centralised, structured configuration management. See [CLI config docs](https://docs.crewai.com/cli/config).
- Initial tracing support added, enabling early agent activity monitoring and groundwork for future step-tracking (see [crewAI#3268](https://github.com/crewAIInc/crewAI/issues/3268) and [tracing docs](https://docs.crewai.com/cli/tracing)).
- Okta device-based authorisation for improved enterprise security ([enterprise auth docs update](https://docs.crewai.com/auth/okta)).
- Improved CLI error reporting for clearer debugging and faster troubleshooting.
- String operations optimised for performance.
- Upgraded LiteLLM dependency for better LLM (large language model) integration.
- [User Memory](https://docs.crewai.com/migration/user-memory) system deprecated (now removed) – you must migrate existing workflows.

Unresolved and high-priority issues (as of 2025-08-08):
- Windows platform support: CrewAI still does not run natively on Windows. See [issue #3253](https://github.com/crewAIInc/crewAI/issues/3253).
- Agent kickoff failures with custom prompts and Weave integration ([#3261](https://github.com/crewAIInc/crewAI/issues/3261), [tools#394](https://github.com/crewAIInc/crewAI-tools/issues/394)).
- Tool integration bugs persist (notably with embedchain, Weave, and Selenium).
- Ongoing VertexAI BadRequestErrors ([#3277](https://github.com/crewAIInc/crewAI/issues/3277)).
- Issues disabling reasoning mode ([#3242](https://github.com/crewAIInc/crewAI/issues/3242)).
- Documentation clarity: Outdated/broken links and missing guides remain a pain-point ([#3240](https://github.com/crewAIInc/crewAI/issues/3240)).

## New Features & Enhancements

- Support for LangDB, opening new data workflow integrations ([LangDB docs](https://docs.crewai.com/integrations/langdb)).
- CLI: Tracing (initial, alpha-stage), laying the foundation for live agent step transparency and audit trails.
- Okta device authorisation option for enterprise users to streamline and secure authentication.
- CLI enhancements: More user feedback, structured error output for easier troubleshooting.

Community feedback on new features is positive—especially on configuration, tracing, and LangDB. However, reliability (especially platform support and error resilience) and observability (live, explainable agent actions) are top asks for the next cycle.

## Documentation & Guides

- CLI config, tracing, and LangDB guides published and being expanded. [Start here](https://docs.crewai.com/cli/config)
- Okta/enterprise authentication expanded ([auth docs](https://docs.crewai.com/auth/okta)).
- User Memory migration guide now available—essential if you relied on the previous memory feature ([migration guide](https://docs.crewai.com/migration/user-memory)).
- Documentation on agent transparency, troubleshooting, and stepwise execution in progress.
- Known issues: Documentation lags new features, sample code/tests and plugin integration examples need improvement. See and help with the latest at [crewAI#3240](https://github.com/crewAIInc/crewAI/issues/3240).

Full release notes here – [CrewAI v0.157.0 on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.157.0)

---

**Community Priorities & Insights**

- High demand for explainability and agent action transparency (step-by-step tracing, live HITL—human-in-the-loop—streaming).
- Users and teams are eager for improved Windows support and smoother agent startup (kickoff).
- Positive engagement: More contributors are raising issues and PRs, especially focused on documentation and usability.
- Docs, clarity, and working examples remain the most frequent requests after every feature release.
- To influence priority, upvote or comment on the [high-impact issues](https://github.com/crewAIInc/crewAI/issues).

---

**Action points:**
- If you relied on User Memory, migrate immediately to stay compatible.
- Test and comment on new CLI config and tracing features—your feedback shapes the next release.
- Report platform/agent-launch issues with full logs for triage.
- Help improve docs by submitting corrections or reporting missing/broken links.

Thank you for building and shaping CrewAI with us. For support, join [the forum](https://community.crewai.com/), and for detailed guidance, see [docs.crewai.com](https://docs.crewai.com).

❤️ The CrewAI team appreciates your feedback—let's keep improving for everyone!

---

Legend:  
🟠 = Still open or recurring  
✅ = Resolved  
Release as of 2025-08-08. Feedback or clarification? Raise it in the next sync or open an issue.

---