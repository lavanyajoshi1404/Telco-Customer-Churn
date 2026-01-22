import streamlit as st
import pickle
import numpy as np
import pandas as pd

# ================= Page Configuration =================
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📉",
    layout="wide"
)

# ================= Load Model & Scaler =================
model = pickle.load(open("churn_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# ================= Title =================
st.markdown(
    "<h1 style='text-align:center;'>📉 Customer Churn Prediction System</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align:center;'>Predict customer churn using XGBoost Machine Learning model</p>",
    unsafe_allow_html=True
)

st.divider()

# ================= Sidebar Inputs =================
st.sidebar.header("🧾 Customer Information")

tenure = st.sidebar.number_input("Tenure (months)", min_value=0, max_value=72, value=12)
monthly_charges = st.sidebar.number_input("Monthly Charges", min_value=0.0, max_value=200.0, value=70.0)
total_charges = st.sidebar.number_input("Total Charges", min_value=0.0, max_value=10000.0, value=1500.0)

contract = st.sidebar.selectbox(
    "Contract Type",
    ["Month-to-month", "One year", "Two year"]
)

payment_method = st.sidebar.selectbox(
    "Payment Method",
    ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"]
)

internet_service = st.sidebar.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

# ================= Encoding Maps =================
contract_map = {"Month-to-month": 0, "One year": 1, "Two year": 2}
payment_map = {
    "Electronic check": 0,
    "Mailed check": 1,
    "Bank transfer (automatic)": 2,
    "Credit card (automatic)": 3
}
internet_map = {"DSL": 0, "Fiber optic": 1, "No": 2}

# ================= Feature Template (MOST IMPORTANT PART) =================
# This guarantees same feature names & order as training
feature_names = list(scaler.feature_names_in_)

input_df = pd.DataFrame(
    np.zeros((1, len(feature_names))),
    columns=feature_names
)

# ================= Fill User Inputs =================
input_df['tenure'] = tenure
input_df['MonthlyCharges'] = monthly_charges
input_df['TotalCharges'] = total_charges
input_df['Contract'] = contract_map[contract]
input_df['PaymentMethod'] = payment_map[payment_method]
input_df['InternetService'] = internet_map[internet_service]

# ================= Scale Input =================
input_scaled = scaler.transform(input_df)

# ================= Main Layout =================
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Customer Summary")
    st.metric("Tenure (Months)", tenure)
    st.metric("Monthly Charges", f"₹ {monthly_charges}")
    st.metric("Total Charges", f"₹ {total_charges}")

with col2:
    st.subheader("📄 Service Details")
    st.write(f"**Contract Type:** {contract}")
    st.write(f"**Payment Method:** {payment_method}")
    st.write(f"**Internet Service:** {internet_service}")

st.divider()

# ================= Prediction =================
st.subheader("🔮 Prediction Result")

if st.button("🚀 Predict Customer Churn"):
    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0][1]

    if prediction == 1:
        st.error("⚠️ Customer is likely to CHURN")
        st.metric("Churn Probability", f"{probability * 100:.2f}%")
    else:
        st.success("✅ Customer is likely to STAY")
        st.metric("Retention Probability", f"{(1 - probability) * 100:.2f}%")

# ================= Info Section =================
st.info("""
### 🧠 About This Project
- **Model:** XGBoost Classifier
- **Problem Type:**  Classification
- **Deployment:** Streamlit Cloud
- **Output:** Churn prediction with probability


""")

# ================= Footer =================
st.markdown(
    "<p style='text-align:center;color:gray;'>Built with ❤️ using Python, XGBoost & Streamlit</p>",
    unsafe_allow_html=True
)
