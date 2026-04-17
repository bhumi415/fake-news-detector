import streamlit as st

st.set_page_config(page_title="Fake News Detector", layout="wide")

# 🔥 CLEAN CSS (NO GLASS, PROPER CONTRAST)
st.markdown("""
<style>

/* Background */
.stApp {
    background: url('https://images.unsplash.com/photo-1504711434969-e33886168f5c') no-repeat center center fixed;
    background-size: cover;
}

/* Remove top padding */
.block-container {
    padding-top: 1rem;
}

/* Title */
.title {
    text-align: center;
    font-size: 36px;
    color: black;
    font-weight: 700;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #333;
    margin-bottom: 25px;
}

/* TEXT AREA WHITE */
textarea {
    background-color: white !important;
    color: black !important;
    border-radius: 12px !important;
    border: 2px solid #ddd !important;
    padding: 10px;
}

/* BUTTON CENTER */
.stButton {
    display: flex;
    justify-content: center;
}

.stButton>button {
    background: linear-gradient(135deg, #22c55e, #16a34a);
    color: white;
    border-radius: 12px;
    height: 3em;
    width: 200px;
    font-weight: 600;
    border: none;
    margin-top: 10px;
}

/* RESULT BIG */
.result {
    text-align: center;
    font-size: 26px;
    margin-top: 30px;
    font-weight: 700;
}

</style>
""", unsafe_allow_html=True)

# 🔥 TITLE
st.markdown("<div class='title'>📰 Fake News Detector</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Analyze news and verify it instantly</div>", unsafe_allow_html=True)

# INPUT
text = st.text_area("")

# BUTTON
if st.button("Analyze News"):
    if text.strip() == "":
        st.warning("Enter some news!")
    else:
        fake_keywords = ["alien", "secret", "miracle", "shocking", "viral"]

        if any(word in text.lower() for word in fake_keywords):
            st.markdown("<div class='result' style='color:red;'>❌ Fake News</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='result' style='color:green;'>✅ Real News</div>", unsafe_allow_html=True)