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


# Page config
st.set_page_config(page_title="Match to Wine", layout="centered")

# === Initialize session ===
if "step" not in st.session_state:
    st.session_state.step = 1

if "answers" not in st.session_state:
    st.session_state.answers = {}

# === Step 1: Box-style selection ===
def step_1():
    st.markdown("<h2 style='text-align: center;'>🍷 What type of wine would you like?</h2>", unsafe_allow_html=True)

    wine_types = ["Red", "White", "Rosé"]

    # Initialize selection states
    if "wine_type_choices" not in st.session_state:
        st.session_state.wine_type_choices = {wt: False for wt in wine_types}

    # Create columns for even layout
    cols = st.columns(len(wine_types))

    for i, wine in enumerate(wine_types):
        selected = st.session_state.wine_type_choices[wine]

        # Define button style
        bg_color = "#f8eaff" if selected else "#ffffff"
        border_color = "#a020f0" if selected else "#cccccc"

        # Button-like markdown box
        if cols[i].button(wine, key=f"wine_{wine}", use_container_width=True):
            st.session_state.wine_type_choices[wine] = not selected  # toggle

        # Style box using HTML only
        cols[i].markdown(
            f"""
            <style>
            div[data-testid="column"] div:has(button#{'wine_' + wine.replace(' ', '_')}) {{
                border: 2px solid {border_color};
                background-color: {bg_color};
                border-radius: 12px;
                padding: 16px;
                text-align: center;
                font-weight: bold;
                color: #333;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

    # Navigation
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Next"):
            selected_types = [wt for wt, selected in st.session_state.wine_type_choices.items() if selected]
            st.session_state.answers["wine_type"] = selected_types
            st.session_state.step = 2

# === Step 2 placeholder ===
def step_2():
    st.markdown("<h2 style='text-align: center;'>Step 2 coming soon...</h2>", unsafe_allow_html=True)
    if st.button("⬅️ Back"):
        st.session_state.step = 1

# === Render correct step ===
if st.session_state.step == 1:
    step_1()
elif st.session_state.step == 2:
    step_2()
