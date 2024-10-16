
from crewai import Task
from tools import tool
from agents import news_researcher,news_writer, data_analyst, fact_checker, editor

# Research task
research_task = Task(
  description=(
    "Identify the next big trend in {topic}."
    "Focus on identifying pros and cons and the overall narrative."
    "Your final report should clearly articulate the key points,"
    "its market opportunities, and potential risks."
  ),
  expected_output='A comprehensive 3 paragraphs long report on the latest AI trends.',
  tools=[tool],
  agent=news_researcher,
)

# Writing task with language model configuration
write_task = Task(
  description=(
    "Compose an insightful article on {topic}."
    "Focus on the latest trends and how it's impacting the industry."
    "This article should be easy to understand, engaging, and positive."
  ),
  expected_output='A 4 paragraph article on {topic} advancements formatted as markdown.',
  tools=[tool],
  agent=news_writer,
  async_execution=False,
  output_file='new-blog-post5.md'  # Example of output customization
)

data_analysis_task = Task(
    description=(
        "Analyze datasets related to {topic} to identify key trends, patterns, and insights. "
        "Focus on generating visualizations and data summaries that support the narrative of the latest developments. "
        "Ensure that the analysis is clear, accurate, and backed by data."
    ),
    expected_output='A detailed report with visualizations, charts, and key data insights.',
    tools=[tool],  # Include the specific data analysis tool needed
    agent=data_analyst,  # Use the Data Analyst agent
    async_execution=False,
    output_file='data-analysis-report5.pdf'  # Save the output to a PDF file
)

fact_check_task = Task(
    description=(
        "Verify the information gathered about {topic} to ensure accuracy. "
        "Check for any factual errors or unsupported claims and provide corrections if necessary."
    ),
    expected_output='A summary of verified information with references or corrections.',
    tools=[tool],  # Include the specific tool needed
    agent=fact_checker,  # Use the Fact-Checker agent
    async_execution=False
)

# Editing Task with the Editor Agent
edit_task = Task(
    description=(
        "Refine and edit the draft article on {topic}. "
        "Ensure the content is clear, well-structured, and free of grammatical errors. "
        "Improve readability and flow."
    ),
    expected_output='An edited version of the article, polished and ready for publication.',
    tools=[tool],  # Include the specific tool needed
    agent=editor,  # Use the Editor agent
    async_execution=False,
    output_file='final-article5.md'  # Save edited content to a file
)

