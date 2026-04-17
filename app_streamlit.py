import streamlit as st

# Page config
st.set_page_config(page_title="Fake News Detector", layout="centered")

# 🔥 CUSTOM CSS
st.markdown("""
<style>
body {
    background-color: #0f172a;
}
.main {
    background: linear-gradient(135deg, #0f172a, #1e293b);
}
h1 {
    text-align: center;
    color: #e2e8f0;
}
p {
    text-align: center;
    color: #94a3b8;
}
textarea {
    background-color: #1f2937 !important;
    color: white !important;
    border-radius: 10px !important;
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
    transform: scale(1.05);
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
st.markdown("<h1>📰 Fake News Detector</h1>", unsafe_allow_html=True)
st.markdown("<p>Analyze news and verify it instantly</p>", unsafe_allow_html=True)

# Input
text = st.text_area("")

# Button
if st.button("Analyze News"):
    if text.strip() == "":
        st.warning("⚠️ Enter some news!")
    else:
        with st.spinner("Analyzing..."):
            fake_keywords = ["alien", "secret", "miracle", "shocking", "viral", "rumor"]

        if any(word in text.lower() for word in fake_keywords):
            st.markdown(
                "<div class='result-box' style='background:#7f1d1d; color:#f87171;'>❌ Fake News</div>",
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                "<div class='result-box' style='background:#064e3b; color:#10b981;'>✅ Real News</div>",
                unsafe_allow_html=True
            )