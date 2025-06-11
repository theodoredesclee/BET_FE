import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import os
from pathlib import Path
import base64
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))
from src.config import image_logo

# This is the home page where age verification is done
# === Page config ===
st.set_page_config(
    page_title="Wine Order App",
    page_icon="🍷",
    layout="centered",
    initial_sidebar_state="auto"
)

# === Styling ===
st.markdown(
    """
    <style>
    .stApp {
        background-color: #F9F4EF;
        color: #4B2C2A;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# === Load and display logo ===


with open(image_logo, "rb") as f:
    encoded = base64.b64encode(f.read()).decode()

st.markdown(
    f"""
    <div style='text-align: center;'>
        <img src='data:image/png;base64,{encoded}' width='120'>
        <h1>🍷 Welcome to the Wine Order App</h1>
        <p style='font-size:18px;'>🔞 Are you at least 18 years old to enter this site?</p>
    </div>
    """,
    unsafe_allow_html=True
)

# === Session state init ===
if "age_verified" not in st.session_state:
    st.session_state.age_verified = None

# === Age verification buttons ===
col1, col2, col3 = st.columns([2, 2, 2])
with col1:
    _ = st.empty()
with col2:
    yes = st.button("✅ Yes, I am 18 or older", use_container_width=True)
with col3:
    no = st.button("❌ No, I am under 18", use_container_width=True)

# === Handle button clicks ===
if yes:
    st.session_state.age_verified = True
    st.switch_page("pages/welcome.py")

if no:
    st.session_state.age_verified = False
    st.switch_page("pages/restricted.py")

# === Handle reloads ===
if st.session_state.age_verified is True:
    st.switch_page("pages/welcome.py")
elif st.session_state.age_verified is False:
    st.switch_page("pages/restricted.py")
