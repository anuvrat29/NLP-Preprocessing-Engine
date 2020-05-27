# NLP-Preprocessing-Engine
This is a NLP Engine and help you to get text preprocessed data.


### Importance
1.  This is NLP Engine which will make simple the entire pipeline.
2.  This project contins all the text preprocessing steps.

### Text Preprocessing important steps given below
-	Lowercase: This is very basic and important step in preprocessing to maintain uniformity in text either you can use lowercase or uppercase depending upon your choice.
-	Contraction: Words are combined in when you write in English language like don't => do not, I'll => I will so resolve all these Contraction words.
-	Numeric Preprocess: Either you can change numbers to string or remove the numbers. Most of the time number is not helpful in sentiment analysis, text matching but if you want then you can select.
-	Stopword Removal: In some cases, "no", "not", "never" are important in the the text cause used in sentiment analysis.
-	Advanced Preprocess: Punctuation, whitespaces, short words like I, A, etc. do not contribute in sentence, so remove those.
-	Stemming and Lemmatization: You can go for stemming and lemmatization or either of this. For both it will be first stemming and then lemmatization. In stemming, porter and snowball stemming you can choose either of this.

### •   Step 1: Install All the dependencies.

1.  All the dependencies mentioned in requirements.txt
2.  Install using pip install -r requirements.txt

### •   Step 2: Run the application.

1.  Run engine.py which will run on http://127.0.0.1:65000.
2.  Visit this URL in web browser.

3.  If you want to run on specific IP then change "host" in engine.py
4.  And visit http://IP-ADDRESS:65000.
