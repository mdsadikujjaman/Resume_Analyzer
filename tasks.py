from crewai import Task
from agents import resume_reviewer, ats_checker, career_coach


def create_tasks(resume_text):
    roast_task=Task(
        description=f"""
        Review this resume and roast it honestly.
        Highlight weak bullet points and formatting problems.
        Resume: {resume_text}
        """,
        expected_output="A detailed critique of the resume, including specific feedback on weak bullet points and formatting issues.",
        agent=resume_reviewer
    )

    ats_task=Task(
        description=f"""
        Analyze this resume for ATS compatibility.
        Identify any issues with formatting, keyword usage, or structure.
        - ATS score out of 100
        Resume: {resume_text}
        """,
        expected_output="A detailed analysis of the resume's ATS compatibility, including specific recommendations for improvement and good fit for the role.",
        agent=ats_checker
    )

    skill_task=Task(
        description=f"""
        Provide personalized career advice based on this resume.
        Consider the individual's background, skills, and goals.
        Resume: {resume_text}
        """,
        expected_output="List of missing skills and recommended improvements for resume.",
        agent=career_coach
    )

    return [roast_task, ats_task, skill_task]