from resume_matching_engine import ResumeMatchingEngine
from resume_score import ResumeScore

class PdfMinerEngine(ResumeMatchingEngine):
    """
        A concrete implementation of ResumeMatchingEngine that uses a PdfMiner.
    """

    def compute_score(self, jd_text: str, resume_text: str) -> ResumeScore:
        """
        Computes the matching score using PdfMiner.
        """
        # implementation specific to PdfMiner
        # Do data cleansing
        # use model to get the score
        print("computing score using PdfMiner engine")
        return ResumeScore(experience_score=0.8, skill_score=0.7, similarity_score=0.9)
