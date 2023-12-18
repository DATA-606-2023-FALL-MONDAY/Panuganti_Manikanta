# Import necessary libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from itertools import groupby
import gc
import pickle

def make_features(df):
    # parse the timestamp and create an "hour" feature
    df['timestamp'] = pd.to_datetime(df['timestamp'], utc=True)
    df['timestamp'] = df['timestamp'].dt.tz_localize(None)
    df["hour"] = df["timestamp"].dt.hour

    periods = 20
    df["anglez"] = abs(df["anglez"])
    df["anglez_diff"] = df.groupby('series_id')['anglez'].diff(periods=periods).fillna(method="bfill").astype('float16')
    df["enmo_diff"] = df.groupby('series_id')['enmo'].diff(periods=periods).fillna(method="bfill").astype('float16')
    df["anglez_rolling_mean"] = df["anglez"].rolling(periods,center=True).mean().fillna(method="bfill").fillna(method="ffill").astype('float16')
    df["enmo_rolling_mean"] = df["enmo"].rolling(periods,center=True).mean().fillna(method="bfill").fillna(method="ffill").astype('float16')
    df["anglez_rolling_max"] = df["anglez"].rolling(periods,center=True).max().fillna(method="bfill").fillna(method="ffill").astype('float16')
    df["enmo_rolling_max"] = df["enmo"].rolling(periods,center=True).max().fillna(method="bfill").fillna(method="ffill").astype('float16')
    df["anglez_rolling_std"] = df["anglez"].rolling(periods,center=True).std().fillna(method="bfill").fillna(method="ffill").astype('float16')
    df["enmo_rolling_std"] = df["enmo"].rolling(periods,center=True).std().fillna(method="bfill").fillna(method="ffill").astype('float16')
    df["anglez_diff_rolling_mean"] = df["anglez_diff"].rolling(periods,center=True).mean().fillna(method="bfill").fillna(method="ffill").astype('float16')
    df["enmo_diff_rolling_mean"] = df["enmo_diff"].rolling(periods,center=True).mean().fillna(method="bfill").fillna(method="ffill").astype('float16')
    df["anglez_diff_rolling_max"] = df["anglez_diff"].rolling(periods,center=True).max().fillna(method="bfill").fillna(method="ffill").astype('float16')
    df["enmo_diff_rolling_max"] = df["enmo_diff"].rolling(periods,center=True).max().fillna(method="bfill").fillna(method="ffill").astype('float16')

    return df

features = ["hour",
            "anglez",
            "anglez_rolling_mean",
            "anglez_rolling_max",
            "anglez_rolling_std",
            "anglez_diff",
            "anglez_diff_rolling_mean",
            "anglez_diff_rolling_max",
            "enmo",
            "enmo_rolling_mean",
            "enmo_rolling_max",
            "enmo_rolling_std",
            "enmo_diff",
            "enmo_diff_rolling_mean",
            "enmo_diff_rolling_max",
           ]


# Set the title of the web app
st.title("Sleep Tracking Dashboard")

# Upload CSV file through Streamlit
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

# Display data if file is uploaded
if uploaded_file is not None:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)
    # st.subheader("Raw Sleep Data")
    temp = df[(df['timestamp'] > '2017-11-09') & (df['timestamp'] < '2017-11-11')]
    # st.write(temp)


    
    test_df = make_features(temp)

    # Create a plot using Plotly Express
    fig = px.line(test_df, x='timestamp', y='awake', title='Sleep Tracking Plot Actual')
    
    # Display the plot
    st.plotly_chart(fig)
    st.write("awake 0 = sleeping")

    X_test = test_df[features]
    y_test = test_df['awake']

    filename = "model_2.sav"
    loaded_model = pickle.load(open(filename, 'rb'))
    print("Loaded sucesfully!!!")
    result = loaded_model.score(X_test, y_test)

    predicted_y_test = loaded_model.predict(X_test)
    test_df['awake'] = predicted_y_test

    # Convert the 'Time' column to datetime format
    # df['Time'] = pd.to_datetime(df['Time'])



    # test_df = test_df[(test_df['timestamp'] > '2017-11-09') & (test_df['timestamp'] < '2017-11-11')]


    fig2 = px.line(test_df, x='timestamp', y='awake', title='Sleep Tracking Plot Predicted')
    
    # Display the plot
    # st.subheader("Sleep Tracking Plot")
    st.plotly_chart(fig2)
    st.write("awake 0 = sleeping")


