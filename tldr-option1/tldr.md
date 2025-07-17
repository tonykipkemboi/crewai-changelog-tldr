:police_car_light: CrewAI 0.148.0 is out! :police_car_light:

Here’s the essential overview for CrewAI version 0.148.0—the biggest updates, critical fixes, and must-read community insights to keep your agents running reliably this quarter.

---

## Core Improvements & Fixes

- **Agent Evaluation Upgrade**
  - New AgentEvaluator module brings regression testing, thread-safety, and LLM event tracking.  
  - Expanded test coverage includes SQLite FTS5 and single/LiteAgent evaluation modes.
  - [AgentEvaluator issue details](https://github.com/crewAIInc/crewAI/releases/tag/0.148.0)

- **Logging and Memory**
  - Integrated neatlogs for cleaner, context-rich agent logs.
  - Improved logging for workflow step-tracking and debugging.
  - Memory handling refactored (though see known issues below).
  - [Memory issues and fixes](https://github.com/crewAIInc/crewAI/issues/3169)

- **Critical Bugfixes**
  - Fixed task class and knowledge handling errors.
  - Corrected directory parameter inconsistencies in workflows.
  - [Release changelog](https://github.com/crewAIInc/crewAI/releases/tag/0.148.0)

---

## New Features & Enhancements

- **Guardrails & Agent Safeguards**
  - Brand new guide and implementation for agent guardrails—define safe, reliable agent mission boundaries.
  - [Guardrails documentation](https://docs.crewai.com/)

- **Expanded LLM (Large Language Model) Integration**
  - Support and docs for multiple LLM endpoints: HuggingFace, Azure, OpenRouter, Ollama, and more.
  - Enhanced context management for custom endpoints.
  - [LLM Integration Guide](https://docs.crewai.com/)

- **Composable Agent Workflows**
  - Reinforced crew context tracking: agents now pass context seamlessly through LLM event chains (with improved visibility during debugging).
  - “Composability” now a focus—easier to build and chain robust, reusable agent flows.
  - [CrewAI blog: Building dependable agents](https://blog.crewai.com/build-agents-to-be-dependable/)

---

## Documentation & Guides

- **Major Doc Expansion (July 2025)**
  - New and revamped guides:  
    - [Introduction, Agent Concepts, Flows](https://docs.crewai.com/)
    - [Memory: Scoping, Persistence, Deletion](https://docs.crewai.com/)
    - [LLM Provider Setup](https://docs.crewai.com/)
    - [Deployment Practices: Docker, CI/CD, Troubleshooting](https://docs.crewai.com/)
    - [Agent Evaluation and Guardrail Guides](https://docs.crewai.com/)
  - Quick tips:
    - If your deployment hangs in CI/CD—check new “Deployment” section and follow forum workarounds.
    - Review new FAQ addressing persistent memory bugs and tool invocation issues.

- **Lead Blog and Community Insights**
  - [How-To: Build agents that “don’t break”](https://blog.crewai.com/build-agents-to-be-dependable/)
  - [Active support threads: Installation/dependency errors](https://community.crewai.com/c/community-support/7/l/top)
  - [Memory and agent isolation discussions](https://community.crewai.com/c/community-support/7/)

---

**Ongoing Key Issues:**
- 🟠 _Not yet fixed:_  
    - **Memory leaks or undeletable agent knowledge** ([#3169](https://github.com/crewAIInc/crewAI/issues/3169))
    - **Agents failing to invoke tools, just “simulate” results** ([#3154](https://github.com/crewAIInc/crewAI/issues/3154))
    - **Integration bugs with custom/local LLM providers—especially OpenRouter, HuggingFace, and Ollama** ([#3165](https://github.com/crewAIInc/crewAI/issues/3165))
    - **Interactive prompt breaks CI/CD or Docker deployments** ([#3163](https://github.com/crewAIInc/crewAI/issues/3163))

- _Most critical bugs are still open._ Stay tuned on those GitHub tickets and upvote if they impact you.

**Community Trends:**
- Top requests: bulletproof agent knowledge deletion, easier plug-and-play with LLMs, zero-interaction deployment, and “fix the tool call bug”.
- New docs and blogs focus on making “system doesn’t break” a real user experience—support this by joining the [forum](https://community.crewai.com/c/community-support/7/) and sharing your deployment lessons.

---

For details, workarounds, and direct community help, check the full release notes:

**Full release notes here – [https://github.com/crewAIInc/crewAI/releases](https://github.com/crewAIInc/crewAI/releases)**

Thank you for powering CrewAI’s evolution. Your feedback and collaboration drive every improvement—keep reporting, sharing, and building the next wave of agent workflows.

---

*For help, post in the [CrewAI Community Forum](https://community.crewai.com/c/community-support/7/) and consult [CrewAI documentation](https://docs.crewai.com/).*