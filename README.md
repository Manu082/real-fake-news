# 📰 Fake News Detection using Machine Learning

A Streamlit web app that predicts if a news article is real or fake using NLP and machine learning.

## ✅ Overview
- Model: Logistic Regression
- Text vectorization: TF-IDF
- Accuracy: ~98%

## 📦 Files
- Fake & Real News.ipynb: Jupyter notebook for training the model
- app.py: Streamlit app for prediction
- fake_news_model.pkl / tfidf_vectorizer.pkl: Saved model and vectorizer
- Fake.csv / True.csv: Dataset
- requirements.txt: Dependencies

## ✅ How to Run
1. Install dependencies:


pip install -r requirements.txt

2. Train model:
- Open and run Fake & Real News.ipynb (creates .pkl files)
3. Start the app:


streamlit run app.py