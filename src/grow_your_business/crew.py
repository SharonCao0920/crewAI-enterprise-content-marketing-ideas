from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class GrowYourBusiness():
    """PaycheckManager.com Business Growth Crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def market_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['market_researcher'],
            verbose=True
        )

    @agent
    def content_strategist(self) -> Agent:
        return Agent(
            config=self.agents_config['content_strategist'],
            verbose=True
        )

    @task
    def market_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['market_analysis_task'],
            output_file='market_research_report.md'
        )

    @task
    def content_strategy_task(self) -> Task:
        return Task(
            config=self.tasks_config['content_strategy_task'],
            output_file='marketing_strategy.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the PaycheckManager.com business growth crew"""
        return Crew(
            agents=[self.market_researcher(), self.content_strategist()],
            tasks=[self.market_analysis_task(), self.content_strategy_task()],
            process=Process.sequential,
            verbose=True
        )
    