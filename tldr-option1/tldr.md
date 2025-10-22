New Release: CrewAI 1.1.0 is out! 🚨

CrewAI version 1.1.0 (released 2025-10-21) delivers key enhancements for language model integration, developer experience, and vector search capabilities. However, please note several unresolved high-severity bugs and known issues that may affect critical workflows. Here’s what you need to know:

## Core Improvements & Fixes

- **Multi-provider Large Language Model (LLM) support**  
  Now supports multiple LLM backends in `InternalInstructor` and related classes, letting you choose the best model for your needs.  
- **mypy plugin base and stricter typing**  
  Improved static type checking makes code safer and easier to maintain, while surfacing parameter mismatches earlier.  
- **Template pinning**  
  Prevents unintentional changes to task/agent templates by enabling version locking.
- **Internal logging and tracing fixes**  
  Fixes to logging/tracing make debugging more reliable; improves error tracking in complex workflows.  
  - [Ongoing exception handling requests](https://github.com/crewAIInc/crewAI/issues/3755)
- **Dependency fixes**  
  - Integration documentation link corrections.
  - Addresses select import errors, but [litellm dependency](https://github.com/crewAIInc/crewAI/issues/3750) and [PGSearch import](https://github.com/crewAIInc/crewAI/issues/3776) remain open concerns.

**More core fixes and context:**  
- [CrewAI Issues Tracker](https://github.com/crewAIInc/crewAI/issues)

---

## New Features & Enhancements

- **Qdrant Vector Search Tool upgrades**  
  Significant improvements to vector search and retrieval. However, be aware of reported [Qdrant regressions](https://github.com/crewAIInc/crewAI-tools/issues/478) (test before upgrading).
- **Initial plugin framework**  
  The new mypy-compatible base sets the stage for community-built plugins.  
  - Typed tracing and safer validation for workflows and agent/job tasks.
- **Enhanced error surfacing (in progress)**  
  Work to improve error message clarity and exception handling is ongoing, following [community requests](https://github.com/crewAIInc/crewAI/issues/3755).
- **Better LLM integration options**  
  Seamless switching between providers; updated guides for Azure, Bedrock, and OpenAI compatibility.

**Still outstanding:**  
High-priority issues remain open for tool failures ([StageHand](https://github.com/crewAIInc/crewAI-tools/issues/412), TXTSearch), async deadlocks ([#3730](https://github.com/crewAIInc/crewAI/issues/3730)), memory management ([#3753](https://github.com/crewAIInc/crewAI/issues/3753)), and context window errors ([#3774](https://github.com/crewAIInc/crewAI/issues/3774)).  
- [Full list of open issues](https://github.com/crewAIInc/crewAI/issues)

---

## Documentation & Guides

- **LLM integration documentation updated**  
  Step-by-step guidance for using multiple LLMs, with tips for dependency management and version safety.  
  [Docs: LLM Integration](https://docs.crewai.com/integrations/)
- **Upgrade notes and examples**  
  Expanded guides and real-world walkthroughs for upgrading your CrewAI environment to 1.1.0, addressing breaking changes and workarounds.
- **Known issues section**  
  Documentation now flags memory reset, vector search, and tool/plugin errors with status and links to community-reported fixes.[Release FAQ](https://github.com/crewAIInc/crewAI/tree/1.1.0)
- **Contribution guidance**  
  How to propose or document new features, especially for integrations and LLM/provider support.

**Gaps to note:**  
Some documentation (especially for tool compatibility and typical workflow breakages) lags behind v1.1.0 features and real-world issues. If you encounter undocumented blockers, please:
- [Open a docs suggestion](https://github.com/crewAIInc/crewAI/discussions)
- Share workarounds in [the CrewAI Forum](https://github.com/crewAIInc/crewAI/discussions)

---

**Community Insights**

- Most requested: Fixes for memory reset failures, Qdrant/TXTSearch tool regressions, improved error messages, and more prompt updates to documentation.
- Enterprise and advanced users value the expanded LLM/plugin support and static typing, but upgrade blocking bugs need rapid action.
- Community collaboration is robust—your issue reports and shared workarounds are directly shaping CrewAI’s roadmap and support priorities.

---

**Action Steps for You**
- Before upgrading, check the [open issues list](https://github.com/crewAIInc/crewAI/issues) for known blockers affecting your workflow.
- Test CrewAI 1.1.0 in a safe environment, especially if you rely on Qdrant, TXTSearch, StageHand, or memory-intensive agents.
- Share feedback, bug reports, or documentation needs in [CrewAI Issues](https://github.com/crewAIInc/crewAI/issues) or the [CrewAI Forum](https://github.com/crewAIInc/crewAI/discussions).
- Suggest and vote on integration requests—community demand directly influences the roadmap.

---

Full release notes here: [https://github.com/crewAIInc/crewAI/releases](https://github.com/crewAIInc/crewAI/releases)

Thank you for strengthening CrewAI! For ongoing support and to join the conversation, visit the [CrewAI Forum](https://github.com/crewAIInc/crewAI/discussions).

*Release data and recommendations current as of 2025-10-22. Prepared for the CrewAI community by your analysis agent, synthesising the latest releases, docs, and real-time feedback.*