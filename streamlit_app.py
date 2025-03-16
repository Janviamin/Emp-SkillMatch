import pandas as pd
import streamlit as st

# Load employee database (this acts as a backend database)
@st.cache_data
def load_employee_data():
    return pd.read_excel("employee_database.xlsx")

# Function to calculate match percentage
def calculate_match_percentage(employee_skills, required_skills):
    employee_skills_set = set(employee_skills.lower().split(','))
    required_skills_set = set(required_skills.lower().split(','))
    match_count = len(employee_skills_set & required_skills_set)
    return (match_count / len(required_skills_set)) * 100 if required_skills_set else 0

# Function to match employees
def match_employees(project_requirements, employee_data):
    matched_employees = []
    for _, proj in project_requirements.iterrows():
        dept_match = employee_data[employee_data["Department"] == proj["Department"]]
        dept_match = dept_match.copy()
        dept_match["Match Percentage"] = dept_match["Technical Skill Set"].apply(lambda x: calculate_match_percentage(x, proj["Technical Skill"]))
        skill_match = dept_match[dept_match["Match Percentage"] > 0]
        matched_employees.append(skill_match)
    return pd.concat(matched_employees).drop_duplicates().sort_values(by="Match Percentage", ascending=False)

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
        
        # Option to download results
        st.download_button(
            label="Download Results",
            data=matched_employees.to_csv(index=False).encode("utf-8"),
            file_name="matched_employees.csv",
            mime="text/csv"
        )
    else:
        st.write("No matching employees found.")
