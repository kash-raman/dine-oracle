# Libraries
import streamlit as st
from PIL import Image

# Confit
st.set_page_config(page_title='DineOracle', page_icon=':bar_chart:', layout='wide')

# Title
st.title('DineOracle - Predicting Restaurant Success with AI/ML')

# Content
c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14 = st.columns(14)
c1.image(Image.open('images/yelp-logo.png'))
 

st.write(
    """
    With the increasing competition in the restaurant industry, owners and operators are constantly seeking ways to improve their business performance and stay ahead of the curve. One approach that has gained significant attention in recent years is the use of artificial intelligence (AI) and machine learning (ML) to predict restaurant success. In this write-up, we will explore how AI/ML can be used to predict restaurant success and the benefits it offers.

AI/ML technology can analyze various data points such as demographics, social media engagement, online reviews, and sales data to provide valuable insights into customer behavior, preferences, and trends. By analyzing this data, restaurant owners can make informed decisions about menu offerings, marketing strategies, staffing, and even the location of the restaurant.

One example of how AI/ML can be used to predict restaurant success is through sentiment analysis. Sentiment analysis involves analyzing customer reviews and feedback on social media and review websites to determine the overall sentiment towards the restaurant. This analysis can provide insights into areas that need improvement, such as food quality, customer service, or ambiance, and help owners make necessary changes to improve their restaurant's reputation and increase customer satisfaction.

Another example is predictive modeling, which uses historical data to predict future trends and behaviors. By analyzing past sales data, restaurant owners can forecast future sales and adjust their menu offerings and staffing accordingly to meet demand.

AI/ML can also be used to optimize pricing strategies. By analyzing pricing trends and customer behavior, restaurant owners can determine the most effective pricing strategies to maximize profits and customer satisfaction. For example, dynamic pricing can be used to adjust prices based on demand, time of day, and other factors to optimize revenue.

The benefits of using AI/ML to predict restaurant success are significant. By making data-driven decisions, restaurant owners can improve their overall performance, reduce costs, and increase revenue. They can also improve customer satisfaction and loyalty by providing personalized experiences and menu offerings that meet their needs and preferences.

In conclusion, AI/ML technology offers valuable insights into customer behavior, preferences, and trends that can help restaurant owners make informed decisions and improve their overall performance. With the increasing competition in the restaurant industry, those who embrace this technology can gain a competitive advantage and ensure long-term success.
    """
)

st.subheader('Methodology')
st.write(
    """
    The data for this prediction model was selected from the  Yelp dataset (https://www.yelp.com/dataset)
    data platform by using its **REST API**.  
    [**GitHub Repository**](https://github.com/kash-raman/dine-oracle).

   Add verbiage here
    """
)

st.subheader('Future Works')
st.write(
    """
    TBD
    """
)

c1, c2, c3 = st.columns(3)
with c1:
    st.info('**Data Analyst: [@DataDazzlers](https://github.com/kash-raman/dine-oracle)**', icon="💡")
with c2:
    st.info('**GitHub: [@DataDazzlers](https://github.com/kash-raman/dine-oracle)**', icon="💻")
with c3:
    st.info('**Data: [@DataDazzlers](https://github.com/kash-raman/dine-oracle)**', icon="🧠")