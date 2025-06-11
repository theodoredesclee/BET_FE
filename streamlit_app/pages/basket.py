import streamlit as st
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

st.set_page_config(page_title="Your Basket", page_icon="🧺")

# Initialize basket if not already present
if 'basket' not in st.session_state:
    st.session_state.basket = []

st.title("🧺 Your Basket")

# Show basket items
if st.session_state.basket:
    total = 0
    items_to_remove = []

    for i, item in enumerate(st.session_state.basket):
        col1, col2, col3 = st.columns([3, 1, 1])
        with col1:
            st.write(f"**{item['name']}** — ${item['price']}")
        with col2:
            st.write(f"Qty: {item.get('quantity', 1)}")
        with col3:
            if st.button("❌ Remove", key=f"remove_{i}"):
                items_to_remove.append(i)
        total += item['price'] * item.get('quantity', 1)

    # Remove selected items
    for idx in sorted(items_to_remove, reverse=True):
        st.session_state.basket.pop(idx)
        st.success("Item removed!")

    st.markdown(f"### 🧾 Total: **${total}**")

    # Checkout button
    if st.button("🛒 Proceed to Checkout"):
        st.switch_page("pages/products_summary.py")

else:
    st.info("Your basket is currently empty.")
    if st.button("🔙 Back to Sommelier Chatbot"):
        st.switch_page("pages/sommelier_final.py")  # ✅ Only the filename, if inside /pages
