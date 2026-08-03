import streamlit as st
import pandas as pd
import requests

# Base URL of the Flask backend
BACKEND_URL = "http://backend:7860"

# Set the title of the Streamlit app
st.title("Revenue Prediction Model Frontend")

# Section for online prediction
st.subheader("Product Sales Prediction")

# Input fields for product and store data
Product_Weight = st.number_input("Product Weight", min_value=0.00, value=12.66)
Product_Sugar_Content = st.selectbox("Product Sugar Content", ["Low Sugar", "Regular", "No Sugar"])
Product_Allocated_Area = st.number_input("Product Allocated Area", min_value=0.001, value=1.00) #Code to define the UI element for Product_Allocated_Area
Product_MRP = st.number_input("Maximum Retail Price", min_value=1.00, value=1000.00) #Code to define the UI element for Product_MRP
Store_Size = st.selectbox("Store Size", ["Small", "Medium", "High"]) #Code to define the UI element for Store_Size
Store_Location_City_Type = st.selectbox("Store Location City Type", ["Tier 1", "Tier 2", "Tier 3"]) #Code to define the UI element for Store_Location_City_Type
Store_Type = st.selectbox("Store Type", ["Food Mart", "Departmental Store", "Supermarket Type1", "Supermarket Type2"]) #Code to define the UI element for Store_Type
Product_Id_char = st.selectbox("Product ID Char", ["FD", "NC", "DR"]) #Code to define the UI element for Product_Id_char
Store_Age_Years = st.number_input("Store Age Years", min_value=0, value=50) #Code to define the UI element for Store_Age_Years
Product_Type_Category = st.selectbox("Product Type Category", ["Perishable", "Non Perishable"]) #Code to define the UI element for Product_Type_Category

# Convert user input into a DataFrame
product_data = ([{
    "Product_Weight": Product_Weight,
    "Product_Sugar_Content": Product_Sugar_Content,
    "Product_Allocated_Area": Product_Allocated_Area,
    "Product_MRP": Product_MRP,
    "Store_Size": Store_Size,
    "Store_Location_City_Type": Store_Location_City_Type,
    "Store_Type": Store_Type,
    "Product_Id_char": Product_Id_char,
    "Store_Age_Years": Store_Age_Years,
    "Product_Type_Category": Product_Type_Category
}])

# Make prediction when the "Predict" button is clicked
if st.button("Predict", type='primary'):
# Send data to Flask API
    response = requests.post(f"{BACKEND_URL}/v1/predict", json=product_data.to_dict(orient='records')[0])   
    if response.status_code == 200:
        prediction = response.json()['Predicted Sales (Dollars)']
        st.success(f"Predicted Product Store Sales Total: {prediction:.2f}")
    else:
        st.error("Error in API request")
