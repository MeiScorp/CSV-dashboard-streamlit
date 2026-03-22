import streamlit as st
import altair as alt
import pandas as pd

st.title("📈 Charts")

# Check if data exists
if "df" not in st.session_state:
    st.warning("Please upload a CSV file on the main page.")
    st.stop()

df = st.session_state["df"].copy()

# Reset index so we can use it as a column
df = df.reset_index().rename(columns={"index": "RowIndex"})

numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns

if len(numeric_cols) < 1:
    st.info("No numeric columns available for charts.")
    st.stop()

tab1, tab2, tab3, tab4 = st.tabs(["Scatter Plot", "Histogram", "Bar Chart", "Line Chart"])

# ---------------- SCATTER ----------------
with tab1:
    st.subheader("Scatter Plot")

    x = st.selectbox("X-axis", df.columns)
    y = st.selectbox("Y-axis", numeric_cols)

    chart = (
        alt.Chart(df)
        .mark_circle(size=60)
        .encode(x=x, y=y, tooltip=list(df.columns))
        .interactive()
    )

    st.altair_chart(chart, use_container_width=True)

# ---------------- HISTOGRAM ----------------
with tab2:
    st.subheader("Histogram")

    col = st.selectbox("Select numeric column", numeric_cols)

    chart = (
        alt.Chart(df)
        .mark_bar()
        .encode(alt.X(col, bin=True), y="count()")
    )

    st.altair_chart(chart, use_container_width=True)

# ---------------- BAR CHART ----------------
with tab3:
    st.subheader("Bar Chart")

    col = st.selectbox("Select numeric column for bar chart", numeric_cols)

    chart = (
        alt.Chart(df)
        .mark_bar()
        .encode(x=col, y="count()")
    )

    st.altair_chart(chart, use_container_width=True)

# ---------------- LINE CHART ----------------
with tab4:
    st.subheader("Line Chart")

    x = st.selectbox("X-axis (choose any column)", df.columns)
    y = st.selectbox("Y-axis (numeric only)", numeric_cols)

    chart = (
        alt.Chart(df)
        .mark_line()
        .encode(x=x, y=y)
    )

    st.altair_chart(chart, use_container_width=True)
