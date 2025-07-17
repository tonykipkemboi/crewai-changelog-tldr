# CrewAI Major Releases Analysis (May 17, 2025 - July 17, 2025)

## 🚀 Major Release Overview

1. **Version 0.148.0** (Released on July 16, 2025)
   - **Core Improvements & Fixes:**
     - Utilized production WorkOS environment ID for enhanced stability.
     - Added SQLite FTS5 support for streamlined testing workflows.
     - Resolved agent knowledge handling issues for improved reliability.
     - Improved comparison mechanisms by transitioning to the BaseLLM class.
     - Fixed the missing `create_directory` parameter in the Task class for better functionality.
   - **New Features & Enhancements:**
     - Introduced agent evaluation functionality, pivotal for performance assessments.
     - Added evaluator experiment and regression testing methods.
     - Implemented a thread-safe AgentEvaluator to ensure safe concurrent operations.
     - Enabled event emissions for effective agent evaluation tracking.
     - Supported evaluation of both single Agent and LiteAgent types.
     - Integrated with neatlogs for enhanced logging capabilities.
     - Introduced crew context tracking for LLM guardrail events, improving oversight.
   - **Documentation & Guides:**
     - Updated documentation for guardrail attributes and added usage examples.
     - Provided a comprehensive integration guide for neatlogs.
     - Updated documentation for the Agent repository and details for Agent.kickoff usage.

2. **Version 0.141.0** (Released on July 9, 2025)
   - **Core Improvements & Fixes:**
     - Enhanced GitHub Actions tests through parallel execution, boosting efficiency.
   - **New Features & Enhancements:**
     - Added crew context tracking for LLM guardrail events to improve monitoring.
   - **Documentation & Guides:**
     - Added documentation specific to Agent repository usage and details on the Agent.kickoff method.

3. **Version 0.140.0** (Released on July 2, 2025)
   - **Core Improvements & Fixes:**
     - Fixed typos in test prompts and ensured project normalization.
     - Enforced uppercase formatting for environment variables.
     - Updated LiteLLM dependency and refined collection handling in RAGStorage.
     - Implemented PEP 621 dynamic versioning for better package management.
   - **New Features & Enhancements:**
     - Introduced capabilities for tracking LLM calls per task and agent.
     - Added MemoryEvents for monitoring memory usage.
     - Enhanced support for models up to 7B parameters and added analytics tracking tools.
   - **Documentation & Guides:**
     - Updated CLI LLM documentation and various integration details.

4. **Version 0.134.0** (Released on June 25, 2025)
   - **Core Improvements & Fixes:**
     - Fixed parameter syntax issues and improved compatibility with Pydantic versions.
     - Upgraded code examples for Langfuse to the latest Python SDK.
   - **New Features & Enhancements:**
     - Introduced initialization for tools from defined attributes and improved MCP tools support.
   - **Documentation & Guides:**
     - Created comprehensive docs for LLM guardrail events and improved service integration documentation.

## ⚠️ Notable Changes and Considerations
- The latest versions brought significant enhancements in performance and user experience, especially through the introduction of agent evaluation functionalities.
- Users are encouraged to review documentation updates to adapt to changes in task management and agent handling, particularly with respect to the new evaluation features.

## 🎉 Acknowledgments
- Special thanks to the contributors whose continuous efforts have driven these software improvements forward, facilitating enhanced features and stability for users of CrewAI.

---

