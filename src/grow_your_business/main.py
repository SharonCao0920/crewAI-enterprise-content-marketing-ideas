#!/usr/bin/env python
import sys
from grow_your_business.crew import GrowYourBusiness

def run():
    """Run the crew with three focused inputs."""
    company_name = "PaycheckManager.com"
    target_market = "Small businesses with 1-50 employees"
    primary_goal = "Increase subscriber base and market share"

    crew_manager = GrowYourBusiness()
    crew = crew_manager.get_crew(
        company_name=company_name,
        target_market=target_market,
        primary_goal=primary_goal
    )
    
    result = crew.kickoff()
    print(result)

def train():
    """Train the crew with multiple iterations."""
    company_name = "PaycheckManager.com"
    target_market = "Small businesses with 1-50 employees"
    primary_goal = "Increase subscriber base and market share"

    try:
        crew_manager = GrowYourBusiness()
        crew = crew_manager.get_crew(
            company_name=company_name,
            target_market=target_market,
            primary_goal=primary_goal
        )
        
        result = crew.train(
            n_iterations=int(sys.argv[1]),
            filename=sys.argv[2]
        )
        print(result)
    except Exception as e:
        print(f"Training error: {e}")

def replay():
    """Replay a specific task execution."""
    company_name = "PaycheckManager.com"
    target_market = "Small businesses with 1-50 employees"
    primary_goal = "Increase subscriber base and market share"

    try:
        crew_manager = GrowYourBusiness()
        crew = crew_manager.get_crew(
            company_name=company_name,
            target_market=target_market,
            primary_goal=primary_goal
        )
        
        result = crew.replay(task_id=sys.argv[1])
        print(result)
    except Exception as e:
        print(f"Replay error: {e}")

def test():
    """Test the crew with different configurations."""
    company_name = "PaycheckManager.com"
    target_market = "Small businesses with 1-50 employees"
    primary_goal = "Increase subscriber base and market share"

    try:
        crew_manager = GrowYourBusiness()
        crew = crew_manager.get_crew(
            company_name=company_name,
            target_market=target_market,
            primary_goal=primary_goal
        )
        
        result = crew.test(
            n_iterations=int(sys.argv[1]),
            openai_model_name=sys.argv[2]
        )
        print(result)
    except Exception as e:
        print(f"Testing error: {e}")

def main():
    """Main function to handle different command line arguments."""
    if len(sys.argv) < 2:
        run()
    else:
        command = sys.argv[1]
        if command == "train":
            if len(sys.argv) < 4:
                print("Usage: python main.py train <n_iterations> <output_filename>")
                return
            train()
        elif command == "replay":
            if len(sys.argv) < 3:
                print("Usage: python main.py replay <task_id>")
                return
            replay()
        elif command == "test":
            if len(sys.argv) < 4:
                print("Usage: python main.py test <n_iterations> <model_name>")
                return
            test()
        else:
            print("Unknown command. Available commands: train, replay, test")

if __name__ == "__main__":
    main()