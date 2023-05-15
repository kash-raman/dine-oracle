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
# Global Variables
theme_plotly = None # None or streamlit
 

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
postal_code = r.raw['address']['postcode']
st.write(f"Stored position:   {location}")

predict = form.form_submit_button("Predict")
if predict:
    st.write(postal_code)
    st.write(features_available)
    st.write(speciality)