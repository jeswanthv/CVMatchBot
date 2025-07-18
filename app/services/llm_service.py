import requests


def analyze_resume(resume_text: str, job_desc: str) -> str:
    prompt = f"""
    Compare this resume to the job description and give a match score out of 100.
    List any missing skills or experience. Write a short feedback paragraph.

    Job Description:
    {job_desc}

    Resume:
    {resume_text}
    """

    res = requests.post("http://host.docker.internal:11434/api/generate", json={
        "model": "llama3.2",
        "prompt": prompt,
        "stream": False
    })

    try:
        res_json = res.json()
        print("LLM response JSON:", res_json)  # 👈 log it to debug
        return res_json["response"]
    except Exception as e:
        print("Error parsing LLM response:", e)
        print("Raw text:", res.text)
        return "Something went wrong with LLM response."
