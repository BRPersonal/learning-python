import json

class ResumeScore:
    def __init__(self, experience_score: float, skill_score: float, similarity_score: float):

        #validate boundaries. scores should be between 0 and 1
        if (experience_score < 0.0 or experience_score > 1.0):
            raise ValueError("experience score should be between 0 and 1")
        if (skill_score < 0.0 or skill_score > 1.0):
            raise ValueError("skill score should be between 0 and 1")
        if (similarity_score < 0.0 or similarity_score > 1.0):
            raise ValueError("similarity score should be between 0 and 1")

        self.experience_score = round(experience_score, 2)
        self.skill_score = round(skill_score, 2)
        self.similarity_score = round(similarity_score, 2)

        self.final_score = round(((experience_score * 0.5) + (skill_score * 0.4) + (similarity_score * 0.1)),2)

    def __str__(self):
        """
            Return the JSON representation of the object when printed.
        """
        return json.dumps(self.to_dictionary())

    def to_dictionary(self) -> dict:
        """
        Convert the object to a dictionary
        """
        result = {
            "experience_score": self.experience_score * 100,
            "skill_score": self.skill_score * 100,
            "similarity_score": self.similarity_score * 100,
            "final_score": self.final_score * 100
        }

        return result

