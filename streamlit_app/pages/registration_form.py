import streamlit as st

st.set_page_config(page_title="Your Details", page_icon="📝")
st.title("📝 Registration Form")

# --- Block access if no confirmed order ---
if 'order_confirmed' not in st.session_state or not st.session_state.order_confirmed:
    st.warning("Please confirm your order first.")
    st.stop()

# --- Personal Information ---
st.subheader("👤 Personal Information")
first_name = st.text_input("First Name *")
last_name = st.text_input("Last Name *")
email = st.text_input("Email Address *")
phone = st.text_input("Phone Number *")

# --- Optional Info ---
optional_info = st.text_area("Additional Notes (optional)")

# --- Address Section ---
st.subheader("🏠 Address Information")
street = st.text_input("Street and Number *")

col1, col2 = st.columns([1, 2])
with col1:
    zip_code = st.text_input("ZIP Code *")
with col2:
    city = st.text_input("City *")

country = st.text_input("Country *")

# --- Submit Button ---
if st.button("Continue to Payment"):
    required_fields = [first_name, last_name, email, phone, street, zip_code, city, country]
    if all(required_fields):
        # ✅ Store info
        st.session_state.user_info = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "phone": phone,
            "notes": optional_info,
            "street": street,
            "zip_code": zip_code,
            "city": city,
            "country": country
        }

        st.success("Form submitted successfully ✅")
        st.switch_page("pages/payment.py")
    else:
        st.error("❌ Please fill in all required fields marked with *.")
