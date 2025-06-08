import streamlit as st
st.title('Hello Ariska!')
st.header('Welcome to My Data Analytics App')

check_on = st.checkbox('Check me!')
if check_on :
    st.write('Check Box is Checked')

name = st.text_input('Enter Your Name')
if name :
    st.write(f'Hello {name}!')

import pandas as pd
data = pd.read_csv('iris_data.csv')

import plotly.express as px
fig = px.scatter(data, x="SepalLengthCm", y="SepalWidthCm", color="Species")
st.plotly_chart(fig, use_container_width=True)
