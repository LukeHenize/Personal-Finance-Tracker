import streamlit as st
import pandas as pd
import numpy as np

st.title("Personal Finance Tracker")

#setup bank statement csv file
# bankStatement = pd.DataFrame({}, columns=["Transaction Date", "Transaction Amount","Vendor Name","Withdrawal/Deposit", "Transaction Type", "Balance Change"])

# #ask for bank statement input
# with st.form("getTransaction") :
#     transDate = st.date_input("Enter transaction date")
#     transAmount = st.number_input("Enter amount", 0, 10000)
#     transName  = st.text_input("Enter vendor name")
#     withdrawalOrDeposit = st.radio("Withdrawal or Deposit?", ["Withdrawal", "Deposit"])
#     transType = st.selectbox("Enter transaction type", ["Mortgage/Rent", "Food/Groceries", "Medical Expense", "ATM Withdrawal", "Misc. Withdrawal",
#                                                         "Paycheck","ATM Deposit", "Misc. Deposit"])
#     balanceChange = transAmount
#     if withdrawalOrDeposit == "Withdrawal" :
#        balanceChange *= -1
#     submitted = st.form_submit_button("Enter transaction to my bank statement")
#     if submitted :
#         if "statement" in st.session_state :
#             bankStatement = st.session_state["statement"]
#         bankStatement.loc[len(bankStatement.index)] = [transDate, transAmount, transName, withdrawalOrDeposit, transType, balanceChange] 
#         st.session_state["statement"] = bankStatement 
# #plot bankStatement
# #st.line_chart(bankStatement, y="Transaction Amount")
# st.dataframe(bankStatement)

if st.button("My bank statement is complete!") :
    #st.session_state["statement"].to_csv("statement.csv", index=False)
    #st.session_state["statement"] = pd.DataFrame()
    #load df again to avoid using session state
    statement = pd.read_csv("statement.csv")
    st.dataframe(statement)
    st.line_chart(statement, x="Transaction Date", y="Balance Change")