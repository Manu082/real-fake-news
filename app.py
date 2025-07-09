import streamlit as st
import pickle
import os
import warnings

warnings.filterwarnings("ignore", category=RuntimeWarning)

# ✅ Page Config
st.set_page_config(
    page_title="📰 Fake News Detection",
    page_icon="📰",
    layout="wide"
)

# ✅ Sidebar
st.sidebar.title("📰 Fake News Detector")
st.sidebar.markdown("""
Detect whether a news article is **Real** or **Fake** using Machine Learning and NLP.  
Built with 🧡 by **Manas Didwania**.
""")

st.sidebar.markdown("---")
st.sidebar.info("✅ Supports English text\n✅ Trained on fake/real news dataset")

# ✅ Main Title
st.title("📰 Fake News Detection using Machine Learning")
st.markdown(
    """
    This web app uses **Natural Language Processing (NLP)** and a trained **Machine Learning model** to predict whether a news article is **Real** or **Fake**.
    """
)
st.divider()

# ✅ Load Model and Vectorizer
@st.cache_resource(show_spinner=True)
def load_model_and_vectorizer():
    try:
        if not os.path.exists("fake_news_model.pkl") or not os.path.exists("tfidf_vectorizer.pkl"):
            return None, None

        with open("fake_news_model.pkl", "rb") as f_model:
            model = pickle.load(f_model)

        with open("tfidf_vectorizer.pkl", "rb") as f_vectorizer:
            vectorizer = pickle.load(f_vectorizer)

        return model, vectorizer
    except Exception as e:
        st.error(f"❌ Failed to load model/vectorizer: {e}")
        return None, None

model, vectorizer = load_model_and_vectorizer()

if model is None or vectorizer is None:
    st.warning("""
    ⚠️ Model and vectorizer not found or invalid.  
    Please ensure `fake_news_model.pkl` and `tfidf_vectorizer.pkl` are in the same folder as `app.py`.
    """)
    st.stop()

# ✅ User Input
st.subheader("📜 Enter News Text")
user_input = st.text_area(
    "Paste your news article or headline below:",
    height=200,
    placeholder="Example: Aliens spotted near the White House!"
)

# ✅ Optional NLP Analysis
if user_input.strip():
    with st.expander("📊 Show Input Text Analysis"):
        st.write(f"✅ **Character Count:** {len(user_input)}")
        st.write(f"✅ **Word Count:** {len(user_input.split())}")
        st.code(user_input, language='markdown')

# ✅ Predict Button
if st.button("🔍 Predict"):
    if not user_input.strip():
        st.warning("⚠️ Please enter some text to analyze.")
    else:
        with st.spinner("Analyzing with trained model..."):
            input_vector = vectorizer.transform([user_input])
            prediction = model.predict(input_vector)

            st.markdown("### 🧠 **Prediction Result**")
            if prediction[0] == 1:
                st.success("🟢 This news is predicted to be **REAL**.")
            else:
                st.error("🔴 This news is predicted to be **FAKE**.")

st.markdown("---")
st.caption("✅ Built with Streamlit, scikit-learn & NLP | © 2025 MANAS DIDWANIA")
