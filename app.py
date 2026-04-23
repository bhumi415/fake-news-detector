from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import re

app = Flask(__name__)
CORS(app)

# Load ML model
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

@app.route('/')
def home():
    return jsonify({"message": "Fake News Detection API Running"})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        if not data or "text" not in data:
            return jsonify({"error": "Invalid input"}), 400

        text = data["text"]

        # Validation
        if text.strip() == "":
            return jsonify({"error": "Empty input"}), 400

        if len(text.split()) < 5:
            return jsonify({"error": "Enter proper news sentence"}), 400

        # Clean text
        clean = re.sub(r'[^a-zA-Z]', ' ', text).lower()

        # Vectorize
        vect = vectorizer.transform([clean])

        # Prediction + Probability
        pred = model.predict(vect)[0]
        prob = model.predict_proba(vect)[0]

        if pred == 1:
            result = "Real News"
            confidence = prob[1]
        else:
            result = "Fake News"
            confidence = prob[0]

        return jsonify({
            "prediction": result,
            "confidence": round(confidence * 100, 2)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)