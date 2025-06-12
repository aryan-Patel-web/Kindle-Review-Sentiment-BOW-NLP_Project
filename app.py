from flask import Flask, render_template, request
import pickle

# Load model and vectorizer
with open('bow_vectorizer.pkl', 'rb') as f:
    bow = pickle.load(f)
with open('nb_model_bow.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        review = request.form['review']
        review = review.lower().strip()
        review_bow = bow.transform([review]).toarray()
        pred = model.predict(review_bow)[0]
        prediction = 'Positive' if pred == 1 else 'Negative'
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)