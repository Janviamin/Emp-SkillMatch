import streamlit as st

# Streamlit UI
st.title("Employee Matching System")

uploaded_file = st.file_uploader("Upload Project Requirement File", type=["xlsx"])
if uploaded_file:
    st.write("File uploaded successfully!")
