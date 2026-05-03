#  SMS Spam Detection using Machine Learning

This project is a **Machine Learning-based SMS Spam Detection System** that classifies messages as **Spam** or **Ham (Not Spam)**.
It uses Natural Language Processing (NLP) techniques and is deployed as a **web application using Streamlit**.

---

##  Features

* Detects whether an SMS is Spam or Not Spam
* Uses Machine Learning for accurate classification
* Text preprocessing using NLP techniques
* Simple and interactive Streamlit web interface
* Fast and real-time prediction

---

##  Technologies Used

* Python 🐍
* Scikit-learn
* Pandas & NumPy
* NLTK (Natural Language Processing)
* Streamlit

---

##  Project Structure

```
├── app.py              # Streamlit web application
├── model.pkl           # Trained ML model
├── vectorizer.pkl      # TF-IDF vectorizer
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

---

##  How It Works

1. User enters a text message
2. Text is preprocessed (cleaning, tokenization, stopword removal)
3. TF-IDF converts text into numerical features
4. Machine Learning model predicts Spam or Ham
5. Result is displayed instantly

---

##  Installation & Setup

### 1️ Clone the repository

```
git clone https://github.com/your-username/sms-spam-detection.git
cd sms-spam-detection
```

---

### 2️ Install dependencies

```
pip install -r requirements.txt
```

---

### 3️ Run the application

```
streamlit run app.py
```

---

##  Deployment

This project is deployed using **Streamlit Cloud**.

### Steps:

1. Push code to GitHub
2. Connect repository to Streamlit Cloud
3. Deploy `app.py`
4. App will be live online

---

##  Model Information

* Algorithm: Naive Bayes / Logistic Regression
* Feature Extraction: TF-IDF Vectorization
* Dataset: SMS Spam Collection Dataset
* Evaluation Metrics: Accuracy, Precision, Recall

---

##  Screenshots
<img width="600" height="500" alt="Screenshot 2026-05-02 191539" src="https://github.com/user-attachments/assets/ea9ec8a0-8db3-4988-bde6-181006f103e5" />

<img width="600" height="500" alt="Screenshot 2026-05-02 191434" src="https://github.com/user-attachments/assets/b5c4ed12-1883-4f76-a671-6be4e1c18afa" />



---

##  Disclaimer

This system is for educational purposes only and may not always provide 100% accurate results.

---

##  Contributing

Contributions are welcome!
Feel free to fork this repository and submit a pull request.

---

##  License

This project is licensed under the MIT License.

---

##  Acknowledgements

* Kaggle Dataset
* Scikit-learn Documentation
* Streamlit Community

---

