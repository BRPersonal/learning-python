from abc import ABC, abstractmethod
from resume_score import ResumeScore

class ResumeMatchingEngine(ABC):
    """
    An abstract base class that serves as an interface for resume matching engines.
    """
    @abstractmethod
    def compute_score(self, jd_text: str, resume_text: str) -> ResumeScore:
        """
        Abstract method to compute the matching score between a job description and a resume.
        Must be implemented by subclasses.
        """
        pass
