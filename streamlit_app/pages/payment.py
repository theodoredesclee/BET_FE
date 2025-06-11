import streamlit as st
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

st.set_page_config(page_title="Payment", page_icon="💳")
st.title("💳 Payment")

# --- Protect this page ---
if 'order_confirmed' not in st.session_state or not st.session_state.order_confirmed:
    st.warning("Please confirm your order first.")
    st.stop()

if 'user_info' not in st.session_state:
    st.warning("Please enter your personal details first.")
    st.stop()

# --- Show total price ---
st.subheader("🧾 Order Total")
total = st.session_state.get("order_total", 0)
st.markdown(f"**Total to pay: ${total}**")

# --- Mock Payment Form ---
st.subheader("💳 Payment Information")
card_number = st.text_input("Card Number (mock)", max_chars=16)
expiry_date = st.text_input("Expiry Date (MM/YY)", max_chars=5)
cvv = st.text_input("CVV", type="password", max_chars=3)

# --- Confirm Payment ---
if st.button("Pay Now"):
    if all([card_number, expiry_date, cvv]):
        # For demo purposes, we'll accept any non-empty input
        st.session_state.payment_success = True

        # Optionally create a final_order object
        st.session_state.final_order = {
            "basket": st.session_state.basket,
            "user_info": st.session_state.user_info,
            "total": total,
            "payment_status": "Success"
        }

        st.success("✅ Payment processed successfully!")
        st.switch_page("pages/order_summary.py")
    else:
        st.error("❌ Please fill in all payment fields.")
