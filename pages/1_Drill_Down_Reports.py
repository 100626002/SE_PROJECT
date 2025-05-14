import streamlit as st
import pandas as pd
import random

# Page Setup
st.set_page_config(page_title="Drill-Down Reports", layout="wide")
st.markdown("<h1 style='text-align: center;'>Drill-Down Reports</h1>", unsafe_allow_html=True)

## [1 - Dropdown Filters]
team = st.selectbox("Select Team", ["QA", "Design", "Engineering", "Art"])
range_choice = st.selectbox("Select Date Range", ["Day", "Week", "Month"])

st.write(f"📊 Showing report details for **{team}** over **{range_choice}**.")

## [2 - Fatigue Risk Ratings]
st.markdown("<h3>Fatigue Risk Ratings</h3>", unsafe_allow_html=True)
st.caption("Individual employees are anonymised")

# Simulate risk counts
high_risk = random.randint(1, 3)
medium_risk = random.randint(2, 5)
low_risk = random.randint(3, 7)

st.markdown(f"- 🔴 **{high_risk}** employees are High Risk!")
st.markdown(f"- 🟠 **{medium_risk}** employees are Medium Risk")
st.markdown(f"- 🟢 **{low_risk}** employees are Low Risk")

## [3 - Performance Metrics Summary]
st.markdown("<h3>Performance Metrics Summary</h3>", unsafe_allow_html=True)

avg_reaction_time = round(random.uniform(200, 400), 1)
avg_accuracy = random.randint(85, 100)
avg_errors = random.randint(0, 5)
avg_completion = f"{random.randint(30, 120)} seconds"

st.markdown(f"- ⏱️ Average Reaction Time: **{avg_reaction_time}ms**")
st.markdown(f"- 🎯 Average Accuracy: **{avg_accuracy}%**")
st.markdown(f"- ❌ Average Errors Made: **{avg_errors}**")
st.markdown(f"- ⏳ Average Completion Time: **{avg_completion}**")

## [4 - Export Report]
st.subheader("📥 Export Report")

# Simulated export content
export_df = pd.DataFrame({
    "Metric": ["Reaction Time", "Accuracy", "Errors", "Completion Time"],
    "Value": [f"{avg_reaction_time}ms", f"{avg_accuracy}%", avg_errors, avg_completion]
})

csv = export_df.to_csv(index=False).encode('utf-8')

st.download_button(
    label="⬇️ Export Drill-Down Report",
    data=csv, 
    file_name='drill_down_report.csv',
    mime='text/csv'
)