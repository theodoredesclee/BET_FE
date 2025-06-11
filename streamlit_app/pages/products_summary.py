import streamlit as st

st.set_page_config(page_title="Checkout Summary", page_icon="🧾")

st.title("🧾 Checkout Summary")

# ✅ Prevent direct access without a basket
if 'basket' not in st.session_state or not st.session_state.basket:
    st.warning("Your basket is empty.")
    st.stop()

# ✅ Show the order summary
total = 0
st.subheader("Your Items")
for item in st.session_state.basket:
    qty = item.get('quantity', 1)
    st.write(f"- {item['name']} — ${item['price']} x {qty}")
    total += item['price'] * qty

st.markdown(f"### 💵 Total: **${total}**")

# ✅ Confirm and go to registration_form.py
if st.button("✅ Confirm Order"):
    st.session_state.order_confirmed = True
    st.session_state.order_total = total
    st.switch_page("pages/registration_form.py")
