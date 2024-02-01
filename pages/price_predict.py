import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.set_page_config('Price Prediction')

st.title('Price Prediction')

with open('artifacts/df.pkl','rb') as file:
    df = pickle.load(file)

with open('artifacts/pipeline.pkl','rb') as file:
    pipeline = pickle.load(file)

st.header('Enter your inputs')

property_type = st.selectbox('Property Type', ['Residential Apartment','Independent House/Villa','Independent/Builder Floor'])
city = st.selectbox('City Zone', df['CITY'].unique().tolist())
bedroom_num = float(st.selectbox('No. of Bedrooms', df['BEDROOM_NUM'].unique().tolist()))
area = st.number_input('Area (in Sqft)')
balcony_num = float(st.selectbox('No. of Balconies', df['BALCONY_NUM'].unique().tolist()))
location = st.selectbox('Location', df[df['CITY'] == city]['Location'].unique().tolist())
luxury_category = st.selectbox('Luxury', df['luxury_category'].unique().tolist())
floor_category = st.selectbox('Floor Category', df['floor_category'].unique().tolist())
age_category = st.selectbox('Age', df['age_category'].unique().tolist())
landmark_Category = st.selectbox('Landmarks', df['Landmark_Category'].unique().tolist())

if st.button('Predict'):

    data = [[property_type, city, bedroom_num, area, balcony_num, location, luxury_category, floor_category, age_category, landmark_Category]]
    columns = ['PROPERTY_TYPE', 'CITY', 'BEDROOM_NUM', 'AREA', 'BALCONY_NUM',
       'Location', 'luxury_category', 'floor_category', 'age_category',
       'Landmark_Category']
    
    one_df = pd.DataFrame(data, columns=columns)

    base_price = np.expm1(pipeline.predict(one_df))[0]

    low_price = base_price - 0.05
    high_price = base_price + 0.05

    st.text(f'The Price of the Flat is between {round(low_price,2)}Cr. and {round(high_price,2)}Cr.')
