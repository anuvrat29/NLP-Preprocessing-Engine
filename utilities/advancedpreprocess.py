"""
    This file contains all the advanced preprocessing steps.
"""
from gensim.parsing.preprocessing import strip_short
from gensim.parsing.preprocessing import strip_punctuation
from gensim.parsing.preprocessing import strip_multiple_whitespaces

class AdvancedPreprocess:
    """
        This class contains all the methods which will handle numeric preprocessing.
    """
    @classmethod
    def remove_shortwords(cls, text):
        """
            This method will remove short words.
        """
        return strip_short(text, minsize=2)

    @classmethod
    def remove_puctuation(cls, text):
        """
            This method will remove puctuation from text.
        """
        return strip_punctuation(text)

    @classmethod
    def remove_multiple_spaces(cls, text):
        """
            This method will remove multiple whitespaces.
        """
        return strip_multiple_whitespaces(text)

    @classmethod
    def run_advanced(cls, text, punctuation, whitespace, shortword):
        """
            This method will remove punctuation, multiple whitespaces, short words.
        """
        if shortword:
            text = cls.remove_shortwords(text)
        if punctuation:
            text = cls.remove_puctuation(text)
        if whitespace:
            text = cls.remove_multiple_spaces(text)
        return text
