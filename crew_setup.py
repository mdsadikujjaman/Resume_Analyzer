from crewai import Crew
from agents import resume_reviewer, ats_checker, career_coach
from tasks import create_tasks

def run_resume_agents(resume_text):
    roast_task, ats_task, skill_task = create_tasks(resume_text)
    crew = Crew(
        agents=[resume_reviewer, ats_checker, career_coach],
        tasks=[roast_task, ats_task, skill_task],
        verbose=True
    )

    result=crew.kickoff()

    return result