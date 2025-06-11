import requests
import streamlit as st
import os
import sys
from pathlib import Path
import json
sys.path.append(str(Path(__file__).resolve().parents[1]))
from src.api.backend.order_summary_backend import generate_order_summary

st.set_page_config(page_title="Order Summary", page_icon="✅")
st.title("✅ Order Confirmation")

# --- Block access if payment not completed ---
if 'payment_success' not in st.session_state or not st.session_state.payment_success:
    st.warning("Payment not completed. Please go back and finish checkout.")
    st.stop()

if 'final_order' not in st.session_state:
    st.warning("No order found.")
    st.stop()

order = st.session_state.final_order
basket = order["basket"]
user = order["user_info"]
total = order["total"]

# --- Show Order Summary ---
summary = generate_order_summary(basket, user, total)

st.subheader("🛍️ Items Ordered")
for line in summary["items"]:
    st.write(line)

st.markdown(f"### 🧾 Total Paid: **{summary['total']}**")

# --- Show Shipping Info ---
st.subheader("📦 Shipping To")
st.markdown(f"**{summary['shipping_info']['name']}**")
st.markdown(summary["shipping_info"]["address"])
st.markdown(f"📧 {summary['shipping_info']['contact']}")
if summary["shipping_info"]["note"]:
    st.markdown(f"📝 _Note: {summary['shipping_info']['note']}_")

st.success("Thank you for your order! A confirmation email will be sent shortly.")



# --- Save Order to dict ---


def save_order_to_dict(basket):
    sale_dict = {}
    sale_dict['name'] = []
    sale_dict['Count'] = []
    for i in range(len(basket)):
        sale_dict['name'].append(basket[i]['name'])
        sale_dict['Count'].append(basket[i]['quantity'])
    print(sale_dict)
    return sale_dict

basket = save_order_to_dict(basket)

st.write(basket)
requests.post('http://127.0.0.1:8000/new_orders' , json =basket)

#save_orders_dict(basket, ORDERS_PATH)

# --- Optionally clear session to start fresh ---
if st.button("🛍️ Back to Shop"):
    st.session_state.basket = []
    st.session_state.order_confirmed = False
    st.session_state.user_info = None
    st.session_state.payment_success = False
    st.session_state.final_order = None
    st.switch_page("pages/welcome.py")
