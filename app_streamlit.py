import streamlit as st

st.set_page_config(page_title="Fake News Detector", layout="centered")

# 🔥 PREMIUM CSS (FINAL FIXED)
st.markdown("""
<style>

.stApp {
    background: url('https://images.unsplash.com/photo-1504711434969-e33886168f5c') no-repeat center center fixed;
    background-size: cover;
}

/* CENTER ALIGN */
.block-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

/* GLASS CARD */
.main-box {
    width: 600px;
    background: rgba(15, 23, 42, 0.8);
    padding: 35px;
    border-radius: 18px;
    backdrop-filter: blur(14px);
    box-shadow: 0 10px 40px rgba(0,0,0,0.5);
}

/* TITLE */
.title {
    text-align: center;
    font-size: 32px;
    color: black;
    font-weight: 700;
}

/* SUBTITLE */
.subtitle {
    text-align: center;
    color: black;
    margin-bottom: 25px;
}

/* TEXT AREA */
textarea {
    background-color: rgba(0,0,0,0.85) !important;
    color: #ffffff !important;
    border-radius: 12px !important;
    border: 1px solid rgba(255,255,255,0.1);
}

/* BUTTON */
.stButton>button {
    background: linear-gradient(135deg, #22c55e, #16a34a);
    color: white;
    border-radius: 12px;
    height: 3em;
    width: 100%;
    font-weight: 600;
    border: none;
    margin-top: 10px;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.04);
    background: linear-gradient(135deg, #16a34a, #15803d);
}

/* RESULT */
.result {
    text-align: center;
    font-size: 20px;
    margin-top: 20px;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)

# 🔥 MAIN UI BOX
st.markdown("<div class='main-box'>", unsafe_allow_html=True)

st.markdown("<div class='title'>📰 Fake News Detector</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Analyze news and verify it instantly</div>", unsafe_allow_html=True)

text = st.text_area("")

if st.button("Analyze News"):
    if text.strip() == "":
        st.warning("⚠️ Enter some news!")
    else:
        fake_keywords = ["alien", "secret", "miracle", "shocking", "viral", "rumor"]

        if any(word in text.lower() for word in fake_keywords):
            st.markdown("<div class='result' style='color:#f87171;'>❌ Fake News</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='result' style='color:#22c55e;'>✅ Real News</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)