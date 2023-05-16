# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
import time
from streamlit_folium import st_folium
import folium
import geopy
import pickle
import numpy as np
# Global Variables
theme_plotly = None # None or streamlit
model_avail = True
city= ''

def predict_resturant_success(model,city,postal_code,dogsallowed,restaurantstableservice,wheelchairaccessible,happyhour,goodformeal,american_new,american_traditional,breakfast_brunch,burgers,cafes,chicken_wings,chinese,coffee_tea,delis,fast_food,food,italian,mexican,pizza,salad,sandwiches,seafood,specialty_food):
    input = np.array([city,postal_code,dogsallowed,restaurantstableservice,wheelchairaccessible,happyhour,goodformeal,american_new,american_traditional,breakfast_brunch,burgers,cafes,chicken_wings,chinese,coffee_tea,delis,fast_food,food,italian,mexican,pizza,salad,sandwiches,seafood,specialty_food])
    predict = model.predict(input)
    return int(predict)

def check_status(value):
    if value == 1:
        return "Success"
    elif value == 0:
        return "Failed"
    else:
        return "Invalid value"
def check_in_list(value,_list):
    if(value in _list):
        return 1
    return 0

# Config
st.set_page_config(page_title='DineOracle - Prediction', page_icon=':bar_chart:', layout='wide')

# Title
st.title('🌍 DineOracle - Prediction') 
DEFAULT_LATITUDE = 40.
DEFAULT_LONGITUDE = -75.
 
form= st.form("form")
features_available = form.multiselect('Feature Available', ["Good For Meal", "Fast Food","Salad","Cafes","Happy Hour","Dogs Allowed","Breakfast & Lunch","Coffee/Tea",
                                            "Table Service" ,"WheelChair Accessible" ])
speciality = form.multiselect('Speciality Food', [ "American", "Italian", "Chinese","Mexican","Breakfast","Lunch","Beverages",
                                            "Pizza", "Sandwiches","Delis" ,"Seafood","Burgers","Chicken Wings"])

predict = form.form_submit_button("Predict")
geo_locator = geopy.Nominatim(user_agent='1234')
m = folium.Map(location=[DEFAULT_LATITUDE, DEFAULT_LONGITUDE], zoom_start=10)
m.add_child(folium.LatLngPopup())
f_map = st_folium(m, width=500)
selected_latitude = DEFAULT_LATITUDE
selected_longitude = DEFAULT_LONGITUDE
if f_map.get("last_clicked"):
    selected_latitude = f_map["last_clicked"]["lat"]
    selected_longitude = f_map["last_clicked"]["lng"]
    #st.write(f"Stored position: {selected_latitude}, {selected_longitude}")
if selected_latitude == DEFAULT_LATITUDE and selected_longitude == DEFAULT_LONGITUDE:
    st.write("Selected position has default values!")
r = geo_locator.reverse((selected_latitude, selected_longitude))
location =r.raw['display_name']
city =  list(filter(lambda x: 'city' in x, r.raw['address']))  
postal_code = r.raw['address']['postcode']
st.write(f"Stored position:   {location}")

filename = 'xgboost_baseline_model'
with open(filename, 'rb') as f:
    model = pickle.load(f)
if predict:
    
    joinedList= features_available + speciality
    if model_avail:
        
        predict_resturant_success(model,city ,postal_code,check_in_list("Dogs Allowed",joinedList),check_in_list("Table Service",joinedList),
                                  check_in_list("WheelChair Accessible",joinedList),check_in_list("Happy Hour",joinedList), check_in_list("Good For Meal",joinedList))
        st.success('The resturant with these feature will be {}'.format(check_status(output)))