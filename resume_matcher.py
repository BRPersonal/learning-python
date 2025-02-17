from resume_matching_engine_factory import ResumeMatchingEngineFactory

if __name__ == "__main__":
    chatgpt_engine = ResumeMatchingEngineFactory.create_engine("chatGPT")
    pdfminer_engine = ResumeMatchingEngineFactory.create_engine("pdfMiner")

    jd_text = "Software Engineer with 5+ years of experience"
    resume_text = "Experienced software engineer specializing in Python and Java"

    chatgpt_score = chatgpt_engine.compute_score(jd_text, resume_text)
    pdfminer_score = pdfminer_engine.compute_score(jd_text, resume_text)

    print(f"ChatGPT Score: {chatgpt_score}")
    print(f"PdfMiner Score: {pdfminer_score}")