*For more detailed information, please visit our [documentation](https://docs.crewai.com) or check the [GitHub repository](https://github.com/crewAIInc/crewAI).*

----------

### Categorized Issues for Version 0.148.0 (Date Range: 2025-05-17 to 2025-07-17)

#### From crewAI-tools Repository:
1. **Open Issues**:
   - **[BUG]** SeleniumScrapingTool only works the first time 
     - Issue #379, opened on Jul 13, 2025
     - *Priority: Medium*
   - **[ENHANCEMENT]** DirectoryReadTool produces huge content because of os.walk 
     - Issue #342, opened on Jun 24, 2025
     - *Priority: Low*
   - **[BUG]** Remote MCP auth issue? 
     - Issue #318, opened on Jun 02, 2025
     - *Priority: High*
   - **[FEATURE REQUEST]** Add Tool Filtering to crewai-tools MCPServerAdapter 
     - Issue #317, opened on May 30, 2025
     - *Priority: Medium*
   - **[ERROR]** SERPERDEV tool error 
     - Issue #303, opened on May 12, 2025
     - *Priority: Low*

#### From crewAI Repository:
1. **Open Issues**:
   - **[BUG]** crewAI not working with local ollama 
     - Issue #3176, opened on Jul 17, 2025
     - *Priority: High*
   - **[FEATURE REQUEST]** Support extra_headers param in LLM object 
     - Issue #3177, opened on Jul 17, 2025
     - *Priority: Medium*
   - **[FEATURE REQUEST]** We need structured output capabilities that can be compatible with more models. 
     - Issue #3174, opened on Jul 17, 2025
     - *Priority: Medium*
   - **[BUG]** LLM Failed with Custom OpenAI-Compatible Endpoint 
     - Issue #3165, opened on Jul 15, 2025
     - *Priority: High*
   - **[BUG]** MCPServerAdapter calls click.confirm() in __init__ 
     - Issue #3163, opened on Jul 15, 2025
     - *Priority: High*
   - **[BUG]** 🐞Agent does not invoke tools correctly 
     - Issue #3154, opened on Jul 14, 2025
     - *Priority: High*
   - **[FEATURE REQUEST]** Sequential chunk-based analysis, agent memory aggregation, and summarization for large files 
     - Issue #3144, opened on Jul 13, 2025
     - *Priority: Medium*

----------

## CrewAI Community Discussions and Feedback (May 17, 2025 - July 17, 2025)

### Key Issues Identified: 
1. **LLM Response Errors**: Community members reported problems such as "ValueError: Invalid response from LLM call," which has affected their workflow significantly.
2. **Local Deployment Issues**: A common theme in discussions is the failure of CrewAI when trying to run it with local instances of models like llama.cpp, disrupting intended functionalities.
3. **MCPTool Errors**: Users pointed out issues with the "Event loop is closed" error when calling MCP tools, which has created barriers in their automation tasks.
4. **Configuration Challenges**: Members experienced difficulties setting up various agents and handling commands related to their MCP servers, leading to a proliferation of troubleshooting requests in the community.
5. **Integration Problems**: There were repeated mentions of connectivity issues with external systems and other LLM services, indicating challenges in environment compatibility.

### Community Sentiment:
- There was a notable frustration among users trying to integrate or use the new enhancements from version 0.148.0, especially concerning local and third-party LLM connections.
- Users have been active in seeking help and sharing their troubleshooting experiences, reflecting a collaborative spirit despite the technical hurdles encountered. Many threads were initiated to discuss workaround strategies and best practices.
- Overall, the sentiment was mixed; while some users appreciated the new features, the critical bugs have generated a sense of urgency for fixes and developments.

### Recommendations for Improvement:
- **Prioritize Bug Fixes**: High-priority bugs affecting local deployments and tool functionalities need to be addressed promptly.
- **Enhanced Documentation**: Clearer integration guides and troubleshooting sections could lead to reduced confusion and improve user experience.
- **Community Engagement**: Regular check-ins by developers in the community support threads could foster a better relationship and potentially quicken resolution times for reported issues.

These insights can help guide adjustments and developments in CrewAI, focusing on enhancing the user experience and addressing technical shortcomings as highlighted by active discussions from the community.

--- 

❤️ Thank you for shaping CrewAI. For the latest support and to contribute a solution, join [community link] and keep building!

---

**Legend**:  
🟠 = Recurring or still open  
✅ = Closed/resolved  
Release/data as of July 17, 2025. For feedback or clarification, reply in the next community sync or open a thread.

---

*Prepared by Cross-Analysis Agent based on releases, GitHub issues, docs, community threads, and official blog posts, May 17, 2025 - July 17, 2025.*