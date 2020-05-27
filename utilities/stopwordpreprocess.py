"""
    This file contains all the stopword removal steps.
"""
from gensim.parsing.preprocessing import STOPWORDS
from gensim.parsing.preprocessing import remove_stopwords

STOPWORDS = STOPWORDS.union(set(["no", "not", "never"]))

class StopwordRemoval:
    """
        This class contains all the methods which will handle numeric preprocessing.
    """
    @classmethod
    def consider_negative_stopwords(cls, text):
        """
            This method will remove the stopwords from text but not remove negative words.
        """
        temp_str = text.split()
        new_string = [word for word in temp_str if word not in STOPWORDS]
        return text

    @classmethod
    def donot_consider_negative_stopwords(cls, text):
        """
            THis method will remove all stopwords.
        """
        return remove_stopwords(text)

    @classmethod
    def run_stopwords(cls, text, stopwords):
        """
            This method will do stopword removal preprocess.
        """
        if stopwords == "removewords":
            text = cls.donot_consider_negative_stopwords(text)
        else:
            text = cls.consider_negative_stopwords(text)
        return text
