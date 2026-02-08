import pickle
# Load placement classification model
with open("Project/placement_classifier.pkl", "rb") as file:
    placement_model = pickle.load(file)

# Load salary regression model
with open("Project/package_prediction_model.pkl", "rb") as file:
    salary_model = pickle.load(file)
print("Enter Student Details:")

cgpa = float(input("CGPA(?/10): "))
internships = int(input("Number of Internships: "))
mock_test = int(input("Mock Test Score: "))
coding_hours = int(input("Coding Hours per Week: "))
resume_score = int(input("Resume Score: "))
student_data = [[
    cgpa,
    internships,
    mock_test,
    coding_hours,
    resume_score
]]
placement_result = placement_model.predict(student_data)
if placement_result[0] == 1:
    placement_status = "PLACED"
else:
    placement_status = "NOT PLACED"
salary_prediction = salary_model.predict(student_data)
salary_lpa = salary_prediction[0]
print("\n--- Prediction Result ---")
print("Placement Status:", placement_status)
print("Expected Salary Package (LPA):", round(salary_lpa, 2))
