import streamlit as st

st.set_page_config(page_title="Fake News Detector")

st.title("📰 Fake News Detector")
st.write("Analyze news and verify it instantly")

text = st.text_area("Enter News")

if st.button("Analyze News"):
    if text.strip() == "":
        st.warning("⚠️ Enter some news!")
    else:
        # 🔥 Simple rule-based logic (demo)
        fake_keywords = ["alien", "secret", "miracle", "shocking", "viral", "rumor"]

        if any(word in text.lower() for word in fake_keywords):
            st.error("❌ Fake News")
        else:
            st.success("✅ Real News")