import re
import json
import os
import pandas as pd
import streamlit as st
import google.generativeai as genai
from difflib import get_close_matches
import sys
import requests
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))



st.set_page_config(page_title="Prediction Automation", layout="centered")
st.markdown("""
    <style>
    .stApp { background-color: #F9F4EF; color: #4B2C2A; }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    .top-centered-box {
        display: flex;
        justify-content: center;
        text-align: center;
        flex-direction: column;
        margin-top: 30px;
    }
    </style>
    <div class="top-centered-box">
        <h2>Prediction Automation Metrics</h2>
        <p>Welcome</p>
    </div>
""", unsafe_allow_html=True)

# Manual Run button
if st.button("Manual Run"):
    st.write("Manual process started...")

    # Run the POST request to your FastAPI endpoint
    try:
        response = requests.get('http://127.0.0.1:8000/run_metrics')
        if response.status_code == 200:
            st.success("Manual run completed successfully!")
        else:
            st.error(f"Failed to run metrics: {response.status_code}")
    except Exception as e:
        st.error(f"Error while making request: {e}")

days = st.number_input("Days", min_value=0, value=0)
hours = st.number_input("Hours", min_value=0, max_value=23, value=0)
minutes = st.number_input("Minutes", min_value=0, max_value=59, value=0)
seconds = st.number_input("Seconds", min_value=0, max_value=59, value=0)

# Schedule button
if st.button("Schedule"):
    total_seconds = (
        days * 86400 +
        hours * 3600 +
        minutes * 60 +
        seconds
    )
    st.success(f"Task scheduled to run every {total_seconds} seconds.")
