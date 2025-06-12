# Kindle Review Sentiment Analysis using Bag of Words (BOW)

A web-based sentiment analysis system for Kindle book reviews using Bag of Words (BOW) and Naive Bayes.  
It preprocesses, cleans, and lemmatizes review text before classifying as positive or negative.  
Deployable as a Flask app for real-time sentiment prediction.

---

## What is Bag of Words (BOW) in NLP?

Bag of Words is a popular text representation technique in Natural Language Processing (NLP) that converts text into fixed-length vectors based on word frequency, ignoring grammar and word order. Each unique word in the corpus becomes a feature, and the value is the count of that word in the document.

---

## How BOW is Used in This Project

- **Text Cleaning:** Lowercasing, removing special characters, stopwords, URLs, and HTML tags.
- **Lemmatization:** Reducing words to their base form.
- **Vectorization:** Using `CountVectorizer` to convert cleaned reviews into BOW vectors.
- **Classification:** Training a Naive Bayes classifier on these vectors to predict sentiment.

---

## Project Workflow

1. **Data Loading:** Read Kindle reviews from CSV.
2. **Preprocessing:** Clean and lemmatize review text.
3. **Train-Test Split:** Split data for training and evaluation.
4. **Vectorization:** Transform text using BOW.
5. **Model Training:** Train Naive Bayes classifier.
6. **Evaluation:** Assess accuracy and performance.
7. **Deployment:** Save model and vectorizer with pickle, deploy with Flask web app.

---

## Technologies Used

- Python (Pandas, scikit-learn, NLTK)
- Flask (for web deployment)
- HTML/CSS (for frontend)
- Pickle (for model serialization)

---

## Project Structure

```
├── all_kindle_review.csv
├── Kindle_Review_Sentiment_Analysis_BOW.ipynb
├── app.py
├── bow_vectorizer.pkl
├── nb_model_bow.pkl
├── requirements.txt
└── templates/
    └── index.html
```

---

## Requirements

- flask
- pandas
- scikit-learn
- nltk

Install with:
```
pip install -r requirements.txt
```

---

## Usage Summary

1. Train the model in the notebook and save the vectorizer/model.
2. Run `app.py` to start the Flask web server.
3. Enter a Kindle review in the web interface to get sentiment prediction.

---

## Example Test Inputs

**Example 1 (Positive):**
```
This book was fantastic! The story was engaging and I couldn't put it down.
```

**Example 2 (Negative):**
```
I did not enjoy this book. The plot was boring and the characters were flat.
```
