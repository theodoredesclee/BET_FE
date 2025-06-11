import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import os, base64
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))
from src.config import image_logo

# This is the page to decide wether to use the chatbot or the matching tool

# === Set page config ===
st.set_page_config(page_title="Wine Ordering App", layout="centered")
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
# === Load and encode image ===
#project_root = os.path.abspath('/Users/theodoredesclee/code/ecotrini/BET')
image_path = image_logo

image = Image.open(image_path).resize((120, 120))

with open(image_path, "rb") as f:
    data = f.read()
    encoded = base64.b64encode(data).decode()

# === Display centered image ===
st.markdown(
    f"""
    <div style="text-align: center;">
        <img src="data:image/png;base64,{encoded}" width="120">
    </div>
    """,
    unsafe_allow_html=True
)

# === Display centered title and description ===
st.markdown("<h1 style='text-align: center;'>🍇 Wine Ordering App</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Welcome to the wine shop! Browse and order your favorites.</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Choose what you want to do:</p>", unsafe_allow_html=True)

# === Centered buttons using columns ===
col1, col2, col3, col4, col5 = st.columns([1, 2, 1, 2, 1])

with col2:
    if st.button("🔍 Talk to our Sommelier", use_container_width=True):
        st.switch_page("pages/sommelier_final.py")

with col4:
    if st.button("🍽️ Match to Wine", use_container_width=True):
        st.switch_page("pages/match.py")
