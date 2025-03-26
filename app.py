import streamlit as st
import pickle
import os 

# Load the pickled models
tfidf = pickle.load(open("vectorizer.pkl", "rb"))
model = pickle.load(open("model.pkl", "rb"))

# Streamlit Page Configuration
st.set_page_config(page_title="Spam Detector", page_icon="📧", layout="centered")

# Custom CSS for Styling
st.markdown("""
    <style>
        .main {background-color: #f5f7fa;}
        .title {text-align: center; font-size: 28px; font-weight: bold; color: #1f77b4;}
        .result-box {padding: 15px; border-radius: 10px; font-size: 18px; font-weight: bold; text-align: center;}
        .spam {background-color: #ffcccc; color: red;}
        .ham {background-color: #ccffcc; color: green;}
    </style>
""", unsafe_allow_html=True)

# App Title
st.markdown("<h1 class='title'>📩 Spam Email Detector</h1>", unsafe_allow_html=True)
st.write("🔍 Enter an email text below to check if it's **Spam** or **Not Spam**.")

# Input Text Area
user_input = st.text_area(" Type your email here:", height=150)

# Check Spam Button
if st.button("🚀 Analyze Email"):
    if user_input:
        # Transform the input using the TF-IDF vectorizer
        transformed_input = tfidf.transform([user_input])

        # Make prediction
        prediction = model.predict(transformed_input)[0]

        # Display result with better UI
        if prediction == 1:
            st.markdown("<div class='result-box spam'>⚠️ This is a Spam Email!</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='result-box ham'>✅ This is NOT a Spam Email.</div>", unsafe_allow_html=True)
    else:
        st.warning(" Please enter an email text.")

# Footer
st.markdown("---")

# Run on port 8501 or a different port if needed

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Default to 10000 if PORT is not set
    app.run(host="0.0.0.0", port=port)
