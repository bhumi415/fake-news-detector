from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import re
import os

app = Flask(__name__)
CORS(app)

# Load model
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# Fake keywords
fake_keywords = ["alien", "ghost", "invisible", "secret", "mystery", "rumor"]

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        text = data.get('text', '')

        if text.strip() == "":
            return jsonify({"error": "Empty input"}), 400

        # Clean text
        clean = re.sub(r'[^a-zA-Z]', ' ', text).lower()

        vect = vectorizer.transform([clean])

        # Prediction only (no probability)
        result = model.predict(vect)[0]

        prediction = "Real News" if result == 1 else "Fake News"

        # Keywords
        found_words = [word for word in fake_keywords if word in clean]

        return jsonify({
            "prediction": prediction,
            "keywords": found_words
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

    
