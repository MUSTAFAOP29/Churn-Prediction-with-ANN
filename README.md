# 🧠 Customer Churn Prediction Web App

A user-friendly **Streamlit web application** that predicts customer churn using a deep learning model built with **TensorFlow**. The application allows users to input customer information and returns the likelihood of that customer leaving the service.

---
![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-orange)
![Neural Network](https://img.shields.io/badge/Model-ANN%20(Keras%2FTensorFlow)-red)
![Data](https://img.shields.io/badge/DataSource-CSV%20%7C%20Excel-yellow)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)



## 🚀 Features

- 📊 Real-time prediction of customer churn probability
- 🔍 Preprocessing with `StandardScaler`, `LabelEncoder`, and `OneHotEncoder`
- 💾 Model and encoders loaded from pre-trained files (`model.h5`, `pkl`)
- 🧮 Interactive input using Streamlit widgets
- 🔐 Local `.gitignore` to prevent pushing virtual environments and sensitive files

---

## 📁 Folder Structure
```
NSI-Booking-App/
│
├── main.py             # FastAPI backend
├── frontend.py         # Streamlit frontend
├── requirements.txt    # All required packages
└── hall_booking.db     # (ignored) SQLite DB file
```

## 🛠️ Technologies Used
```
- [Python](https://www.python.org/)
- [TensorFlow](https://www.tensorflow.org/)
- [Streamlit](https://streamlit.io/)
- [Scikit-learn](https://scikit-learn.org/)
- [Pandas](https://pandas.pydata.org/)
- [Pickle](https://docs.python.org/3/library/pickle.html)

---
```
## Installation & Setup
```
# Clone the repo
git clone https://github.com/your-username/churn-prediction-app.git
cd churn-prediction-app

# (Optional) Create a virtual environment
python -m venv myenv
myenv\Scripts\activate   # On Windows
# source myenv/bin/activate  # On Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py

```
## Install dependencies using:

```

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

## 🧠 Tech Stack
| Component     | Technology                      |
| ------------- | ------------------------------- |
| Programming   | Python 3.11                     |
| Frontend      | Streamlit                       |
| Model         | Artificial Neural Network (ANN) |
| ML Framework  | Scikit-learn                    |
| Data Handling | Pandas, NumPy                   |
| Visualization | Matplotlib, Seaborn             |
| File Formats  | CSV, Excel                      |
| Status        | Completed                       |

## 🔍 Important Note
This project is a demonstration of how Artificial Neural Networks (ANN) can be leveraged using Scikit-learn to solve real-world problems through an interactive Streamlit interface. All dependencies are managed through requirements.txt, and the project avoids uploading any virtual environment files or sensitive data to the repository for clean version control and collaboration.

## ✍️ Author
Syed Mustafa 
B.Tech AI & Data Science | Data Science & Agentic AI Enthusiast

## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/syedmustafa29)


