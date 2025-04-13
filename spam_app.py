import streamlit as st
import joblib
import os
import gdown

# Google Drive file IDs
model_id = "1AS9xpZMl4zwW32IJoV92gresTQkceb1A"
vectorizer_id = "1KCWuep5WurRz5KiSSjKg8Sf7IOrm64ov"

# File names
model_file = "spam_classifier_nb.pkl"
vectorizer_file = "vectorizer.pkl"

# Download if not present
if not os.path.exists(model_file):
    gdown.download(f"https://drive.google.com/uc?id={model_id}", model_file, quiet=False)

if not os.path.exists(vectorizer_file):
    gdown.download(f"https://drive.google.com/uc?id={vectorizer_id}", vectorizer_file, quiet=False)

# Load model and vectorizer
model = joblib.load(model_file)
vectorizer = joblib.load(vectorizer_file)

# Streamlit app UI
st.title("📬 Email Spam Detector")
email_input = st.text_area("✉️ Paste Email Text:")

if st.button("🔍 Predict"):
    if not email_input.strip():
        st.warning("Please enter an email.")
    else:
        vector = vectorizer.transform([email_input.lower()])
        result = model.predict(vector)[0]
        label = "🚨 Spam" if result == 1 else "✅ Not Spam"
        st.success(f"Prediction: {label}")
