# CrewAI 0.148.0 is out! 🚓

## Core Improvements & Fixes
- Utilized production WorkOS environment ID for enhanced stability.  
- Added SQLite FTS5 support for streamlined testing workflows.  
- Resolved agent knowledge handling issues for improved reliability.  
- Improved comparison mechanisms by transitioning to the BaseLLM class.  
- Fixed the missing `create_directory` parameter in the Task class for better functionality.  

## New Features & Enhancements
- Introduced agent evaluation functionality, pivotal for performance assessments.  
- Added evaluator experiment and regression testing methods.  
- Implemented a thread-safe AgentEvaluator to ensure safe concurrent operations.  
- Enabled event emissions for effective agent evaluation tracking.  
- Supported evaluation of both single Agent and LiteAgent types.  
- Integrated with neatlogs for enhanced logging capabilities.  
- Introduced crew context tracking for LLM guardrail events, improving oversight.  

## Documentation & Guides
- Updated documentation for guardrail attributes and added usage examples.  
- Provided a comprehensive integration guide for neatlogs.  
- Updated documentation for the Agent repository and details for Agent.kickoff usage.  

Full release notes here - [Read the full release notes](https://docs.crewai.com/release-notes/0.148.0).

---

### Notable Changes and Considerations
- Users should review the updated documentation to understand the new evaluation features and adapt to changes in task management. It's particularly important for enhancing performance through the new agent evaluation functionalities.

---

### Community Insights
- **Key Issues Identified**: Concerns around LLM response errors, local deployment difficulties, MCPTool errors, configuration challenges, and integration problems with external systems.
- **Community Sentiment**: Frustration over bugs and connectivity issues with local instances; however, there is a spirit of collaboration to find workarounds and share troubleshooting help.
- **Recommendations for Improvement**:
  - Prioritize high-importance bug fixes.
  - Enhance documentation for clearer guidance on integrations.
  - Foster community engagement to address issues more swiftly and effectively.

---

❤️ Thank you for shaping CrewAI. For support and to contribute solutions, please join the [community link] and keep building! 

--- 

**Legend**:  
🟠 = Recurring or still open  
✅ = Closed/resolved  
Release/data as of July 17, 2025. For feedback or clarification, please engage in the next community sync or initiate a thread.  

--- 

*Prepared based on releases, GitHub issues, docs, and community discussions from May 17, 2025 - July 17, 2025.*