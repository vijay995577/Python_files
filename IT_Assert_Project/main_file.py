import streamlit as st
from PIL import Image
import pandas as pd
from streamlit_option_menu import option_menu
image1=Image.open("thundersoft.png")
client_choice={"Thundersoft":"TS India Purchases","Qualcomm":"For QC","China":"Chinna"}
Emp_details_choice={"Name":"Employee Name".upper(),"Employee Id":"Employee ID","Email":"Employee Email"}
def Read_Excel(client,name,choice):
    data=xls = pd.ExcelFile('Asset data - Copy.xlsx')
    data = pd.read_excel(data,client_choice[client],header=0)
    details=data.loc[data[Emp_details_choice[choice]]==name]
    st.write(details)
    
    
    
with st.sidebar:
    choose=option_menu("Details",["Emp_details","Asset_details"])
if choose=="Emp_details":
    column1,column2,column3=st.columns([5,5,5])
    with column1:
    	st.image(image1)
    Emp_det=st.selectbox("Get Details Through: ",("Name","Employee Id","Email"))
    if Emp_det=="Email":
        client=st.selectbox("Select your choice",("Thundersoft","Qualcomm","China"))
        email=st.text_input("Enter employee email")
            #st.button("submit")
        if st.button('Submit'):
            Read_Excel(client,email,"Email")
            
    elif Emp_det=="Name":
        client=st.selectbox("Select your choice",("Thundersoft","Qualcomm","China"))
        name=st.text_input("Enter Employee Name")
        if st.button('Submit'):
            Read_Excel(client, name.upper(),Emp_det)
    else:
        client=st.selectbox("Select your choice",("Thundersoft","Qualcomm","China"))
        id=st.text_input("Enter Employee id")
        if st.button('Submit'):
            Read_Excel(client,float(id),"Employee Id")
            
      
