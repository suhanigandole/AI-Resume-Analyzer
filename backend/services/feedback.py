from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

def generate_feedback(resume_text, job_desc):

    prompt = f"""
    Analyze this resume and suggest improvements.

    Resume:
    {resume_text}

    Job Description:
    {job_desc}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content