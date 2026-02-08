import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle
# Load CSV file
df = pd.read_csv("Project/student_placement_anxiety_dataset.csv")
X = df[
    ['CGPA',
     'Internships',
     'Mock_Test_Score',
     'Coding_Hours_Per_Week',
     'Resume_Score']
]

y = df['Expected_Package_LPA']

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

with open("Project/package_prediction_model.pkl", "wb") as file:
    pickle.dump(model, file)
print("Model trained and saved as package_prediction_model.pkl")
