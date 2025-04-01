from resume_matching_engine import ResumeMatchingEngine

from resume_matching_engine_chat_gpt import ChatGptEngine
from resume_matching_engine_pdf_miner import PdfMinerEngine

chatGptEngine = ChatGptEngine()
pdfMinerEngine = PdfMinerEngine()

class ResumeMatchingEngineFactory:
    """
    A factory class that creates ResumeMatchingEngine objects based on the given engine type.
    """
    @staticmethod
    def create_engine(engine_type: str) -> ResumeMatchingEngine:
        """
        Creates and returns a ResumeMatchingEngine object based on the given engine type.
        """
        if engine_type == "chatGPT":
            return chatGptEngine
        elif engine_type == "pdfMiner":
            return pdfMinerEngine
        else:
            raise ValueError(f"Invalid engine type {engine_type}")
