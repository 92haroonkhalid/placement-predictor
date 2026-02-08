## 🎓 Student Placement & Salary Prediction App
A full-stack Machine Learning web application built with Streamlit, Scikit-Learn, and SQLite that predicts:
- 📌 Student Placement Status (Classification)
- 💰 Expected Salary Package (Regression)
The application also includes a secure authentication system with hashed passwords and user session management.

# 🚀 Live Demo
(Add your Streamlit Cloud link here after deployment)

# 🧠 Features
- 🔐 Secure User Registration & Login (SHA256 password hashing)
- 🆔 Unique UUID-based user IDs
- 📊 Placement Prediction using ML Classification
- 💵 Salary Prediction using ML Regression
- 💾 SQLite Database Integration
- 🎨 Interactive and Clean Streamlit UI
- ⚡ Session State Authentication Handling

# 🛠️ Tech Stack
- Python
- Streamlit
- Scikit-learn
- SQLite3
- Hashlib (Security)
- UUID
- Pickle

# 📂 Project Structure
placement-predictor/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── models/
│   ├── placement_classifier.pkl
│   └── package_prediction_model.pkl
│
├── database/
│   └── users.db (auto-created)
│
└── data/
    └── dataset.csv

# ⚙️ Installation & Setup
Clone the repository:
git clone https://github.com/yourusername/placement-predictor.git
cd placement-predictor

Install dependencies:
pip install -r requirements.txt

Run the application:
streamlit run app.py

# 🔐 Authentication System
- Passwords are hashed using SHA256 before storing.
- Unique UUID is generated for each user.
- SQLite used for lightweight database storage.

# 📈 Machine Learning Models
- Classification Model → Predicts whether student will be placed.
- Regression Model → Predicts expected salary package (LPA).
- Models are loaded using pickle.

## 👨‍💻 Author
Haroon Khalid
