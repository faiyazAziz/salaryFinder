import math
import base64
import pandas as pd
import streamlit
import streamlit as st

df = pd.read_csv("salaryData.csv", skipinitialspace=True)
all_companies = df['Company Name'].unique()
all_job_titles = df['Job Title'].unique()
all_loaction = df['Location'].unique()
all_employment_status = df['Employment Status'].unique()
all_job_roles = df['Job Roles'].unique()

# print(all_loaction)
def find_salary(company_name,job_title,location,employment_status,job_roles):
    aa = df
    aa = aa[aa['Company Name'] == company_name]
    aa = aa[aa['Job Roles'] == job_roles]
    aa = aa[aa['Location'] == location]
    aa = aa[aa['Employment Status'] == employment_status]
    aa = aa[aa['Job Title'] == job_title]

    salary = aa['Salary'].mean()
    rating = aa['Rating'].mean()

    return salary,rating

# salaryv,r = find_salary('Sasken','Android Developer','Bangalore','Full Time','Android')
# print(salaryv)

st.markdown('''
            <meta charset = "UTF-8">
            <h3 ><i>Welcome To </i>
            <font size="7" color="red" face="Optima">SalaryJano &#129297	
            </font></h3>
            ''',unsafe_allow_html=True)
# if "button_clicked" not in st.session_state:
#     st.session_state.button_clicked = False
#
# def callback():
#     st.session_state.button_clicked = True

with st.sidebar:
    add_radio = st.radio("What do you want to do",("Predict Salary","Analyze Company","Compare Company"))

if(add_radio == "Predict Salary"):
    company = st.selectbox('Chose Your Dream Company',all_companies)
    job_title = st.selectbox('Choose Job Title',all_job_titles)
    location = st.selectbox('Choose Location',all_loaction)
    employment_status = st.selectbox('Choose Status',all_employment_status)
    job_role = st.selectbox('Choose Job Role',all_job_roles)

    submit = st.button('SUBMIT')

    if(submit):
        salary, rating = find_salary(company,job_title,location,employment_status,job_role)
        if(math.isnan(salary)):
            left_co, cent_co, last_co = st.columns(3)
            with cent_co:
                st.text("NO DATA FOUND")
                st.image('NoData.png')
        else:
            tt =st.write(salary)
