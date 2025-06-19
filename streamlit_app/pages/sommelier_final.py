import re
import requests
import os
import pandas as pd
import streamlit as st
import google.generativeai as genai
from difflib import get_close_matches
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.front_end_fct import load_wine_inventory, load_serge


# --- Setup ---
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

wine_df = load_wine_inventory()
BOT_AVATAR = load_serge()

st.set_page_config(page_title="Sommelier Chatbot", layout="centered")
st.markdown("""
    <style>
    .stApp { background-color: #F9F4EF; color: #4B2C2A; }
    </style>
""", unsafe_allow_html=True)

# --- Session States ---
if "basket" not in st.session_state:
    st.session_state.basket = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "latest_suggestions" not in st.session_state:
    st.session_state.latest_suggestions = []

# --- Recommender Class ---


# --- Display Welcome ---
if len(st.session_state.chat_history) == 0:
    st.markdown("""
        <style>
        .centered-box {
            height: 75vh;
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            flex-direction: column;
        }
        </style>
        <div class="centered-box">
            <h2>🍷 Meet Serge</h2>
            <h3>Your Personal Sommelier</h2>""", unsafe_allow_html=True)
    st.image(BOT_AVATAR, width=150)
    st.markdown("""
            <p>Hey! Ask me what kind of wine you're looking for.</p>
        </div>
    """, unsafe_allow_html=True)

# --- Show Chat Header and History ---
if len(st.session_state.chat_history) > 0:
    st.markdown("<h1 style='text-align: center;'>🍷 Serge the Sommelier</h1>", unsafe_allow_html=True)
    for role, msg in st.session_state.chat_history:
        if role == "user":
            with st.chat_message("user"):
                st.markdown(msg)
        else:
            with st.chat_message("assistant", avatar=BOT_AVATAR):
                st.markdown(msg)

# --- User Input ---
user_input = st.chat_input("What kind of wine are you looking for?")
#params = "userinputtext"
#request.get("/chatendpoint", params = params)
if user_input:
    st.session_state.chat_history.append(("user", user_input))

    # Send user input to FastAPI backend
    api_url = "https://app-289249351425.europe-west1.run.app/recommend"  # Change if deployed elsewhere
    payload = {
        "customer_description": user_input,
        "chat_history": st.session_state.chat_history
    }
    try:
        r = requests.post(api_url, json=payload)
        if r.status_code == 200:
            data = r.json()
            response_text = data.get("recommendations", "No recommendations found.")
            suggestions = data.get("suggestions", [])
        else:
            response_text= "Sorry, there was an error with the recommendation service."
            suggestions = []
    except Exception as e:
        response_text = f"Error contacting the API: {e}"
        suggestions = []

    #recommender = WineRecommender(wine_df)
    #response_text = recommender.get_recommendations(user_input, st.session_state.chat_history)
    #suggestions = recommender.extract_wine_matches(response_text)

    # Save suggestions and show message
    st.session_state.latest_suggestions = suggestions
    st.session_state.chat_history.append(("assistant", response_text))
    st.rerun()

# --- Show Latest Suggestions with Add Buttons ---
if st.session_state.get("latest_suggestions"):
    st.markdown("---")
    st.subheader("🍷 Suggested Wines")

    for i, wine in enumerate(st.session_state.latest_suggestions):
        col1, col2 = st.columns([4, 1])
        with col1:
            st.markdown(f"**{wine['WineName']}**  \nRating: {wine['Rating']} | In Stock: {wine['Count']} | Price: €{wine['Price']}")
        with col2:
            if st.button("🛒 Add", key=f"add_{i}"):
                st.session_state.basket.append({
                    "name": wine["WineName"],
                    "price": wine["Price"],
                    "quantity": 1
                })
                st.success(f"{wine['WineName']} added to your basket!")

# --- Basket Button ---
if st.button("🧺 View Basket"):
    st.switch_page("pages/basket.py")
