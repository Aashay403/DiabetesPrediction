# 🩺 Diabetes Prediction Web App

This is a Django-based web application that uses a **Logistic Regression model** to predict whether a person is likely to have diabetes based on medical input features. The prediction is based on the **Pima Indians Diabetes Dataset**.

---

## 🚀 Features

- User-friendly web interface for inputting medical details
- Machine learning model trained with `scikit-learn`
- Real-time prediction based on user input
- Displays result: **Positive** or **Negative** for diabetes

---

## 📊 Dataset

- **Source**: `diabetes.csv` (Pima Indians Diabetes Dataset)
- **Target Column**: `Outcome` (0 = No Diabetes, 1 = Diabetes)
- Features used include:
  - Pregnancies
  - Glucose
  - BloodPressure
  - SkinThickness
  - Insulin
  - BMI
  - DiabetesPedigreeFunction
  - Age

---

## 🧠 Model

- **Algorithm**: Logistic Regression (from `scikit-learn`)
- **Training**: The model is trained every time a prediction is requested *(Note: this is inefficient and can be improved)*

---

## 🛠️ Requirements

Install the required packages using pip:

```bash
pip install -r requirements.txt
