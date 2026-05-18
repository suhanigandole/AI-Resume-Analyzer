# Gives AI suggestions
# Improves resume

import openai

def generate_feedback(resume_text, job_desc):

    prompt = f"""
    You are a resume expert AI.

    Analyze and give:
    1. Missing skills
    2. Improvements
    3. Better resume summary

    Resume:
    {resume_text}

    Job Description:
    {job_desc}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["choices"][0]["message"]["content"]