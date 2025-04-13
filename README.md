# 📬 Spam Email Detector App(https://amosdetective.streamlit.app/)

This is a lightweight web application built with **Streamlit** that uses a trained **Naive Bayes model** and **TF-IDF vectorizer** to detect whether an email is 🚨 **spam** or ✅ **not spam**.

## 🔍 Features

- Paste any email text and instantly get a prediction
- Clean and intuitive UI
- Loads large model files from Google Drive using `gdown`

## 🛠 Technologies Used

- Python
- Scikit-learn
- Joblib
- Streamlit
- gdown

## 🚀 Deployment

This app is designed for deployment on [Streamlit Cloud](https://streamlit.io/cloud).  
No need to upload model files directly — they're fetched dynamically using `gdown`.
Vectorizer.pkl — Trained TF-IDF vectorizer
