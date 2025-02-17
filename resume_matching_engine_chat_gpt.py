from resume_matching_engine import ResumeMatchingEngine
from resume_score import ResumeScore

class ChatGptEngine(ResumeMatchingEngine):
    """
        A concrete implementation of ResumeMatchingEngine that uses a ChatGPT model.
    """
    def compute_score(self, jd_text: str, resume_text: str) -> ResumeScore:
        """
        Computes the matching score using a ChatGPT model.
        """
        # implementation specific to ChatGPT
        #Do data cleansing
        #use model to get the score
        print("computing score using chat gpt engine")
        return ResumeScore(experience_score=1,skill_score=1,similarity_score=1)

