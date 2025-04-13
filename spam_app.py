import joblib
import gdown
import streamlit as st

# Google Drive file IDs (not full URL)
model_id = "1AS9xpZMl4zwW32IJoV92gresTQkceb1A"
vectorizer_id = "1KCWuep5WurRz5KiSSjKg8Sf7IOrm64ov"

# Download if not already present
if not os.path.exists("spam_classifier_nb.pkl"):
    gdown.download(f"https://drive.google.com/uc?id={model_id}", "spam_classifier_nb.pkl", quiet=False)

if not os.path.exists("vectorizer.pkl"):
    gdown.download(f"https://drive.google.com/uc?id={vectorizer_id}", "vectorizer.pkl", quiet=False)

# Load model and vectorizer
model = joblib.load("spam_classifier_nb.pkl")
vectorizer = joblib.load("vectorizer.pkl")

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
