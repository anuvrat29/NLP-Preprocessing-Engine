"""
    This file contains all the basic preprocessing steps.
"""
from utilities.config import CONTRACTION

class BasicPreprocess:
    """
        This class contains all the methods which will handle basic preprocessing.
    """
    @classmethod
    def convert_to_lowercase(cls, text):
        """
            Change to lowercase which help preprocessing much easier.
        """
        return text.lower()

    @classmethod
    def resolve_contraction(cls, text):
        """
            Resolve the contraction in this meethod.
        """
        for key, value in CONTRACTION.items():
            text.replace(key.lower(), value.lower())
        return text

    @classmethod
    def run_basic(cls, text, lowercase, contraction):
        """
            This method will do basic preprocess.
        """
        if lowercase:
            text = cls.convert_to_lowercase(text)
        if contraction:
            text = cls.resolve_contraction(text)
        return text
