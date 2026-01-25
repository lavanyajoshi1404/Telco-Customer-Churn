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

## 📊 Model E

