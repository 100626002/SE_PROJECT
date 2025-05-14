import streamlit as st
import pandas as pd
import altair as alt
import random

# Page Setup
st.set_page_config(page_title="Team Fatigue Dashboard", layout="wide")
st.markdown("<h1 style='text-align: center;'>Team Fatigue Overview</h1>", unsafe_allow_html=True)

## [1 - Dropdown Filters]
team = st.selectbox("Select Team", ["QA", "Design", "Engineering", "Art"])
range_choice = st.selectbox("Select Date Range", ["Day", "Week", "Month"])

# Display result
st.write(f"🔍 Showing fatigue data for **{team}** over **{range_choice}**.")

## [2 - SIMULATED Average Fatigue Score, Bar Graph]
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
fatigue_scores = [random.randint(0, 100) for _ in days_of_week] 

# DataFrame for data
fatigue_data = pd.DataFrame({
    "Day": days_of_week,
    "Fatigue Score": fatigue_scores
})

# Creating a bar chart using Altair
day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
bar_chart = alt.Chart(fatigue_data).mark_bar().encode(

    x=alt.X("Day:N", sort=day_order),
    y="Fatigue Score",
    color=alt.Color(
        "Fatigue Score:Q",
        scale=alt.Scale(domain=[0, 100], range=["limegreen", "red"]),
        legend=None
    )
).properties(
    title=f"Average Fatigue Score for {team} - {range_choice.capitalize()}"
)

# Displaying bar in Streamlit
st.altair_chart(bar_chart, use_container_width=True)

## [3 - Alerts]
st.subheader("⚠️ Alerts")

# Define fatigue threshold
threshold = 70

# Count how many employees exceed the threshold (we'll simulate 10 employees for now)
fatigued_employees = sum(score > threshold for score in fatigue_scores)

# Simulate a random "rising trend" (placeholder)
import random
rising_trend = random.choice([True, False])

# Display alert summaries
st.markdown(f"- **{fatigued_employees} employees** have exceeded the fatigue threshold!")
st.markdown(f"- **{'1' if rising_trend else '0'} team** has a rising fatigue trend!")

## [4 - Fatigue Trend Heatmap]
st.subheader("📊 Fatigue Trend Heatmap")

# Teams & Days
teams = ["QA", "Design", "Engineering", "Art"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# DataFrame for heatmap: 1 row per (team, day) pair
heatmap_data = pd.DataFrame([
    {"Team": team, "Day": day, "Fatigue Score": random.randint(0, 100)}
    for team in teams
    for day in days
])

# Creating heatmap chart
day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
heatmap = alt.Chart(heatmap_data).mark_rect().encode(
    
    x=alt.X("Day:N", sort=day_order),
    y=alt.Y("Team:N"),
    color=alt.Color(
        "Fatigue Score:Q",
        scale=alt.Scale(scheme="redyellowgreen", reverse=True),
        legend=None
    ),
    tooltip=["Team", "Day", "Fatigue Score"]
).properties(
    width=700,
    height=300
)

# Show chart
st.altair_chart(heatmap, use_container_width=True)

## [5 - Export Report]

st.subheader("📥 Export Report")

# Combining all data into a single DataFrame to export
export_df = pd.DataFrame({
    "Team": [team for team in teams for _ in days],
    "Day": days * len(teams),
    "Fatigue Score": heatmap_data["Fatigue Score"]
})

# Create CSV and make it downloadable
csv = export_df.to_csv(index=False).encode('utf-8')

st.download_button(
    label="⬇️ Export Weekly Fatigue Report",
    data=csv,
    file_name='fatigue_report.csv',
    mime='text/csv'
)
