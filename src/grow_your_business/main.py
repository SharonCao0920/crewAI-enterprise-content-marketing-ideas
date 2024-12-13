#!/usr/bin/env python
import sys
import warnings

from grow_your_business.crew import GrowYourBusiness

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew with multiple inputs.
    """
    inputs = {
        'company': 'PaycheckManager.com',
        'target_market': 'Small businesses with 1-50 employees',
        'growth_goal': 'Increase subscribers by 15%',
        'primary_challenge': 'Reduce customer acquisition costs',
        'key_differentiator': 'Most affordable and user-friendly payroll solution'
    }
    GrowYourBusiness().crew().kickoff(inputs=inputs)

def train():
    """
    Train the crew with multiple inputs.
    """
    inputs = {
        'company': 'PaycheckManager.com',
        'target_market': 'Small businesses with 1-50 employees',
        'growth_goal': 'Increase subscribers by 15%',
        'primary_challenge': 'Reduce customer acquisition costs',
        'key_differentiator': 'Most affordable and user-friendly payroll solution'
    }
    try:
        GrowYourBusiness().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
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
        'target_market': 'Small businesses with 1-50 employees',
        'growth_goal': 'Increase subscribers by 15%',
        'primary_challenge': 'Reduce customer acquisition costs',
        'key_differentiator': 'Most affordable and user-friendly payroll solution'
    }
    try:
        GrowYourBusiness().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

# #!/usr/bin/env python
# import sys
# import warnings

# from grow_your_business.crew import GrowYourBusiness

# warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# # This main file is intended to be a way for you to run your
# # crew locally, so refrain from adding unnecessary logic into this file.
# # Replace with inputs you want to test with, it will automatically
# # interpolate any tasks and agents information

# def run():
#     """
#     Run the crew.
#     """
#     inputs = {
#         'topic': 'AI LLMs'
#     }
#     GrowYourBusiness().crew().kickoff(inputs=inputs)


# def train():
#     """
#     Train the crew for a given number of iterations.
#     """
#     inputs = {
#         "topic": "AI LLMs"
#     }
#     try:
#         GrowYourBusiness().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

#     except Exception as e:
#         raise Exception(f"An error occurred while training the crew: {e}")

# def replay():
#     """
#     Replay the crew execution from a specific task.
#     """
#     try:
#         GrowYourBusiness().crew().replay(task_id=sys.argv[1])

#     except Exception as e:
#         raise Exception(f"An error occurred while replaying the crew: {e}")

# def test():
#     """
#     Test the crew execution and returns the results.
#     """
#     inputs = {
#         "topic": "AI LLMs"
#     }
#     try:
#         GrowYourBusiness().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

#     except Exception as e:
#         raise Exception(f"An error occurred while replaying the crew: {e}")
