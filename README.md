# 📰 Fake News Detection using Machine Learning

A Streamlit web app that predicts whether a news article is Real or Fake using Natural Language Processing (NLP) and Machine Learning .

# 🚀 **Overview**

- **Model:** Logistic Regression
- **Vectorization:** TF-IDF
- **Accuracy Achieved:** ~98%
- **Platform:** Streamlit Cloud

# 🌐 **Live Demo**

**URL**: real-fake.streamlit.app

# 📦 **Dataset**

**Source: Fake and Real News Dataset (Kaggle)**

**Files Included:**

- **Fake.csv** — Fake news articles

- **True.csv** — Real news articles

# **🧠 How It Works**

- **Step 1**: Combine Fake.csv and True.csv with labels (0 = Fake, 1 = Real)

- **Step 2**: Preprocess text using TF-IDF Vectorizer

- **Step 3**: Train Logistic Regression classifier

- **Step 4**: Evaluate model accuracy (~98%)

- **Step 5**: Save the model and vectorizer as .pkl files

- **Step 6**: Use Streamlit app to predict if news is REAL or FAKE

# **💻 Project Structure**

Fake-Real-News/
├── app.py                    ← Streamlit app
├── Fake & Real News.ipynb    ← Jupyter notebook for training
├── fake_news_model.pkl       ← Saved ML model
├── tfidf_vectorizer.pkl      ← Saved TF-IDF vectorizer
├── Fake.csv                  ← Fake news dataset
├── True.csv                  ← Real news dataset
├── requirements.txt          ← Dependencies
└── README.md                 ← Project documentation

# **⚙️ Requirements**

**Python**: 3.7+

**Dependencies**:

- **streamlit**

- **scikit-learn**

- **pandas**

- **numpy**

- **seaborn**

- **matplotlib**

# **✅ Install all dependencies**

pip install -r requirements.txt

# **🛠️ How to Run Locally**

- **Step 1**: Clone the repository
  
   git clone https://github.com/Manu082/Fake-Real-News.git
  
   cd Fake-Real-News
  
- **Step 2** :Install dependencies
  
   pip install -r requirements.txt
  
- **Step 3** :Start the Streamlit app
  
   streamlit run app.py

# **📜 License**

 - **License**: MIT License

# **👤 Author**

   **MANAS DIDWANIA**

**[didwania082@gmail.com]**


# **✅ Happy Coding! 🚀**
  

