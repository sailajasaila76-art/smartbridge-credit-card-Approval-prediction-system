# 💳 Credit Card Approval Prediction Using Machine Learning

## 📌 Project Overview

Banks receive thousands of credit card applications every day. Manually reviewing every application is time-consuming and prone to human error. This project automates the credit card approval process using Machine Learning by analyzing applicant financial and demographic information.

The application predicts whether a customer is likely to be approved or rejected for a credit card using a trained Random Forest model. The trained model is integrated into a Flask web application with a professional dashboard.

---

## 🎯 Objectives

- Automate credit card approval prediction.
- Reduce manual verification effort.
- Improve decision-making using Machine Learning.
- Provide a simple web interface for users.

---

## 🚀 Features

- Data Cleaning and Preprocessing
- Missing Value Handling
- Label Encoding
- Feature Engineering
- Logistic Regression Model
- Decision Tree Model
- Random Forest Model
- XGBoost Model
- Model Comparison
- Best Model Selection
- Flask Web Application
- Professional Dashboard
- Real-Time Prediction

---

## 🛠 Technologies Used

- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Matplotlib
- Joblib
- HTML
- CSS
- Bootstrap 5

---

## 📂 Project Structure

```
credit_card_approval/
│
├── app.py
├── requirements.txt
├── README.md
├── model_training.ipynb
│
├── dataset/
│   ├── application_record.csv
│   └── credit_record.csv
│
├── models/
│   ├── model.pkl
│   ├── label_encoder.pkl
│   └── feature_names.pkl
│
├── templates/
│   ├── dashboard.html
│   ├── index.html
│   └── result.html
│
├── static/
│   ├── style.css
│   └── images/
│
└── screenshots/
```

---

## 📊 Machine Learning Models

| Model | Accuracy |
|--------|----------|
| Logistic Regression | 98.53% |
| Decision Tree | 98.30% |
| Random Forest | **98.69%** |
| XGBoost | 98.60% |

**Best Model:** Random Forest

---

## ▶️ Installation

Clone the repository

```bash
git clone <repository_url>
```

Move to project folder

```bash
cd credit_card_approval
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Flask application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

## 📋 Workflow

1. Load Dataset
2. Data Cleaning
3. Feature Engineering
4. Label Encoding
5. Train Machine Learning Models
6. Compare Accuracy
7. Save Best Model
8. Flask Integration
9. User Prediction
10. Display Result

---

## 📸 Application Screenshots

- Dashboard
- Prediction Form
- Approval Result
- Rejection Result

---

## 📈 Future Enhancements

- IBM Watson Deployment
- Cloud Hosting
- User Authentication
- Database Integration
- Admin Dashboard
- Email Notifications
- REST API

---

## 👥 Team Members

- Hari Priya Kopparthy (Team Lead)
- Gonigunta Sailaja
- Shalusha Gonigunta
- Gnana Prasuna H. J.

---

## 📄 License

This project is developed for educational purposes as part of the SmartBridge Internship Program.

---

## 🙏 Acknowledgements

- SmartBridge
- IBM SkillsBuild
- Scikit-learn
- Flask
- Kaggle
