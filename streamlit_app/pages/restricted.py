import streamlit as st

st.set_page_config(page_title="Access Denied", layout="centered")

# === Styling ===
st.markdown("""
    <style>
    .stApp {
        background-color: #FFF0F0;
        color: #990000;
    }
    .block {
        text-align: center;
        padding: 100px 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Optional: don't allow reset
# Don't delete st.session_state["age_verified"]

st.markdown("""
<div class="block">
    <h1>🚫 Access Denied</h1>
    <p>You must be at least 18 years old to access this application.</p>
    <p>Please come back when you're of legal age 🍷</p>
</div>
""", unsafe_allow_html=True)
