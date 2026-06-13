import streamlit as st

st.title("🇳🇬 Entry & Citizenship Checker")
st.write("Let's check your eligibility status.")

age = st.number_input("Enter your age:", min_value=0, max_value=120, value=0)

if age >= 18:
    st.success("You can enter!")
    
    citizen = st.selectbox(
        "Are you a citizen of Nigeria?",
        options=["Select an option", "yes", "no"]
    )
    
    if citizen == "yes":
        st.warning("You go cry, no worry 😭")
    elif citizen == "no":
        st.info("Na soft life you dey so 😎")

elif age > 0 and age < 18:
    st.error("Go and read your book! 📚")
