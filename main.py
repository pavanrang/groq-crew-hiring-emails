import os
import time
import csv
from crewai import Crew
from langchain_groq import ChatGroq
from agents import EmailPersonalizationAgents
from tasks import PersonalizeEmailTask

# 0. Setup environment
from dotenv import load_dotenv
load_dotenv()

email_template = """
Dear [Name],

I hope you're well. I'm Satya Viswa Pavan Ranga, currently pursuing my Masters in Analytics with a focus on Statistical Modeling at Northeastern University. I'm impressed by [Company]'s innovative approach to data-driven decision-making.

With a Bachelor's in Computer Science and Engineering and experience at Cognizant, I've honed skills in data management and statistical analysis. Projects include creating ingestion flows for Amex and analyzing Airbnb listings using ML.

I'm keen to contribute my expertise in Python, R, SQL, and visualization tools to [Company]'s objectives. Could we discuss potential opportunities further?

Best regards,

Satya Viswa Pavan Ranga
"""

# 1. Create agents
agents = EmailPersonalizationAgents()

email_personalizer = agents.personalize_email_agent()
ghostwriter = agents.ghostwriter_agent()

# 2. Create tasks
tasks = PersonalizeEmailTask()

personalize_email_tasks = []
ghostwrite_email_tasks = []

# Path to the CSV file containing client information
csv_file_path = 'data/hiring_manager_data.csv'

# Open the CSV file
with open(csv_file_path, mode='r', newline='') as file:
    # Create a CSV reader object
    csv_reader = csv.DictReader(file)

    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Access each field in the row
        recipient = {
            'first_name': row['first_name'],
            'last_name': row['last_name'],
            'email': row['email'],
            'bio': row['bio'],
            'last_conversation': row['last_conversation'],
            'Company':row['Company']
        }

        # Create a personalize_email task for each recipient
        personalize_email_task = tasks.personalize_email(
            agent=email_personalizer,
            recipient=recipient,
            email_template=email_template
        )

        # Create a ghostwrite_email task for each recipient
        ghostwrite_email_task = tasks.ghostwrite_email(
            agent=ghostwriter,
            draft_email=personalize_email_task,
            recipient=recipient
        )

        # Add the task to the crew
        personalize_email_tasks.append(personalize_email_task)
        ghostwrite_email_tasks.append(ghostwrite_email_task)


# Setup Crew
crew = Crew(
    agents=[
        email_personalizer,
        ghostwriter
    ],
    tasks=[
        *personalize_email_tasks,
        *ghostwrite_email_tasks
    ],
    max_rpm=29
)

# Kick off the crew
start_time = time.time()

results = crew.kickoff()

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Crew kickoff took {elapsed_time} seconds.")
print("Crew usage", crew.usage_metrics)
