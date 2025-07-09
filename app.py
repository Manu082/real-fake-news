import streamlit as st
import pickle
import os
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)


# ✅ Page Configuration
st.set_page_config(
    page_title="📰 Fake News Detection",
    page_icon="📰",
    layout="centered",
    initial_sidebar_state="auto"
)

# ✅ App Header
st.title("📰 Fake News Detection Using Machine Learning and Python")

st.markdown(
    """
    This simple web app uses **Natural Language Processing (NLP)** and a trained **Machine Learning model**
    to predict whether a news article is **Real** or **Fake**.
    """
)

st.markdown("---")

# ✅ Load model and vectorizer with safe error handling
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


# ✅ Load files
model, vectorizer = load_model_and_vectorizer()

if model is None or vectorizer is None:
    st.warning("""
    ⚠️ Model and vectorizer not found or invalid.  
    Please make sure `fake_news_model.pkl` and `tfidf_vectorizer.pkl` are in the same folder as `app.py`.
    """)
    st.stop()

# ✅ User Input
st.subheader("Enter News Text")
user_input = st.text_area(
    "Paste your news article or headline below:",
    height=200,
    placeholder="Example: Aliens spotted near the White House!"
)

# ✅ Prediction Button
if st.button("🔍 Predict"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some text.")
    else:
        with st.spinner("Analyzing..."):
            input_vector = vectorizer.transform([user_input])
            prediction = model.predict(input_vector)

            st.markdown("### 🧠 Prediction Result:")
            if prediction[0] == 1:
                st.success("🟢 The news is **REAL**.")
            else:
                st.error("🔴 The news is **FAKE**.")

# ✅ Footer
st.markdown("---")
st.caption("✅ Built using Streamlit, scikit-learn & NLP | © 2025 MANAS DIDWANIA")
