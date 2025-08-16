from utils import run_llama

def resume_screening(resumes):
    prompt = f"Analyze and summarize the best candidates from these resumes:\n{resumes}"
    return run_llama(prompt)

if __name__ == "__main__":
    resumes = open("resumes.txt").read()
    print(resume_screening(resumes))
