# Releases Crew

Run using `crewai run`

**Base**
Created using `crewai create crew releases`
Modified by Tony_Wood

**Contributors:**  
Tony_Wood
Max_Moura
zinyando

---

## 🧠 CrewAI Agent System Overview

This system leverages CrewAI to keep the team and community updated on key developments.

---

## 🔄 What It Does

### Crew 1 – `read_releases`: Get Major Releases
- Reads major releases
- Tracks CrewAI releases (e.g., from the last two months)
- Extracts and summarises important changes

### Crew 2 – `release_insights`: Display Major Releases
- Displays and prints information about the latest releases
- Provides context for why each release is important
- Formats release notes for easy reading

### Crew 3 – `read_issues`: Get Issues
- Fetches and shows issues
- Collects the latest issues from GitHub and other sources

### Crew 4 – `issue_insights`: Display Issues
- Highlights trends and common problems for quick action

### Crew 5 – `read_community`: Find Community Info
- Monitors community discussions
- Reads CrewAI forum content

### Crew 6 – `community_insights`: Summarise Community Issues
- Surfaces key insights, FAQs, and community concerns

### Crew 7 – `insights`: Cross-Source Insights
- Identifies common patterns between releases, issues, and community messages

### Crew 8 - `tldr`: To long didnt read version
- Takes the inforamtion in insights and give a short faster to read version

---

## ⚙️ Uses

- Keeps community informed
- Supports community engagement and assistance
- Provides product and operations teams with visibility into issues and updates
- Surfaces insights from the community

---

## Technical Notes

This project is based on the standard CrewAI "create crew" format, with minimal changes to maintain compatibility and simplicity. The focus is on the crew structure and community contribution, rather than code customisation.  
The setup uses the base CrewAI configuration and simple LLMs (currently GPT-4.1).  
No additional dependencies are required beyond those generally installed (such as path and date utilities).
By breaking down the tasks we reduce the chances of hallucinations; so in the authors opinion it is worth the extra time

**Tools used:**  
- Serper  
- Website Scrap

**Templates for reports:**
The `knowledge` folder contains all the templates for the reports. These ensure that we have a consistant output 

Swap the templates for `tldr_template2.md` or `tldr_template.md` to pick preferred format 

**Reports:**
The reports are created in the root directory

**API keys needed**
You will need accounts and keys for the following in `.env`

`MODEL=gpt-4.1`
`OPENAI_API_KEY="..."`
`SERPER_API_KEY="..."`

**Key Inputs**
Change `release="0.148.0"` in `main.py` before each run so it can point at the latest version. 

## Key Knowledge Sources

- **Release notes:**
-  https://docs.crewai.com/release-notes
-  We also use https://github.com/crewAIInc/crewAI/releases/ as sometimes release-notes is slow to update
- 
- **Issues:**  
  - https://github.com/crewAIInc/crewAI-tools/issues/  
  - https://github.com/crewAIInc/crewAI/issues/
- **Community:** https://community.crewai.com/
- **Extra information:**  
  - https://blog.crewai.com/  
  - https://docs.crewai.com/

---

## Language and Accessibility

- English is not assumed to be the first language for all community members; a clear and simple style is used.
- Formatting is selected to be dyslexia-friendly.
- UK English spelling is used.

---

## Reporting

Many reporting features are commented out to reduce noise during normal operation, though they were useful during development.

`insights.md` provides a TL;DR update for the community.

Other reports are generated to provide context for the final summary.  
The primary goal is to deliver essential information to the community as quickly as possible.

---

## Future Ideas

- This project could evolve into an MCP accessible from other Crews, allowing the community to stay updated.
- Potentially useful as an MCP for debugging crews or for tools like Cursor when investigating issues.

---

## Known Issues

- The community at [community.crewai.com](https://community.crewai.com/) is not publicly accessible, so only topics and short previews can be scraped.
