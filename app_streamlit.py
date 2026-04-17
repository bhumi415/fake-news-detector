import streamlit as st
import pickle
import re

# Load model
model = pickle.load(open('backend/model.pkl', 'rb'))
vectorizer = pickle.load(open('backend/vectorizer.pkl', 'rb'))

# Page config
st.set_page_config(page_title="Fake News Detector", layout="centered")

# 🔥 CUSTOM CSS (Premium UI)
st.markdown("""
<style>
body {
    background-color: #0f172a;
}
.main {
    background: linear-gradient(135deg, #0f172a, #1e293b);
}
textarea {
    background-color: #1f2937 !important;
    color: white !important;
}
.stButton>button {
    background: linear-gradient(135deg, #22c55e, #4ade80);
    color: black;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-weight: 600;
    transition: 0.3s;
}
.stButton>button:hover {
    transform: scale(1.03);
}
.result-box {
    padding: 15px;
    border-radius: 10px;
    text-align: center;
    font-size: 18px;
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align:center;'>📰 Fake News Detector</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:gray;'>Analyze news instantly</p>", unsafe_allow_html=True)

# Input
text = st.text_area("")

# 🔥 Loading animation
if st.button("Analyze News"):
    if text.strip() == "":
        st.warning("⚠️ Enter some news!")
    else:
        with st.spinner("Analyzing..."):
            clean = re.sub(r'[^a-zA-Z]', ' ', text).lower()
            vect = vectorizer.transform([clean])
            result = model.predict(vect)[0]

        # Result UI
        if result == 1:
            st.markdown(
                "<div class='result-box' style='background:#064e3b; color:#10b981;'>✅ Real News</div>",
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                "<div class='result-box' style='background:#7f1d1d; color:#f87171;'>❌ Fake News</div>",
                unsafe_allow_html=True
            )