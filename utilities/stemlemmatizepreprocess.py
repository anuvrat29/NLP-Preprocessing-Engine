"""
    This will stem and lemmatize the text.
"""
from gensim.utils import lemmatize
from gensim.parsing.preprocessing import stem_text

import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, SnowballStemmer

porterstemmer = PorterStemmer()
snowballstemmer = SnowballStemmer('english')

class StemLemmatize:
    """
        This class contains all methods of stemming and lemmatization.
    """
    @classmethod
    def porterstemming(cls, text):
        """
            This method will perform porter stemming.
        """
        words = word_tokenize(text)
        return " ".join([porterstemmer.stem(word) for word in words])

    @classmethod
    def snowballstemming(cls, text):
        """
            This method will perform porter stemming.
        """
        words = word_tokenize(text)
        return " ".join([snowballstemmer.stem(word) for word in words])

    @classmethod
    def lemmatization(cls, text):
        """
            This method will do lemmatization of text.
        """
        return " ".join([word.decode('utf-8').split('/')[0] for word in lemmatize(text)])

    @classmethod
    def run_stemlemma(cls, text, stemming, lemmatization):
        """
            This method will stem, lemmatize of text.
        """
        if stemming == "porter":
            text = cls.porterstemming(text)
        else:
            text = cls.snowballstemming(text)

        if lemmatization:
            text = cls.lemmatization(text)
        return text
