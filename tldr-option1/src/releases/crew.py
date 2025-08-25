from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

# include libraries for tools
from crewai_tools import SerperDevTool
from crewai_tools import ScrapeWebsiteTool


grok_4_llm = LLM(
    model="xai/grok-4-latest",
    stream=False,
    temperature=0.7,
    drop_params=True,
    additional_drop_params=["stop"]
)

gpt_5_llm = LLM(
    model="openai/gpt-5",
    drop_params=True,
    additional_drop_params=["stop", "temperature"]
)


llm_tasks = grok_4_llm

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class Releases():
    """Releases crew for tracking and analyzing CrewAI releases, issues, and community feedback"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def read_releases(self) -> Agent:
        return Agent(
            config=self.agents_config['read_releases'],
            verbose=True,
            reasoning=True,
            markdown=True,
            memory=True,
            llm=llm_tasks,
            inject_data=True,
        )

    @agent
    def release_insights(self) -> Agent:
        return Agent(
            config=self.agents_config['release_insights'],
            verbose=True,
            reasoning=True,
            markdown=True,
            memory=True,
            llm=llm_tasks,
            inject_data=True,
        )   

    @agent
    def read_issues(self) -> Agent:
        return Agent(
            config=self.agents_config['read_issues'],
            verbose=True,
            reasoning=True,
            markdown=True,
            memory=True,
            llm=llm_tasks,
            inject_data=True,
        )

    @agent
    def issue_insights(self) -> Agent:
        return Agent(
            config=self.agents_config['issue_insights'],
            verbose=True,
            reasoning=True,
            markdown=True,
            memory=True,
            llm=llm_tasks,
            inject_data=True,
        )

    @agent
    def read_community(self) -> Agent:
        return Agent(
            config=self.agents_config['read_community'],
            verbose=True,
            reasoning=True,
            markdown=True,
            memory=True,
            llm=llm_tasks,
            inject_data=True,
        )

    @agent
    def community_insights(self) -> Agent:
        return Agent(
            config=self.agents_config['community_insights'],
            verbose=True,
            reasoning=True,
            markdown=True,
            memory=True,
            llm=llm_tasks,
            inject_data=True,
        )

    @agent
    def insights(self) -> Agent:
        return Agent(
            config=self.agents_config['insights'],
            reasoning=True,
            markdown=True,
            memory=True,
            verbose=True,
            llm=llm_tasks,
            inject_data=True,
        )
    
    @agent
    def tldr(self) -> Agent:
        return Agent(
            config=self.agents_config['tldr'],
            reasoning=True,
            markdown=True,
            memory=True,
            verbose=True,
            llm=llm_tasks,
            inject_data=True,
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def read_releases_task(self) -> Task:
        return Task(
            config=self.tasks_config['read_releases_task'],
            #output_file='releases.md',
            tools=[SerperDevTool(), ScrapeWebsiteTool()]
        )

    @task
    def release_insights_task(self) -> Task:
        return Task(
            config=self.tasks_config['release_insights_task'],
            #output_file='release_insights.md',
            tools=[SerperDevTool(), ScrapeWebsiteTool()]
        )

    @task
    def read_issues_task(self) -> Task:
        return Task(
            config=self.tasks_config['read_issues_task'],
            #output_file='issues.md',
            tools=[SerperDevTool(), ScrapeWebsiteTool()]
        )

    @task
    def issue_insights_task(self) -> Task:
        return Task(
            config=self.tasks_config['issue_insights_task'],
            #output_file='issue_insights.md',
            tools=[SerperDevTool(), ScrapeWebsiteTool()]
        )

    @task
    def read_community_task(self) -> Task:
        return Task(
            config=self.tasks_config['read_community_task'],
            #output_file='community.md',
            tools=[SerperDevTool(), ScrapeWebsiteTool()]
        )

    @task
    def community_insights_task(self) -> Task:
        return Task(
            config=self.tasks_config['community_insights_task'],
            #output_file='community_insights.md',
            tools=[SerperDevTool(), ScrapeWebsiteTool()]
        )

    @task
    def insights_task(self) -> Task:
        return Task(
            config=self.tasks_config['insights_task'],
            output_file='insights.md',
            tools=[SerperDevTool(), ScrapeWebsiteTool()]
        )

    @task
    def tldr_task(self) -> Task:
        return Task(
            config=self.tasks_config['tldr_task'],
            output_file='tldr.md',
        )
    @crew
    def crew(self) -> Crew:
        """Creates the Releases crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge


        # only use this if you are using the hierarchical process
        manager = Agent(
			role="Releases Crew Manager",
			goal="""    
				As the Releases Crew Manager, your mission is to coordinate and oversee the tracking and analysis of CrewAI releases, issues, and community feedback.
				Responsibilities:
				1. Ensure all agents gather and synthesize information on releases, issues, and community sentiment.
				2. Define clear deliverables and success metrics for each analysis task.
				3. Establish dependencies and workflow between agents to maximize insight and minimize duplication.
				4. Monitor progress and quality of outputs, ensuring actionable insights are produced.
				5. Align the crew's work with the overall goals of improving CrewAI based on real-world feedback and release data.
			""",
			backstory="""
				You are an expert in software release management and community engagement. You excel at orchestrating teams to extract valuable insights from release notes, issue trackers, and user feedback.
				Your leadership ensures that all findings are actionable and drive continuous improvement for CrewAI.
			""",
			allow_delegation=True,
			max_iterations=50,
		)
 

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            memory=True,
            #manager_agent=manager,
            #process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
