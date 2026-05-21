<<<<<<< HEAD
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")
=======
# Gives AI suggestions
# Improves resume

import openai
>>>>>>> 210088843dd3d6d075a62a811f9a497aa0aa3155

def generate_feedback(resume_text, job_desc):

    prompt = f"""
<<<<<<< HEAD
    Analyze this resume and suggest improvements.
=======
    You are a resume expert AI.

    Analyze and give:
    1. Missing skills
    2. Improvements
    3. Better resume summary
>>>>>>> 210088843dd3d6d075a62a811f9a497aa0aa3155

    Resume:
    {resume_text}

    Job Description:
    {job_desc}
    """

<<<<<<< HEAD
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
=======
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["choices"][0]["message"]["content"]
>>>>>>> 210088843dd3d6d075a62a811f9a497aa0aa3155
