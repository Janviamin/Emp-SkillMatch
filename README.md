
# Employee Matching System  
This project aims to develop a Python application that matches employees to project requirements based on their skills and department. It is designed to streamline the assignment of team members to projects by ensuring the right skills are matched with the right tasks.

## Features
Employee Skill Matching: Matches employees to projects based on their skillsets and departmental roles.  
Data Integration: Utilizes data from internal company resources and APIs to ensure accurate matching.  
Automation: Automatically recommends employees for specific projects, reducing manual effort.  
Weekly Dashboard: Provides a real-time dashboard tracking the status of employee matches and project assignments.  
## Project Structure
app.py: The main Python file for the employee matching application.
requirements.txt: A list of dependencies required for the project.
## Installation
Clone the repository:  

bash  
Copy code  
pip install -r requirements.txt  
Set up the virtual environment (if not already done):  

bash  
Copy code  
python -m venv venv  
source venv/bin/activate  # On Windows use venv\Scripts\activate  
Usage  
Run the employee matching application:  

bash  
Copy code  
python app.py  
View the weekly dashboard by navigating to:  

bash  
Copy code  
localhost:8501  # Streamlit app running locally 
Update the employee data by adding or editing records in the data/ folder.  
