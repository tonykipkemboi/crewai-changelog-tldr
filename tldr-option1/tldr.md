New Release: CrewAI 0.165.1 is out! 🚨

We are excited to share this patch release, building on v0.165.0's momentum. It focuses on stability for your AI agent workflows. As a community, we continue refining CrewAI to make it more reliable for developers and leaders alike. Update now to enhance your projects – test in staging first.

## Core Improvements & Fixes
- Fixed Chroma DB lockfiles for smoother database handling – [GitHub PR #1237](https://github.com/crewAIInc/crewAI/pull/1237).
- Resolved flaky tests and CI stability issues – [GitHub PRs #1235, #1236](https://github.com/crewAIInc/crewAI/pull/1235).
- Mocked telemetry to prevent disruptions – [GitHub PR #1236](https://github.com/crewAIInc/crewAI/pull/1236).
- Pinned OpenAI to <1.100.0, fixing import issues – [GitHub PR #1239](https://github.com/crewAIInc/crewAI/pull/1239).
- Removed AgentOps with migration to built-in tracing – [GitHub PR #1249](https://github.com/crewAIInc/crewAI/pull/1249).

## New Features & Enhancements
- Refined tracing with ephemeral logic for efficient short tasks – [Docs on Tracing](https://docs.crewai.com/core-concepts/tracing).
- Added Mem0 agent_id linking for better multi-agent memory recall – [Docs on Memory Systems](https://docs.crewai.com/core-concepts/memory).
- Enhanced tool compatibility, including XMLSearchTool configs – [GitHub PR #1234](https://github.com/crewAIInc/crewAI/pull/1234).

## Documentation & Guides
- Updated examples for Tool Repository and memory systems – [Docs on Tools](https://docs.crewai.com/core-concepts/tools).
- Revised migration guides for deprecations like AgentOps – [Docs on Tracing](https://docs.crewai.com/core-concepts/tracing).
- Added details on LLM integrations and stability – [Docs on LLM Integration](https://docs.crewai.com/core-concepts/llms).
- Blog post: "Advancing AI Agents with Memory and Tracing" – [Blog](https://blog.crewai.com/).

Full release notes here - [https://github.com/crewAIInc/crewAI/releases]

Community insights show positive sentiment on these enhancements, with no open issues. Mixed views on deprecations, but clear paths ease transitions. Share your experiences on [community.crewai.com] – we value your input to keep building together. If you hit edge cases, contribute via GitHub. Let's make CrewAI even stronger!