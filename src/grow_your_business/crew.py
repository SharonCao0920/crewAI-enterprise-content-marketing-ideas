from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class GrowYourBusiness():
    """Business Growth Strategy Crew"""

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

    @agent
    def sales_strategist(self) -> Agent:
        return Agent(
            config=self.agents_config['sales_strategist'],
            verbose=True
        )

    @task
    def market_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['market_analysis_task'],
            output_file='market_analysis.md'
        )

    @task
    def content_strategy_task(self) -> Task:
        return Task(
            config=self.tasks_config['content_strategy_task'],
            output_file='content_strategy.md'
        )

    @task
    def sales_optimization_task(self) -> Task:
        return Task(
            config=self.tasks_config['sales_optimization_task'],
            output_file='sales_strategy.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the business growth strategy crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )