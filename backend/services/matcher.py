# Compares resume vs job description
# Gives ATS score
import numpy as np

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def ats_score(resume_vec, job_vec):

    score = cosine_similarity(resume_vec, job_vec) * 100

    if score >= 80:
        level = "Strong Match"
    elif score >= 50:
        level = "Medium Match"
    else:
        level = "Weak Match"

    return round(score, 2), level