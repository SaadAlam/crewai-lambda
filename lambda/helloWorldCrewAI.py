from crewai import Agent, Task, Crew
from Utils.utils import get_openai_api_key
import json, os

def lambda_handler(event, context):
    openai_api_key = get_openai_api_key()
    os.environ["OPENAI_MODEL_NAME"] = 'gpt-3.5-turbo'
    
    # Define the Agent and Task in CrewAI
    agent_backstory = "I am an AI assistant designed to help with AWS tasks. I can help with a wide range of AWS services."
    agent = Agent(role="AWS Assistant", goal="Help with AWS tasks", backstory=agent_backstory)
     # Define the expected output for the Task
    expected_output = "An explanation of how to create an S3 bucket in AWS."
    task = Task(description="Explain how to create an S3 bucket", agent=agent, expected_output=expected_output)
    
    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=1  # For more detailed logging (optional)
    )
    result = crew.kickoff(inputs={})

    response_data = str(result)  # If result is not JSON serializable

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"message": response_data})
    }
