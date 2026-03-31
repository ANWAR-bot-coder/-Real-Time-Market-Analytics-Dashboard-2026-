import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

# 1. Page Setup
st.set_page_config(page_title="AI & DS Career Dashboard", layout="wide")
st.title("📊 Real-Time Market Analytics Dashboard (2026)")
st.markdown("Database-la irunthu live-ah data-va fetch panni analyze panrom machaa!")

# 2. SQL Database-la irunthu Data-va edukkarom
conn = sqlite3.connect('industry_market.db')
df = pd.read_sql('SELECT * FROM job_listings', conn)
conn.close()

# 3. Sidebar - User Access (Filters)
st.sidebar.header("User Filters")
city_filter = st.sidebar.multiselect("Select Cities", options=df['City'].unique(), default=df['City'].unique())
role_filter = st.sidebar.multiselect("Select Job Roles", options=df['Role'].unique(), default=df['Role'].unique())

# Filtering the data
filtered_df = df[(df['City'].isin(city_filter)) & (df['Role'].isin(role_filter))]

# 4. Key Metrics (Numbers that matter)
m1, m2, m3 = st.columns(3)
m1.metric("Total Jobs Found", len(filtered_df))
m2.metric("Avg Salary", f"{filtered_df['Salary_LPA'].mean():.1f} LPA")
m3.metric("Max Package", f"{filtered_df['Salary_LPA'].max()} LPA")

# 5. Interactive Chart (Plotly)
st.subheader("Salary Distribution Analysis")
fig = px.violin(filtered_df, y="Salary_LPA", x="Role", color="Role", box=True, points="all", hover_data=df.columns)
st.plotly_chart(fig, use_container_width=True)

# 6. Raw Data Table
if st.checkbox("Show Raw Data from SQL"):
    st.write(filtered_df)
