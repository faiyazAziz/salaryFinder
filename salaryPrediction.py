import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
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

def ratio():
    lst = []
    lst2 = []
    lst3 = []
    for i in range(len(all_job_roles)):
        job = all_job_roles[i]
        lst2.append(job)
        aa = df[df['Job Roles']==job]
        count = aa.shape[0]
        lst.append(count)
        lst3.append(0)
    return lst,lst2,lst3

def compare_company(options):
    lst = []
    for i in range(len(options)):
        aa = df[df['Company Name']==options[i]]
        count = aa.shape[0]
        lst.append(count)
    return lst


# salaryv,r = find_salary('Sasken','Android Developer','Bangalore','Full Time','Android')
# print(salaryv)

# st.title("**Welcome To** SalaryJano :sunglasses:")
# if "button_clicked" not in st.session_state:
#     st.session_state.button_clicked = False
#
# def callback():
#     st.session_state.button_clicked = True


st.markdown('''
            <meta charset = "UTF-8">
            <h3 style = "vertical-align:text-top"><i>Welcome To </i>
            <font size="7" color="red" face="Optima">SalaryJano &#129297	
            </font></h3>
            ''',unsafe_allow_html=True)

with st.sidebar:
    add_radio = st.radio("What do you want to do",("Predict Salary","Analyze Company","Compare Company","Ratio of Job"))

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)

if(add_radio == "Predict Salary"):
    st.header("Predict Your Salary")
    company = st.selectbox('Chose Your Dream Company',all_companies)
    job_title = st.selectbox('Choose Job Title',all_job_titles)
    location = st.selectbox('Choose Location',all_loaction)
    employment_status = st.selectbox('Choose Status',all_employment_status)
    job_role = st.selectbox('Choose Job Role',all_job_roles)

    submit = st.button('SALARY')

    if(submit):
        salary, rating = find_salary(company,job_title,location,employment_status,job_role)
        if(math.isnan(salary)):
            left_co, cent_co, last_co = st.columns(3)
            with cent_co:
                st.text("NO DATA FOUND")
                st.image('NoData.png')
        else:
            st.text("")
            st.text("")
            st.write("Rs. " + str(salary))


if(add_radio == "Ratio of Job"):
    st.header("Pie Chart of Tech Jobs In India")
    y,labels,explode = ratio()
    y = np.array(y)
    labels = np.array(labels)
    # explode[0]=0.2
    explode[7]=0.1
    fig,ax = plt.subplots()
    ax.pie(y,labels=labels,shadow=True,explode=explode)
    st.pyplot(fig,use_container_width=True)

if(add_radio=='Compare Company'):
    options = st.multiselect("Select Company To Compare",all_companies,max_selections=4)
    compare = st.button("COMPARE")
    if(compare):
        st.text("")
        st.text("")
        st.text("")
        st.text("")
        y = compare_company(options)
        fig,ax = plt.subplots()
        ax.bar(options,y)
        st.pyplot(fig,use_container_width=True)



