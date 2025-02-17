#!/usr/bin/env python
import sys
import warnings
from grow_your_business.crew import GrowYourBusiness

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew with business inputs.
    """
    inputs = {
        'company': 'PaycheckManager.com',
        'market': 'Small businesses with 1-50 employees',
        'goal': 'Increase subscriber base and market share',
        'industry': 'B2B SaaS',
        'target_segment': 'small business segment'
    }
    GrowYourBusiness().crew().kickoff(inputs=inputs)

def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'company': 'PaycheckManager.com',
        'market': 'Small businesses with 1-50 employees',
        'goal': 'Increase subscriber base and market share',
        'industry': 'B2B SaaS',
        'target_segment': 'small business segment'
    }
    try:
        GrowYourBusiness().crew().train(
            n_iterations=int(sys.argv[1]),
            filename=sys.argv[2],
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        GrowYourBusiness().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'company': 'PaycheckManager.com',
        'market': 'Small businesses with 1-50 employees',
        'goal': 'Increase subscriber base and market share',
        'industry': 'B2B SaaS',
        'target_segment': 'small business segment'
    }
    try:
        GrowYourBusiness().crew().test(
            n_iterations=int(sys.argv[1]),
            openai_model_name=sys.argv[2],
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == "__main__":
    run()