from flask import Flask, request, render_template

from utilities.basicpreprocess import BasicPreprocess
from utilities.numericpreprocess import NumericPreprocess
from utilities.stopwordpreprocess import StopwordRemoval
from utilities.advancedpreprocess import AdvancedPreprocess
from utilities.stemlemmatizepreprocess import StemLemmatize

APP = Flask(__name__, template_folder="frontend")

class NLPEngine:

    @APP.route("/", methods=["GET"])
    def index_page():
        """
            This will return index html page.
        """
        return render_template("index.html")

    @APP.route("/anuvrat/nlp/nlpengine", methods=["POST"])
    def nlp_engine():
        """
            This is controller code which will mediate between view and business logic.
        """
        lowercase = True
        contraction = bool(request.form.get("contraction", False))
        numeric = request.form.get("numeric", False)
        stopwords = request.form.get("stopwords", False)
        punctuation = bool(request.form.get("punctuation", False))
        whitespace = bool(request.form.get("whitespace", False))
        shortword = bool(request.form.get("shortword", False))
        stemming = request.form.get("stemming", False)
        lemmatization = bool(request.form.get("lemmatization", False))
        text = request.form.get("single-string", "")
        text = text if text is not "" else request.form.get("multiple-string", "")

        new_string = []
        for _, value in enumerate(text.splitlines()):
            text = BasicPreprocess().run_basic(value, lowercase, contraction)
            text = NumericPreprocess().run_numeric(text, numeric)
            text = StopwordRemoval().run_stopwords(text, stopwords)
            text = AdvancedPreprocess().run_advanced(text, punctuation, whitespace, shortword)
            text = StemLemmatize().run_stemlemma(text, stemming, lemmatization)
            new_string.append(text)

        data = "\r\n".join(new_string)
        rows = 10 if len(new_string) > 10 else len(new_string)
        return render_template("view.html", data=data, rows=rows)

if __name__ == "__main__":
    APP.run(debug=True, port=65000)
