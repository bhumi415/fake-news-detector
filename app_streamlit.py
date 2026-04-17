import streamlit as st
import pickle
import re

# Load model
model = pickle.load(open('backend/model.pkl', 'rb'))
vectorizer = pickle.load(open('backend/vectorizer.pkl', 'rb'))

st.set_page_config(page_title="Fake News Detector")

st.title("📰 Fake News Detector")
st.write("Analyze news and verify it instantly")

text = st.text_area("Enter News")

if st.button("Analyze News"):
    if text.strip() == "":
        st.warning("Enter some news!")
    else:
        clean = re.sub(r'[^a-zA-Z]', ' ', text).lower()
        vect = vectorizer.transform([clean])
        result = model.predict(vect)[0]

        if result == 1:
            st.success("✅ Real News")
        else:
            st.error("❌ Fake News")