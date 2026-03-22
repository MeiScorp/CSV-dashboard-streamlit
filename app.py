import streamlit as st
import pandas as pd

st.set_page_config(page_title="CSV Analyzer", layout="wide")

st.title("📊 CSV Analyzer")
st.write("Upload a CSV file to start exploring your data.")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.session_state["df"] = df
    st.success("File successfully loaded! Use the pages on the left to explore your data.")
else:
    st.info("Please upload a CSV file to continue.")
