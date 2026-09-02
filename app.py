import pandas as pd
import numpy as np
import pickle as pk
import streamlit as st 

model = pk.load(open('model.pkl','rb'))

st.header('car price prediction ML model')

car_data=pd.read_csv('cardata.csv')

def get_brand_name(car_name):
    car_name = car_name.split(' ')[0]
    return car_name.strip()
car_data['Car_Name'] = car_data['Car_Name'].apply(get_brand_name)

Car_Name =st.selectbox('select car brand',car_data['Car_Name'].unique())
Year = st.slider('Car manufacturing year',2003,2018)
Driven_kms = st.slider('Driven kms',0,300000)
Fuel_Type = st.selectbox('Fuel Type',car_data['Fuel_Type'].unique())
Selling_type = st.selectbox('Selling Type',car_data['Selling_type'].unique())
Transmission = st.selectbox('Transmission',car_data['Transmission'].unique())
Owner = st.selectbox('Owner',car_data['Owner'].unique())

if st.button('predict price'):
    input_data_model = pd.DataFrame(
    [[Car_Name,Year,0,Driven_kms,Fuel_Type,Selling_type,Transmission,Owner]],
    columns=['Car_Name','Year','Present_Price','Driven_kms','Fuel_Type','Selling_type','Transmission','Owner'])
    
    input_data_model['Owner'].replace(['0','1','3'],[0,1,3], inplace=True)
    input_data_model['Fuel_Type'].replace(['Petrol', 'Diesel', 'CNG'],[1,2,3,], inplace=True)
    input_data_model['Selling_type'].replace(['Individual', 'Dealer'],[1,2], inplace=True)
    input_data_model['Transmission'].replace(['Manual', 'Automatic'],[1,2], inplace=True)
    input_data_model['Car_Name'].replace(['800' ,'Honda' ,'Mahindra' ,'alto' ,'amaze' ,'baleno' ,'brio' ,'camry', 'ciaz',
                                          'city' ,'corolla', 'creta' ,'dzire' ,'elantra', 'eon' ,'ertiga', 'etios',
                                  'fortuner' ,'grand' ,'i10' ,'i20' ,'ignis' ,'innova' ,'jazz', 'land', 'omni',
                                  'ritz' ,'s', 'swift' ,'sx4' ,'verna', 'vitara' ,'wagon', 'xcent'],
                             [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34]
                             ,inplace=True)
   
    car_price = model.predict(input_data_model)

    st.markdown('Car price is going to be '+str(car_price[0]))