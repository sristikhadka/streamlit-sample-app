import streamlit as st
# st.title("Monthly payment calculator for a loan")
# loan_amount = st.number_input("Enter the loan amount")
# time_duration = st.number_input("Enter duration in year you want to take loan",step = 3)
# loan_rate = st.number_input("Enter the interest rate")

# interest_calculated = False

# if loan_amount and time_duration and loan_rate:
#     interest = loan_amount + time_duration * loan_rate/1000
#     return_amount = loan_amount + interest
#     monthly_payment = round(return_amount / (time_duration * 12),2)
#     st.write("Your monthly income is {monthly_payment}")
# interest_calculated = True
 
# st.date_input("Enter a date,date(2001,18,08)")

# st.write("dob")
# st.time_input("Enter a time")


# clicked = st.button("Click me to know more")
# if clicked:
#     st.write("You are dump. Clicking on random bottom you get hacked")



st.checkbox("you are mine")
user_choices = ["Male","Female","Don't Disclose"]
# gender = st.radio("Select the Gender",["Male","Female"])
gender = st.multiselect("Select the Gender",["Male","Female"])

if gender:
    st.write(f"Your gender is {gender}")
# st.write("Your gender is {gender}")