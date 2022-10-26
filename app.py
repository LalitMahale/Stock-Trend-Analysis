import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import pandas_datareader as data
#from keras.models import load_model

st.title("Stock Trend Prediction")



stock_name = st.text_input("Enter Stock Title","SBIN")

start = st.date_input("Start Date")#"2010-01-01"
end = st.date_input("End Date")# "2022-10-25"
st.subheader("Data From {} - {}".format(start,end))
df = data.DataReader((stock_name+".NS"),"yahoo",start,end)


# # Describe data
#st.write(df.describe())

# Visualizations
st.subheader("closing Price vs Time Chart")
fig = plt.figure(figsize = (12,6))
plt.plot(df.Close)
st.pyplot(fig)

st.subheader("closing Price vs Time Chart With 100MA")
ma = df.Close.rolling(100).mean()
fig = plt.figure(figsize = (12,6))
plt.plot(ma)
plt.plot(df.Close)
st.pyplot(fig)

st.subheader("closing Price vs Time Chart With 100MA and 200MA")
ma = df.Close.rolling(100).mean()
ma1 = df.Close.rolling(200).mean()
fig = plt.figure(figsize = (12,6))
plt.plot(ma,"r")
plt.plot(ma1,"g")
plt.plot(df.Close,"b")
st.pyplot(fig)

