import streamlit as st
import pickle
import re

# LOAD MODEL SAFELY
try:
    model = pickle.load(open("model.pkl", "rb"))
    vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
except:
    st.error("Model not loaded. Please check files.")
    st.stop()

st.title("📰 Fake News Detector")
st.write("Machine Learning Based Detection")

text = st.text_area("Enter News Here")

def clean_text(text):
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    return text.lower()

if st.button("Analyze News"):
    if text.strip() == "":
        st.warning("Enter some news")
    else:
        clean = clean_text(text)
        vect = vectorizer.transform([clean])
        result = model.predict(vect)[0]

        if result == 1:
            st.success("✅ Real News")
        else:
            st.error("❌ Fake News")