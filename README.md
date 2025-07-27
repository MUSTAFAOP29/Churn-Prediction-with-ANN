# 🧠 Customer Churn Prediction Web App

A user-friendly **Streamlit web application** that predicts customer churn using a deep learning model built with **TensorFlow**. The application allows users to input customer information and returns the likelihood of that customer leaving the service.

---

## 🚀 Features

- 📊 Real-time prediction of customer churn probability
- 🔍 Preprocessing with `StandardScaler`, `LabelEncoder`, and `OneHotEncoder`
- 💾 Model and encoders loaded from pre-trained files (`model.h5`, `pkl`)
- 🧮 Interactive input using Streamlit widgets
- 🔐 Local `.gitignore` to prevent pushing virtual environments and sensitive files

---

## 🛠️ Technologies Used

- [Python](https://www.python.org/)
- [TensorFlow](https://www.tensorflow.org/)
- [Streamlit](https://streamlit.io/)
- [Scikit-learn](https://scikit-learn.org/)
- [Pandas](https://pandas.pydata.org/)
- [Pickle](https://docs.python.org/3/library/pickle.html)

---

## 🧾 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt

customer-churn-app/
│
├── model.h5                     # Trained TensorFlow model
├── scaler.pkl                  # Trained StandardScaler
├── label_encoder_gender.pkl    # Trained LabelEncoder for Gender
├── one_hot_encoder.pkl         # Trained OneHotEncoder for Geography
├── app.py                      # Streamlit app script
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignored files
└── README.md                   # Project documentation

```
