import streamlit as st
import pandas as pd

st.title("API Attack Logs")
df = pd.read_csv("logs/attacks.csv", names=["Time", "IP", "URL", "Type"])
st.dataframe(df)
st.bar_chart(df["Type"].value_counts())
