import streamlit as st
import pickle
import sqlite3
import hashlib
import uuid

con = sqlite3.connect("database/users.db")
pul = con.cursor()
pul.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    uid TEXT NOT NULL,
    username TEXT UNIQUE NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
)
""")
con.commit()
con.close()

def hash_pass(password):
    return hashlib.sha256(password.encode()).hexdigest() #

def gen_uid():
    return str(uuid.uuid4())[:8]

# acha yha registration ho rhee ha ok. and data is being saved in sql database named as users.db
def reg():
    st.title("Registration Page")
    con = sqlite3.connect("database/users.db")
    pul = con.cursor()
    uid = gen_uid()

    name = st.text_input("Name", placeholder="Enter your name")
    email = st.text_input("Email", placeholder="Enter your email").strip().lower()
    pas = st.text_input("Password", placeholder="Enter your password", key="password", type="password")

    if st.button("Register"):
        if email=="" or "." not in email and "@" not in email and "gmail.com" not in email:
            st.error("Invalid email address")
            return
        try:
            pul.execute("INSERT INTO users (uid, username, email, password) values (?, ?, ?, ?)",
                        (uid, name, email, hash_pass(pas)))
            con.commit()
            st.success(f"User registered successfuly as{name}")
        except sqlite3.IntegrityError:
            st.error("Username already exists")
        finally:
            con.close()

# or yha credientials check ho ga or baki kam for registration 
def login():
    st.title("Login Page")
    email = st.text_input("Email adrress", placeholder="Enter your email").strip().lower()
    password = st.text_input("Password", placeholder="Enter your password", type="password")

    if st.button("Login"):
        if email=="" or password=="":
            st.error("Please enter email and password")
            return
        con = sqlite3.connect("database/users.db")
        pul = con.cursor()
        pul.execute("""
            SELECT username,password
                    FROM users
                    WHERE email = ?
                    """, (email,))
        data = pul.fetchone()
        con.close()

        if data is None:
            st.error("Data is not found")
            return

        if data[1] == hash_pass(password):
            st.success(f"Logged in successfully as {data[0]}")
            st.session_state.user = data[0]
            st.session_state.logedin = True
        else:
            st.error("Invalid credentials")


def module():
    with open("Models/placement_classifier.pkl", "rb") as file:
        placement_model = pickle.load(file)

    with open("Models/package_prediction_model.pkl", "rb") as file:
        salary_model = pickle.load(file)
        
    st.title("Student Placement & Salary Prediction")
    st.write("Enter student details to predict placement status and expected salary package.")

    cgpa = st.number_input("CGPA (out of 10)", min_value=0.0, max_value=10.0, step=0.01)
    internships = st.number_input("Number of Internships", min_value=0, step=1)
    mock_test = st.number_input("Mock Test Score", min_value=0, max_value=100, step=1)
    coding_hours = st.number_input("Coding Hours per Week", min_value=0, step=1)
    resume_score = st.number_input("Resume Score", min_value=0, max_value=100, step=1)

    if st.button("Predict"):
        if cgpa == 0.0:
            st.error("Please enter valid details")
            return
        student_data = [[cgpa, internships, mock_test, coding_hours, resume_score]]
        
        placement_result = placement_model.predict(student_data)
        placement_status = "PLACED" if placement_result[0] == 1 else "NOT PLACED"
        
        salary_prediction = salary_model.predict(student_data)
        salary_lpa = salary_prediction[0]
        
        st.subheader("Prediction Result")
        st.write("Placement Status:", placement_status)
        st.write("Expected Salary Package (LPA):", round(salary_lpa, 2))

def main():
    st.set_page_config(page_title="Placement Predictor", layout="wide")
    st.title("Student Placement & Salary Prediction App")
    if "logedin" not in st.session_state:
        st.session_state.logedin = False

    st.sidebar.title("Navigation")

    page = st.sidebar.radio("Go to", ["Dashboard","Login", "Register", "Logout"])

    if page == "Login":
        login()

    elif page == "Register":
        reg()

    elif page == "Dashboard":
        if st.session_state.logedin == True:
            st.write(f"Logged in as {st.session_state.user}")
            module()
        else:    
            st.warning("Please login to access the dashboard.")
            return

    elif page == "Logout":
        st.session_state.clear()
        st.success("Logged out successfully")

main()
