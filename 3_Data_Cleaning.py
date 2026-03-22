import streamlit as st
import pandas as pd

st.title("🧹 Data Cleaning")

if "df" not in st.session_state:
    st.warning("Please upload a CSV file on the main page.")
    st.stop()

df = st.session_state["df"]

tab1, tab2, tab3 = st.tabs(["Edit Data", "Missing Values", "Download"])

# ---------------- EDITOR ----------------
with tab1:
    st.subheader("Editable Table")
    edited_df = st.data_editor(df, use_container_width=True)
    st.session_state["df"] = edited_df

# ---------------- MISSING VALUES ----------------
with tab2:
    st.subheader("Missing Values")

    st.write("Total missing values:", df.isna().sum().sum())
    st.write(df.isna().sum())

    if st.button("Fill missing values with 0"):
        df = df.fillna(0)
        st.session_state["df"] = df
        st.success("Missing values filled!")

    if st.button("Drop rows with missing values"):
        df = df.dropna()
        st.session_state["df"] = df
        st.success("Rows with missing values removed!")

# ---------------- DOWNLOAD ----------------
with tab3:
    st.subheader("Download Edited CSV")

    csv = df.to_csv(index=False)

    st.download_button(
        "Download CSV",
        data=csv,
        file_name="cleaned_data.csv",
        mime="text/csv"
    )
