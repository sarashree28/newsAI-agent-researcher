from crewai import Agent
from tools import tool
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import os


## call the gemini models
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                           verbose=True,
                           temperature=0.5,
                           google_api_key=os.getenv("GOOGLE_API_KEY"))

# Creating a senior researcher agent with memory and verbose mode

news_researcher=Agent(
    role="Senior Researcher",
    goal='Unccover ground breaking technologies in {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity, you're at the forefront of"
        "innovation, eager to explore and share knowledge that could change"
        "the world."

    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True

)

## creating a write agent with custom tools responsible in writing news blog

news_writer = Agent(
  role='Writer',
  goal='Narrate compelling tech stories about {topic}',
  verbose=True,
  memory=True,
  backstory=(
    "With a flair for simplifying complex topics, you craft"
    "engaging narratives that captivate and educate, bringing new"
    "discoveries to light in an accessible manner."
  ),
  tools=[tool],
  llm=llm,
  allow_delegation=True
)

# Data Analyst Agent
data_analyst = Agent(
    role="Data Analyst",
    goal="Analyze data and uncover trends in {topic} using data-driven insights.",
    verbose=True,
    memory=True,
    backstory="A meticulous analyst who uses data to uncover patterns and inform decisions.",
    llm=llm,  # Connect to the LLM for analyzing data summaries
    allow_delegation=True
)

# Fact-Checker Agent
fact_checker = Agent(
    role="Fact-Checker",
    goal="Verify the accuracy of the information gathered for {topic}.",
    verbose=True,
    memory=True,
    backstory="An investigative mind who digs deep to validate information.",
    llm=llm,  # Connect to the LLM for verifying facts
    allow_delegation=True
)

# Editor Agent
editor = Agent(
    role="Editor",
    goal="Edit the content to ensure high quality, clarity, and readability.",
    verbose=True,
    memory=True,
    backstory="A detail-oriented editor who ensures the highest standards of language and clarity.",
    llm=llm,  # Connect to the LLM for improving writing
    allow_delegation=True
)






# import os
# from litellm import completion
# from crewai import Agent

# from crewai_tools import SerperDevTool

# # Define your tool (example using SerperDevTool)
# tool = SerperDevTool(api_key="0448c1de93ac8942ada6358b4ec4736ea7e7b4f7")

# # Define Huggingface API key
# huggingface_api_key = os.getenv("HUGGINGFACE_API_KEY")

# if huggingface_api_key is None:
#     raise ValueError("Huggingface API key not found. Please set the HUGGINGFACE_API_KEY environment variable.")

# # Define LLM function using Huggingface API
# def llm(prompt, temperature=0.5):
#     return completion(
#         model="huggingface/starcoder",
#         prompt=prompt,
#         temperature=temperature,
#         api_key=huggingface_api_key
#     )

# # Sample tool definition (replace with your actual tool or remove tools if unnecessary)
#   # Replace with an actual tool object or remove the `tools` argument if not needed.

# # Creating a Senior Researcher agent with memory and verbose mode
# news_researcher = Agent(
#     role="Senior Researcher",
#     goal='Uncover groundbreaking technologies in {topic}',
#     verbose=True,
#     memory=True,
#     backstory=(
#         "Driven by curiosity, you're at the forefront of innovation, eager to explore and share knowledge "
#         "that could change the world."
#     ),
#     tools=[tool],  # Ensure tool is properly defined
#     llm=llm,
#     allow_delegation=True
# )

# # Creating a Writer agent responsible for writing tech stories
# news_writer = Agent(
#     role='Writer',
#     goal='Narrate compelling tech stories about {topic}',
#     verbose=True,
#     memory=True,
#     backstory=(
#         "With a flair for simplifying complex topics, you craft engaging narratives that captivate and educate, "
#         "bringing new discoveries to light in an accessible manner."
#     ),
#     tools=[tool],  # Ensure tool is properly defined
#     llm=llm,
#     allow_delegation=False
# )



