"""
    This file contains all the numeric preprocessing steps.
"""
import inflect
from gensim.parsing.preprocessing import split_alphanum, strip_numeric

INFLECT_ENGINE = inflect.engine() 

class NumericPreprocess:
    """
        This class contains all the methods which will handle numeric preprocessing.
    """
    @classmethod
    def convert_num_words(cls, text):
        """
            This method will numbers to text which help preprocessing much easier.
        """
        text = split_alphanum(text)
        temp_str = text.split()
        new_string = [INFLECT_ENGINE.number_to_words(word) if word.isdigit() else word for word in temp_str]
        temp_str = " ".join(new_string)
        return temp_str

    @classmethod
    def remove_numbers(cls, text):
        """
            This mwthod will remove the all numbers from text.
        """
        return strip_numeric(text)

    @classmethod
    def run_numeric(cls, text, numeric):
        """
            This method will do numeric preprocess.
        """
        if numeric == "convertnum2str":
            text = cls.convert_num_words(text)
        else:
            text = cls.remove_numbers(text)
        return text
