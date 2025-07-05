import streamlit as st
import pickle
import numpy as np
with open("model.pkl", "rb") as f:
    model = pickle.load(f)
st.title("Loan Approval model")
income = st.number_input("Income", min_value = 0)
credit_score = st.number_input("creditscore", min_value = 300)
loan_amount = st.number_input("loanamount", min_value = 1000)
loanterm = st.selectbox("Loan Term", [180,240,360])

if st.button("Predict"):
    input_data =np.array([[income, credit_score, loan_amount, loanterm]])
    prediction = model.predict(input_data)[0]
    
if prediction == 1:
    st.success("Loan Apprved")
else:
    st.error("Loan not Approved")
