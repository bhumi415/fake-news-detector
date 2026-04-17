import streamlit as st

st.set_page_config(page_title="Fake News Detector", layout="wide")

# 🔥 REMOVE STREAMLIT DEFAULT PADDING
st.markdown("""
<style>

/* Remove top spacing */
.block-container {
    padding-top: 1rem !important;
}

/* Remove weird header gap */
header {visibility: hidden;}
footer {visibility: hidden;}

/* Background */
.stApp {
    background: url('https://images.unsplash.com/photo-1504711434969-e33886168f5c') no-repeat center center fixed;
    background-size: cover;
}

/* CENTER CONTAINER */
.container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 90vh;
}

/* GLASS CARD */
.main-box {
    width: 600px;
    background: rgba(15, 23, 42, 0.85);
    padding: 35px;
    border-radius: 18px;
    backdrop-filter: blur(14px);
    box-shadow: 0 10px 40px rgba(0,0,0,0.5);
}

/* TITLE */
.title {
    text-align: center;
    font-size: 32px;
    color: white;
    font-weight: 700;
}

/* SUBTITLE */
.subtitle {
    text-align: center;
    color: #cbd5f5;
    margin-bottom: 25px;
}

/* TEXT AREA */
textarea {
    background-color: rgba(0,0,0,0.9) !important;
    color: white !important;
    border-radius: 12px !important;
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
}

/* RESULT */
.result {
    text-align: center;
    font-size: 20px;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)

# CENTER WRAPPER
st.markdown("<div class='container'>", unsafe_allow_html=True)

st.markdown("<div class='main-box'>", unsafe_allow_html=True)

st.markdown("<div class='title'>📰 Fake News Detector</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Analyze news and verify it instantly</div>", unsafe_allow_html=True)

text = st.text_area("")

if st.button("Analyze News"):
    if text.strip() == "":
        st.warning("Enter some news!")
    else:
        fake_keywords = ["alien", "secret", "miracle", "shocking", "viral"]

        if any(word in text.lower() for word in fake_keywords):
            st.markdown("<div class='result' style='color:red;'>❌ Fake News</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='result' style='color:#22c55e;'>✅ Real News</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)