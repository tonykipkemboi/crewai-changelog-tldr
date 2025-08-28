New Release: CrewAI 0.175.0 is out! 🚨

## Core Improvements & Fixes
*   We removed the strict version pin on the OpenAI library. This resolves critical `ImportError` conflicts for many of you using modern setups.
*   We improved flow resumability for Human-in-the-Loop (HITL). Your complex, interactive crews are now more robust and reliable.

## New Features & Enhancements
*   You can now use a simplified RAG configuration. We have added native support for Qdrant to give you more powerful knowledge retrieval options.
*   We introduced new automation triggers. This provides a core capability for creating event-driven agent workflows.
*   We streamlined the login process and added a `crewai config reset` command to improve your developer experience.

## Documentation & Guides
*   You can find new documentation covering the new automation triggers feature.
*   We have added guidance for the new hybrid search alpha parameter.
*   We also corrected and improved our API reference documentation.

Full release notes here - [https://github.com/crewAIInc/crewAI/releases](https://github.com/crewAIInc/crewAI/releases)