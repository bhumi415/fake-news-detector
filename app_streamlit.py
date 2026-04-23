import streamlit as st
import pickle
import re

st.set_page_config(page_title="Fake News Detector", layout="centered")

# 🔥 FULL CSS (FIXED + CLEAN)
st.markdown("""
<style>

/* 🔥 FORCE FULL PAGE BACKGROUND */
html, body, .stApp {
    background: linear-gradient(135deg, #e0f2fe, #bae6fd, #93c5fd) !important;
}

/* REMOVE ANY IMAGE / OVERLAY */
.stApp::before {
    display: none !important;
}

/* REMOVE DEFAULT WHITE BACKGROUND */
[data-testid="stAppViewContainer"] {
    background: transparent !important;
}

/* REMOVE BLOCK BACKGROUND */
section.main {
    background: transparent !important;
}

/* MAIN CONTAINER (GLASS) */
.main-box {
    width: 600px;
    margin: auto;
    margin-top: 60px;

    padding: 30px;
    border-radius: 18px;

    background: rgba(255, 255, 255, 0.4);
    backdrop-filter: blur(12px);

    border: 1px solid rgba(255,255,255,0.4);
    box-shadow: 0 8px 30px rgba(0,0,0,0.2);
}

/* TITLE */
.title {
    text-align: center;
    font-size: 32px;
    color: #111;
    font-weight: 600;
}

/* SUBTITLE */
.subtitle {
    text-align: center;
    color: #333;
    font-size: 14px;
}

/* TEXTAREA */
textarea {
    background: white !important;
    color: black !important;
    border-radius: 12px !important;
    border: 1px solid #ccc !important;
}

/* BUTTON */
.stButton>button {
    background: linear-gradient(135deg, #22c55e, #4ade80);
    color: black;
    border-radius: 12px;
    height: 3em;
    width: 100%;
    font-weight: 500;
}

</style>
""", unsafe_allow_html=True)

# LOAD MODEL
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# SESSION STATE
if "history" not in st.session_state:
    st.session_state.history = []

if "selected_text" not in st.session_state:
    st.session_state.selected_text = ""

# UI START
st.markdown("<div class='main-box'>", unsafe_allow_html=True)

st.markdown("<div class='title'>📰 Fake News Detector</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Analyze news using Machine Learning</div>", unsafe_allow_html=True)

text = st.text_area("Enter News Here", value=st.session_state.selected_text)

# SUSPICIOUS WORDS
suspicious_words_list = [
    "alien", "secret", "miracle", "shocking", "viral",
    "hidden", "conspiracy", "mind control", "ghost",
    "invisible", "rumor", "unbelievable"
]

def clean_text(text):
    return re.sub(r'[^a-zA-Z]', ' ', text).lower()

if st.button("Analyze News"):

    if text.strip() == "":
        st.warning("Enter some news")
        st.stop()

    if len(text.split()) < 6:
        st.warning("Please enter proper sentence")
        st.stop()

    cleaned = clean_text(text)
    vect = vectorizer.transform([cleaned])

    pred = model.predict(vect)[0]
    prob = model.predict_proba(vect)[0]

    st.session_state.history.append(text)

    if pred == 1:
        confidence = prob[1]
        st.success(f"✅ Real News ({round(confidence*100,2)}%)")
    else:
        confidence = prob[0]
        st.error(f"❌ Fake News ({round(confidence*100,2)}%)")

    found_words = [w for w in suspicious_words_list if w in cleaned]

    if found_words:
        st.warning(f"⚠️ Suspicious words: {', '.join(found_words)}")

st.markdown("</div>", unsafe_allow_html=True)

# HISTORY
st.subheader("📜 History")

for i, item in enumerate(reversed(st.session_state.history[-5:])):
    if st.button(f"Use: {item[:50]}...", key=i):
        st.session_state.selected_text = item
        st.rerun()