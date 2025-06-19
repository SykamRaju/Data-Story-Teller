import streamlit as st
import pandas as pd
import plotly.express as px
from storyteller import generate_story
from dotenv import load_dotenv
import os

load_dotenv()
st.set_page_config(page_title="Data Storyteller", layout="wide")
st.title("🚀 Indian Startup Funding: Auto Data Storytelling")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("data/StartupFunding.csv")

df.columns = df.columns.str.strip()
st.write("Column names:", df.columns.tolist())

st.subheader("🔍 Data Preview")
st.dataframe(df.head())

st.subheader("📊 Top Funded Cities")
fig = px.bar(df['CityLocation'].value_counts().head(10), labels={'value': 'Count'}, title="Top Cities")
st.plotly_chart(fig)

st.subheader("🏢 Popular Sectors")
fig2 = px.pie(df['IndustryVertical'].value_counts().head(5), names=df['IndustryVertical'].value_counts().head(5).index)
st.plotly_chart(fig2)

st.subheader("🤖 GPT-Generated Insight")
if st.button("Generate Insight"):
    with st.spinner("Thinking..."):
        story = generate_story(df)
        st.success("Here's your insight:")
        st.write(story)