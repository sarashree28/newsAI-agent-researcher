from flask import Flask, render_template, request, redirect, url_for
from crewai import Crew, Process
from agents import news_researcher, news_writer, data_analyst, fact_checker, editor
from tasks import research_task, write_task, data_analysis_task, fact_check_task, edit_task

app = Flask(__name__)

# Initialize Crew with agents and tasks
crew = Crew(
    agents=[news_researcher, news_writer, data_analyst, fact_checker, editor],
    tasks=[research_task, write_task, data_analysis_task, fact_check_task, edit_task],
    process=Process.sequential,
)

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Route to run tasks and display result
@app.route('/run_tasks', methods=['POST'])
def run_tasks():
    topic = request.form.get('topic')
    
    # Execute the tasks
    result = crew.kickoff(inputs={'topic': topic})
    
    # Render result page
    return render_template('result.html', result=result, topic=topic)

if __name__ == "__main__":
    app.run(debug=True)
