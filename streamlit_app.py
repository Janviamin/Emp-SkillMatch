import pandas as pd
import streamlit as st

# Load employee database (this acts as a backend database)
@st.cache_data
def load_employee_data():
    return pd.read_excel("employee_database.xlsx")

# Function to match employees
def match_employees(project_requirements, employee_data):
    matched_employees = []
    for _, proj in project_requirements.iterrows():
        dept_match = employee_data[employee_data["Department"] == proj["Department"]]
        skill_match = dept_match[dept_match["Technical Skill Set"].str.contains(proj["Technical Skill"], case=False, na=False)]
        matched_employees.append(skill_match)
    return pd.concat(matched_employees).drop_duplicates()

# Streamlit UI
st.title("Employee Matching System")
employee_data = load_employee_data()

uploaded_file = st.file_uploader("Upload Project Requirement File", type=["xlsx"])
if uploaded_file:
    project_requirements = pd.read_excel(uploaded_file)
    matched_employees = match_employees(project_requirements, employee_data)
    
    if not matched_employees.empty:
        st.write("### Suggested Employees")
        st.dataframe(matched_employees)
    else:
        st.write("No matching employees found.")
