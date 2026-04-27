
import streamlit as st
import pickle

st.title("SMS Spam Detector")
st.write("Enter an SMS message below to check if it's spam or not.")

# Load the model and vectorizer
try:
    with open('model.pkl', 'rb') as file:
        loaded_artifacts = pickle.load(file)
    model = loaded_artifacts['model']
    vectorizer = loaded_artifacts['vectorizer']
    st.success("Model and vectorizer loaded successfully!")
except FileNotFoundError:
    st.error("Error: 'model.pkl' not found. Please ensure the model training and saving cell has been executed and the file exists.")
    st.stop()
except Exception as e:
    st.error(f"Error loading model or vectorizer: {e}")
    st.stop()

# Input text box for the SMS message
message = st.text_area("Enter SMS message:", "")

if st.button("Predict"):
    if message:
        # Preprocess the message using the loaded vectorizer
        message_tfidf = vectorizer.transform([message])

        # Make prediction
        prediction = model.predict(message_tfidf)[0]

        # Display result
        if prediction == 1:
            st.error("This is a SPAM message!")
        else:
            st.success("This is NOT SPAM.")
    else:
        st.warning("Please enter a message to predict.")
