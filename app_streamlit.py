import streamlit as st
import pickle
import re

# Load model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

st.title("📰 Fake News Detector")
st.write("Machine Learning based detection")

text = st.text_area("Enter News")

def clean(text):
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    return text.lower()

if st.button("Analyze News"):
    if text.strip() == "":
        st.warning("Enter some text")
    else:
        clean_text = clean(text)
        vect = vectorizer.transform([clean_text])
        result = model.predict(vect)[0]

        if result == 1:
            st.success("✅ Real News")
        else:
            st.error("❌ Fake News")