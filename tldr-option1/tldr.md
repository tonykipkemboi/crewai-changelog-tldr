:police_car_light: CrewAI v0.150.0 is out! :police_car_light:

Here’s what you need to know about this release. These highlights focus on actionable improvements, open issues, and recommended next steps for everyone in the CrewAI community.

---

## Core Improvements & Fixes
- **Chroma Storage Safety:** Introduced file locking for the Chroma client, improving data reliability in concurrent and multi-process use.  
  [Chroma file lock details](https://github.com/crewAIInc/crewAI/releases/tag/v0.150.0)
- **LLM Stability Improvements:** Dropped outdated LLM stop parameters; upgraded to LiteLLM 1.74.3 for better large language model compatibility.  
  [LiteLLM upgrade notes](https://github.com/crewAIInc/crewAI/issues/3207)
- **Save Method & Messaging Fixes:** Addressed save method errors and messaging bugs, especially affecting Ollama local integration.
- **Deprecation of UserMemory:** Major step towards more robust agent storage and knowledge management.  
  [UserMemory deprecation guide](https://docs.crewai.com/user-memory-migration)
- **Mac OS Installation Fixes (in progress):** Actively investigating Mac dependency issues with ChromaDB/DB drivers.  
  [See open issue](https://github.com/crewAIInc/crewAI/issues/3202)

## New Features & Enhancements
- **Ad-hoc Tool Calling:** Agents can now flexibly call new tools at runtime, boosting extensibility without code changes.
- **Mem0 Storage v2:** Major backend update for faster, more consistent knowledge storage and retrieval for agents.  
  [Mem0 v2 docs](https://docs.crewai.com/mem0-v2)
- **SerperScrapeWebsiteTool Added:** Part of the research suite; supports powerful website scraping and content extraction.  
  [Tool documentation](https://github.com/crewAIInc/crewAI-tools/releases)
- **SQLite FTS5 Integration:** Native support brings stronger, faster in-memory and persistent search for RAG (retrieval-augmented generation) workflows.  
  [FTS5 notes](https://github.com/crewAIInc/crewAI-tools/issues/342)
- **Bedrock AgentCore Browser/Code Toolkit:** Stagehand and core browser/code tools refactored for reliability and automation.  
- **Tool Refactoring & Bugfixes:** Weave kickoff and MongoDBVectorSearchTool improvements increase stability for multi-agent research and database operations.

## Documentation & Guides
- **Tavily Search & Extractor:** Comprehensive new guides on integrating search and web extraction tools.  
  [Tavily docs](https://docs.crewai.com/tools/tavily)
- **SerperScrapeWebsite Tool:** Added usage and troubleshooting documentation for advanced scraping use cases.
- **Migration Guides:** Step-by-step docs for deprecations—especially UserMemory → Mem0 v2—now highlighted.
- **Tool Installation and Upgrade Notes:** Clearer requirements, especially around SQLite FTS5 and external dependencies.
- **Community FAQs:** Outlined solutions for top blockers, including import errors, DB support requests, and breaking API changes.  
  [FAQ section in docs](https://docs.crewai.com/faq)

---

**Action Points:**
- If you use UserMemory, you must follow the [migration guide](https://docs.crewai.com/user-memory-migration).
- Test workflows that rely on tool imports or custom LLM endpoints—several [import bugs](https://github.com/crewAIInc/crewAI/issues/3210) remain open.
- Share and upvote bugs or reproducible cases in [GitHub issues](https://github.com/crewAIInc/crewAI/issues) to help prioritise fixes.
- Review new guides and consider contributing your own migration steps, especially if you hit issues.

**Current high-priority open issues:**  
- TavilySearchTool import failures  
- Custom LLM endpoint failures  
- Ollama local integration bugs  
- Logging and output conflicts  
- ChromaDB Mac compatibility  
- Weave and DirectoryReadTool hangs

See details or join the discussion:  
[Open CrewAI Issues](https://github.com/crewAIInc/crewAI/issues) | [crewai-tools Issues](https://github.com/crewAIInc/crewAI-tools/issues)

---

Full release notes here – [https://github.com/crewAIInc/crewAI/releases](https://github.com/crewAIInc/crewAI/releases)

❤️ Thank you for shaping CrewAI—your feedback and collaboration drive each release. Join us on GitHub or in the community threads, and let’s keep building!