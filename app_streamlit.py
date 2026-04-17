import streamlit as st

st.set_page_config(page_title="Fake News Detector", layout="centered")

# 🔥 ORIGINAL STYLE CSS (GLASS EFFECT)
st.markdown("""
<style>

.stApp {
    background: url('https://images.unsplash.com/photo-1504711434969-e33886168f5c') no-repeat center center fixed;
    background-size: cover;
}

.main-box {
    background: rgba(0, 0, 0, 0.6);
    padding: 30px;
    border-radius: 15px;
    backdrop-filter: blur(10px);
    margin-top: 50px;
}

.title {
    text-align: center;
    font-size: 32px;
    color: white;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: #ccc;
    margin-bottom: 20px;
}

textarea {
    background-color: #111 !important;
    color: white !important;
    border-radius: 10px !important;
}

.stButton>button {
    background: #22c55e;
    color: black;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-weight: 600;
}

.result {
    text-align: center;
    font-size: 20px;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)

# BOX START
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