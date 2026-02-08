# 🎓 Student Placement & Salary Prediction App
A full-stack Machine Learning web application built with Streamlit, Scikit-Learn, and SQLite that predicts:
- 📌 Student Placement Status (Classification)
- 💰 Expected Salary Package (Regression)

The application also includes a secure authentication system with hashed passwords and user session management.

## 🌟 About

This project is designed to help students predict their chances of getting placed in companies and estimate their expected salary (LPA) based on various academic and personal metrics.
It combines machine learning models with a Streamlit interactive UI for a smooth user experience.

## 🚀 Live Demo
use these login credentials
- email: 123@gmail.com
- pass: 12345678

https://placement-predictor-app.streamlit.app/

## ✅ Features

- Student Login & Signup – Secure authentication using SQLite.
- Placement Prediction – Binary classification (Placed / Not Placed).
- Salary Prediction – Regression predicting expected salary.
- Interactive UI – User-friendly Streamlit app.
- Dual Functionality – Both classification & regression models integrated.

## 🛠 Tech Stack

- Python 3.10+
- Streamlit – Frontend and deployment
- scikit-learn – Machine learning
- pandas & numpy – Data handling
- matplotlib & seaborn – Visualization
- SQLite – Database for user authentication
- pickle – Model serialization

## 📊 Dataset

Features include:
Academic Metrics: CGPA, grades, internships, projects
Personal Metrics: Age, gender, skill scores
Target variables:
Placement Status: Placed / Not Placed
Expected Salary (LPA)
⚠️ Dataset cleaning, scaling, and encoding were performed before training.

## 🧠 How It Works

- Data Preprocessing – Handle missing values, encode categorical variables, scale numerical features.
- Model Training – Two models trained:
- Placement Classifier: Logistic Regression / Random Forest / XGBoost
- Salary Regressor: Linear Regression / Random Forest Regressor
- Model Deployment – Models serialized with pickle and integrated into Streamlit app.
- Prediction – User enters data → app returns placement status & expected salary.

## 🖼 Screenshots

Login Page:
<img width="1919" height="927" alt="image" src="https://github.com/user-attachments/assets/ed25f29b-3290-4eeb-b35f-c178a2f14b34" />


Placement & Salary Prediction Page:
<img width="1914" height="921" alt="image" src="https://github.com/user-attachments/assets/d98b6e72-991c-4f7d-82a0-be43e8b05844" />



## ⚡ Installation & Usage

Clone the repository:

git clone https://github.com/92haroonkhalid/placement-predictor.git
cd placement-predictor


Create a virtual environment:

python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows


Install dependencies:

pip install -r requirements.txt


Run the app:

streamlit run app.py


Open the URL displayed (usually http://localhost:8501) in your browser.

## 📈 Model Performance
- Placement Classifier: Accuracy: 0.9
LPA classifier
- Mean Squared Error (MSE): 8.77
- Mean Absolute Error (MAE): 2.66
- R² Score: -0.17

## 🚀 Future Enhancements
- Add automated testing for prediction functions.
- Include data visualization dashboard for insights.
- Improve UI/UX design and interactive elements.
- Deploy using Docker / cloud hosting for production-ready access.

## 🤝 Contributing
- Fork the repo
- Create a feature branch (git checkout -b feature-name)
- Commit your changes (git commit -m "Add new feature")
- Push to the branch (git push origin feature-name)
- Create a Pull Request

# 👨‍💻 Author
Haroon Khalid
