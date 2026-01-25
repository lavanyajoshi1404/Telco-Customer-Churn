# Telco Customer Churn Prediction System

## 📌 Project Overview

Customer churn is one of the most critical challenges faced by telecom companies, as acquiring new customers is significantly more expensive than retaining existing ones. This project focuses on building an **end-to-end Customer Churn Prediction System** using Machine Learning and deploying it as an interactive web application.

The system predicts whether a customer is likely to churn based on their service usage, contract details, and billing information, enabling businesses to take proactive retention actions.

---

## 🎯 Project Objectives

* Analyze customer behavior and churn patterns
* Build a robust machine learning model to predict churn
* Evaluate model performance using standard classification metrics
* Deploy the trained model using **Streamlit** for real-time predictions
* Provide churn probability along with prediction for better decision-making

---

## 📂 Dataset Description

The dataset contains telecom customer-level data with the following categories:

* **Demographic Information**: Gender, Senior Citizen, Partner, Dependents
* **Account Information**: Tenure, Contract Type, Payment Method
* **Billing Information**: Monthly Charges, Total Charges
* **Services Used**: Phone Service, Internet Service, Online Security, Tech Support, Streaming Services
* **Target Variable**: `Churn` (Yes / No)

---

## 🛠️ Technologies & Tools Used

* **Programming Language**: Python
* **Data Analysis & ML Libraries**:

  * NumPy
  * Pandas
  * Matplotlib
  * Seaborn
  * Scikit-learn
  * XGBoost
* **Model Deployment**: Streamlit
* **Environment**: Jupyter Notebook / Google Colab

---

## 🔍 Exploratory Data Analysis (EDA)

* Checked for missing and inconsistent values
* Analyzed churn distribution across different customer segments
* Studied impact of:

  * Contract type
  * Tenure length
  * Monthly charges
  * Internet and support services
* Identified high churn among customers with:

  * Month-to-month contracts
  * Fiber optic internet
  * High monthly charges

---

## ⚙️ Data Preprocessing

* Handled missing values in `TotalCharges`
* Encoded categorical variables
* Feature scaling using **StandardScaler**
* Train-test split for model evaluation

---

## 🤖 Model Building

The following models were experimented with:

* Logistic Regression
* Decision Tree Classifier
* Random Forest Classifier
* **XGBoost Classifier (Final Model)**

**Reason for choosing XGBoost:**

* Better handling of non-linear relationships
* High performance on tabular data
* Improved accuracy and recall for churn prediction

---

## 📊 Model Evaluation

The model was evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

**Final Model Performance (XGBoost):**

* Achieved strong balance between precision and recall
* Effectively identified high-risk churn customers

---

## 🚀 Model Deployment (Streamlit App)

The trained model is deployed using **Streamlit**, allowing users to:

* Enter customer details via an interactive UI
* Get instant churn prediction (Churn / Stay)
* View churn probability percentage

### 🔮 Application Features

* User-friendly sidebar input form
* Real-time prediction
* Probability-based confidence score
* Clean and responsive UI

---

## 📁 Project Structure

```
├── Telco-Customer-Churn.csv
├── Telco_Customer_Churn.ipynb
├── app.py
├── churn_model.pkl
├── scaler.pkl
├── requirements.txt
└── README.md
```

---

## 📈 Key Insights

* Long-term contract customers are less likely to churn
* Customers without tech support and online security churn more
* Higher monthly charges increase churn probability
* Tenure is one of the strongest predictors of customer retention

---

## 🔮 Future Enhancements

* Add more customer features for improved prediction
* Perform hyperparameter tuning for further optimization
* Deploy the application on Streamlit Cloud / AWS
* Integrate dashboard for churn analytics and monitoring

---

## 👩‍💻 Author

**Lavanya**
Engineering Student | Aspiring Software Developer & Machine Learning Enthusiast

---

## 📜 License

This project is intended for educational and learning purposes only.


