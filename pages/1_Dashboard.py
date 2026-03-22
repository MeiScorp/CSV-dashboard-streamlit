import streamlit as st
import pandas as pd

st.title("📊 Dashboard")

if "df" not in st.session_state:
    st.warning("Please upload a CSV file on the main page.")
    st.stop()

df = st.session_state["df"]

tab1, tab2, tab3 = st.tabs(["📄 Data Preview", "🔍 Filters", "📈 Summary"])

# ---------------- TAB 1 ----------------
with tab1:
    st.subheader("Data Preview")
    st.dataframe(df, use_container_width=True)

# ---------------- TAB 2 ----------------
with tab2:
    st.subheader("Filters")

    col = st.selectbox("Select a column to filter", df.columns)
    filtered_df = df.copy()

    if df[col].dtype == "object":
        values = st.multiselect("Select values", df[col].unique())
        if values:
            filtered_df = df[df[col].isin(values)]
    else:
        min_val = float(df[col].min())
        max_val = float(df[col].max())
        rng = st.slider("Select range", min_val, max_val, (min_val, max_val))
        filtered_df = df[(df[col] >= rng[0]) & (df[col] <= rng[1])]

    st.write("Filtered Data:")
    st.dataframe(filtered_df, use_container_width=True)

# ---------------- TAB 3 ----------------
with tab3:
    st.subheader("Summary Statistics")
    st.write(df.describe())
