# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
import time

# Global Variables
theme_plotly = None # None or streamlit
 

# Config
st.set_page_config(page_title='DineOracle - Prediction', page_icon=':bar_chart:', layout='wide')

# Title
st.title('🌍 DineOracle - Prediction')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)
    with st.form(key='my_form'):
        city_name = st.text_input('Location(postal code/city name):')
        features_available = st.multiselect('Feature Available', ["Good For Meal", "Fast Food","Salad","Cafes","Happy Hour","Dogs Allowed","Breakfast & Lunch","Coffee/Tea",
                                            "Table Service" ,"WheelChair Accessible" ])
        speciality = st.multiselect('Speciality Food', [ "American", "Italian", "Chinese","Mexican","Breakfast","Lunch","Beverages",
                                            "Pizza", "Sandwiches","Delis" ,"Seafood","Burgers","Chicken Wings"])
        submit_button = st.form_submit_button(label='Predict')
     
#     with st.spinner(text='In progress'):
#         time.sleep(5)
#         st.success('Done')

# st.progress(progress_variable_1_to_100)
# st.balloons()
# st.snow()
# st.error('Error message')
# st.warning('Warning message')
# st.info('Info message')
# st.success('Success message')
# st.exception(e)