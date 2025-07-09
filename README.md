# 📰 Fake News Detection using Machine Learning

A Streamlit web app that predicts if a news article is Real or Fake using Natural Language Processing (NLP) and Machine Learning.

✅Overview

   Model: Logistic Regression

   Vectorization: TF-IDF

   Accuracy: ~98%

   Interface: Interactive Streamlit web app

It helps identify potentially fake news by analyzing text content with NLP techniques.

🚀 Live Demo

  🌐 Check it out here:

   👉 https://real-fake.streamlit.app/

⚙️ Features

  ✅ Predict whether a news article is Real or Fake


  ✅ NLP preprocessing with TF-IDF Vectorizer


  ✅ Trained Logistic Regression model


  ✅ Clean, responsive Streamlit UI


  ✅ ~98% training accuracy


  ✅ Easy deployment on Streamlit Cloud

📦 Project Structure


Fake-Real-News/
├── app.py                    ← Streamlit web app
├── Fake & Real News.ipynb    ← Jupyter notebook for training
├── fake_news_model.pkl       ← Saved ML model
├── tfidf_vectorizer.pkl      ← Saved TF-IDF vectorizer
├── Fake.csv                  ← Fake news dataset
├── True.csv                  ← Real news dataset
├── requirements.txt          ← Dependencies
└── README.md                 ← You're here!

1️⃣ Clone the repository

  git clone https://github.com/Manu082/Fake-Real-News.git
  cd Fake-Real-News

2️⃣ Install dependencies

  pip install -r requirements.txt

3️⃣ Train the model (Optional)


  If you want to retrain:

  Open Fake & Real News.ipynb in Jupyter Notebook.

  Run all cells to generate:

  fake_news_model.pkl

  tfidf_vectorizer.pkl

✔️ Or use the existing provided .pkl files.

4️⃣ Start the Streamlit app

  streamlit run app.py

✅ Open your browser at http://localhost:8501.

✅ Dataset Source

  This project uses the Fake and Real News Dataset from Kaggle.

   Fake.csv: Fake news articles

   True.csv: Real news articles

✅ Requirements

nginx
Copy
Edit
streamlit
scikit-learn
pandas
numpy
seaborn
matplotlib

✅ All listed in requirements.txt

📜 License

  This project is licensed under the MIT License.

💡 Author

  👤 MANAS DIDWANIA
  📧 [didwania082@gmail.com]

⭐️ Notes

  Make sure .pkl files are in the same directory as app.py.

  Keep model files under GitHub’s file size limits (~100MB).

✨ Happy Coding!


