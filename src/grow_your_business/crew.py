from crewai import Agent, Crew, Process, Task
from textwrap import dedent

class GrowYourBusiness:
    """PaycheckManager.com Business Growth Crew"""
    
    def __init__(self):
        self.market_researcher = Agent(
            name="Market Researcher",
            role="Market Research Strategist",
            goal="Analyze small business payroll market to identify growth opportunities",
            backstory=dedent("""
                A market research expert with deep expertise in B2B SaaS and HR technology. 
                Specializes in analyzing market trends and competitive landscapes to provide 
                actionable insights for business growth.
            """),
            verbose=True,
            allow_delegation=False
        )
        
        self.content_strategist = Agent(
            name="Content Strategist",
            role="Marketing Strategy Expert",
            goal="Develop targeted marketing strategies to increase subscriber base",
            backstory=dedent("""
                A strategic marketing professional specializing in B2B SaaS marketing. 
                Expert at developing compelling marketing campaigns that highlight product 
                benefits and drive customer acquisition.
            """),
            verbose=True,
            allow_delegation=False
        )
        
        self.sales_strategist = Agent(
            name="Sales Strategist",
            role="Sales Growth Specialist",
            goal="Optimize sales funnel and conversion strategies",
            backstory=dedent("""
                A sales expert focused on B2B SaaS platforms with proven experience in 
                developing effective sales strategies and improving conversion rates.
            """),
            verbose=True,
            allow_delegation=False
        )

    def get_crew(self, company_name, target_market, primary_goal):
        """Create and return the crew with proper task assignments"""
        
        market_analysis = Task(
            description=f"Analyze {company_name}'s market position in {target_market}",
            agent=self.market_researcher,
            expected_output="Detailed market analysis report with competitor insights and growth opportunities"
        )

        content_strategy = Task(
            description=f"Create marketing strategy for {company_name} to achieve {primary_goal}",
            agent=self.content_strategist,
            expected_output="Comprehensive marketing strategy document with campaign frameworks and channel recommendations"
        )

        sales_optimization = Task(
            description=f"Develop sales strategy for {company_name} focused on {target_market}",
            agent=self.sales_strategist,
            expected_output="Complete sales optimization plan with funnel improvements and conversion tactics"
        )

        return Crew(
            agents=[
                self.market_researcher,
                self.content_strategist,
                self.sales_strategist
            ],
            tasks=[
                market_analysis,
                content_strategy,
                sales_optimization
            ],
            verbose=True,
            process=Process.sequential
        )