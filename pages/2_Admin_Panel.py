import streamlit as st

# Page setup
st.set_page_config(page_title="Admin Panel", layout="wide")
st.markdown("<h1 style='text-align: center;'>Admin Panel</h1>", unsafe_allow_html=True)

## [1 - Game Configuration]
st.markdown("### 🎮 Game Configuration")
session_freq = st.radio(
    "Session Frequency (Set game session prompts to employees):",
    options=["Daily", "Weekly", "Bi-Monthly", "Monthly"],
    horizontal=True
)

## [2 - User Management]
st.markdown("### 👥 User Management")

col1, col2 = st.columns([1, 1])
with col1:
    st.button("➕ Add User")
with col2:
    st.button("📁 Bulk Upload")

search_term = st.text_input("🔍 Search Users")

# Simulated user list (could be connected to a real database later)
users = [
    {"name": "Employee 1", "team": "QA", "active": True},
    {"name": "Employee 2", "team": "Design", "active": True},
    {"name": "Employee 3", "team": "Art", "active": False},
]

st.write("")

for user in users:
    if search_term.lower() in user["name"].lower():
        col1, col2 = st.columns([4, 1])
        with col1:
            status_icon = "✅" if user["active"] else "❌"
            st.markdown(f"{status_icon} {user['name']} - {user['team']}")
        with col2:
            action = "Deactivate" if user["active"] else "Reactivate"
            st.button(f"{action}", key=user["name"])

## [3 - Fatigue Threshold Configuration]
st.markdown("### ⚙️ Fatigue Threshold Configuration")

with st.form("threshold_form"):
    col1, col2, col3 = st.columns(3)
    with col1:
        low_min = st.number_input("Low (min)", value=0)
        low_max = st.number_input("Low (max)", value=39)
    with col2:
        med_min = st.number_input("Medium (min)", value=40)
        med_max = st.number_input("Medium (max)", value=70)
    with col3:
        high_min = st.number_input("High (min)", value=71)
        high_max = st.number_input("High (max)", value=100)

    st.markdown("")

    col_left, col_right = st.columns([1, 1])
    with col_left:
        save = st.form_submit_button("💾 Save Changes")
    with col_right:
        reset = st.form_submit_button("♻️ Reset Defaults")

    if save:
        st.success("Thresholds saved!")
    if reset:
        st.warning("Thresholds reset to defaults (0–39, 40–70, 71–100)")