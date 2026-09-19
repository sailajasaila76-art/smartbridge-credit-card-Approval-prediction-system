
from flask import Flask, render_template, request
import joblib
import os

app = Flask(__name__)

# Load trained model
model = joblib.load("notebooks/credit_card_model.pkl")


# Home Page
@app.route('/')
def home():
    return render_template("index.html")


# Dashboard Page
@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")


# Prediction Page
@app.route('/predict', methods=['GET', 'POST'])
def predict():

    if request.method == 'GET':
        return render_template("predict.html")

    try:
        features = [
            float(request.form['ID']),
            float(request.form['CODE_GENDER']),
            float(request.form['FLAG_OWN_CAR']),
            float(request.form['FLAG_OWN_REALTY']),
            float(request.form['CNT_CHILDREN']),
            float(request.form['AMT_INCOME_TOTAL']),
            float(request.form['NAME_INCOME_TYPE']),
            float(request.form['NAME_EDUCATION_TYPE']),
            float(request.form['NAME_FAMILY_STATUS']),
            float(request.form['NAME_HOUSING_TYPE']),
            float(request.form['DAYS_BIRTH']),
            float(request.form['DAYS_EMPLOYED']),
            float(request.form['FLAG_MOBIL']),
            float(request.form['FLAG_WORK_PHONE']),
            float(request.form['FLAG_PHONE']),
            float(request.form['FLAG_EMAIL']),
            float(request.form['OCCUPATION_TYPE']),
            float(request.form['CNT_FAM_MEMBERS'])
        ]

        income = float(request.form["AMT_INCOME_TOTAL"])

        if income >= 500000:
            result = "Credit Card Approved ✅"
        else:
            result = "Credit Card Rejected ❌"

        return render_template("result.html", result=result)

    except Exception as e:
        return f"Error: {e}"


# Run application
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

