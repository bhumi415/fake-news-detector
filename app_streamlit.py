import streamlit as st
import pickle
import re
import os

# Page config
st.set_page_config(page_title="Fake News Detector", layout="centered")

# Title
st.title("📰 Fake News Detector")
st.write("Analyze news and verify it instantly")

# 🔥 File paths (SAFE WAY)
model_path = os.path.join('backend', 'model.pkl')
vectorizer_path = os.path.join('backend', 'vectorizer.pkl')

# 🔥 Check if files exist
if not os.path.exists(model_path):
    st.error("❌ Model file not found! Check backend/model.pkl")
    st.stop()

if not os.path.exists(vectorizer_path):
    st.error("❌ Vectorizer file not found! Check backend/vectorizer.pkl")
    st.stop()

# Load model
model = pickle.load(open(model_path, 'rb'))
vectorizer = pickle.load(open(vectorizer_path, 'rb'))

# Input box
text = st.text_area("Enter News")

# Button
if st.button("Analyze News"):
    if text.strip() == "":
        st.warning("⚠️ Please enter some news!")
    else:
        with st.spinner("Analyzing..."):
            # Clean text
            clean = re.sub(r'[^a-zA-Z]', ' ', text).lower()

            # Transform
            vect = vectorizer.transform([clean])

            # Predict
            result = model.predict(vect)[0]

        # Result
        if result == 1:
            st.success("✅ Real News")
        else:
            st.error("❌ Fake News")