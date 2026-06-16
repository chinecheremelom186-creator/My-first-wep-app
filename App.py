import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# Set up the title of your app
st.title("🇳🇬 Entry & Citizenship Checker")
st.write("Please fill out the details below honestly.")

# 1. Create the input containers for personal info
full_name = st.text_input("Enter your Full Name:")
phone_number = st.text_input("Enter your Phone Number:")

# 2. Create the input containers for age
age = st.number_input("Enter your age:", min_value=0, max_value=120, value=0)

# If they are 18 or older, show the citizenship options and the logic
if age >= 18:
    st.success("You can enter!")
    
    citizen = st.selectbox("Are you a citizen of Nigeria?", options=["Select an option", "yes", "no"])
    
    if citizen == "yes":
        st.warning("You go cry, no worry 😭")
    elif citizen == "no":
        st.info("Na soft life you dey so 😎")
        
    # 3. Add a Submit Button (Only shows up once they pick a citizenship option)
    if citizen != "Select an option":
        if st.button("Submit My Answers to Chinechere 🚀"):
            # Validation: Make sure they didn't leave name or phone blank
            if not full_name or not phone_number:
                st.error("Please fill in your Name and Phone Number before submitting!")
            else:
                try:
                    # Direct connection to your specific Google Sheet link
                    sheet_url = "https://docs.google.com/spreadsheets/d/1TR0cJAINs8utyADQxpI3vNhtFvMAkJ34KW4AQeteIV0/edit?usp=drivesdk"
                    
                    # Connect the pipe
                    conn = st.connection("gsheets", type=GSheetsConnection)
                    
                    # Read whatever is already in the sheet first
                    existing_data = conn.read(spreadsheet=sheet_url, usecols=[0, 1, 2, 3])
                    
                    # Create a container holding all 4 data pieces matching your sheet columns
                    new_entry = pd.DataFrame([{
                        "Age": age, 
                        "Citizen": citizen,
                        "Name": full_name,
                        "Phone": phone_number
                    }])
                    
                    # Combine the old data with the new entry
                    updated_data = pd.concat([existing_data, new_entry], ignore_index=True)
                    
                    # Update the sheet live!
                    conn.create(spreadsheet=sheet_url, data=updated_data)
                    
                    st.balloons()
                    st.success("Sent successfully! Go check your Google Sheets app right now! 🎉")
                except Exception as e:
                    st.error("Connection error. Make sure your Google Sheet is set to 'Anyone with link can Edit'!")
                    
