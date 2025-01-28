import sqlite3
import bcrypt
import db_population_functions
import checks



# Function to verify login credentials
def verify_user(name, role, password):
    
    conn = sqlite3.connect("hospital.db")
    cursor = conn.cursor()
    cursor.execute("SELECT hashed_password FROM Users WHERE name=? AND role=?", (name, role))
    result = cursor.fetchone()
    
    if result:
        hashed_password = result[0]
        return bcrypt.checkpw(password.encode(), hashed_password)
    else:
        return False

# CLI for role selection and login
def main_password():
    conn = sqlite3.connect("hospital.db")
    cursor = conn.cursor()
    
    print("###############################################")
    print("#                                             #")
    print("#                    Welcome!                 #")
    print("#                                             #")
    print("###############################################\n")

    print("===============================================")
    print("            Enter your credentials             ")
    print("===============================================")

    # Input for username and password
    role = input("\nWhat is your role? (doctor, patient, pharmacist): ").strip().lower()
    name = input("\nName: ").strip()
    password = input("\nPassword: ").strip()


    if role not in ['doctor', 'patient', 'pharmacist']:

        print("\n-------------------------------------------------")
        print("|                  Invalid role                    |")
        print("| Please enter 'doctor', 'patient', or 'pharmacist'|")
        print("---------------------------------------------------")
        main_password()


    if role == "patient":
        cursor.execute("SELECT COUNT(*) FROM Patients WHERE name =?",(name,))
        if cursor.fetchone()[0] == 0:
            print("\n-----------------------------------------------")
            print("|                Registration                 |")
            print("-----------------------------------------------")

            while True:
                date_of_birth = input("Enter date of birth (YYYY-MM-DD): ").strip()
                if checks.is_valid_date(date_of_birth) == False:
                        print("\n-----------------------------------------------")
                        print("|    Invalid date. Format is YYYY-MM-DD       |")
                        print("-----------------------------------------------")
                else:
                    break
            gender = input("Enter gender (male, female, other): ").strip().lower()
            phone = input("Enter phone number: ").strip()
            db_population_functions.add_patient(name, date_of_birth, gender, phone)
            return name, role

    if verify_user(name, role, password) == False:

        print("\n-----------------------------------------------")
        print("|            Incorrect credentials.           |")
        print("-----------------------------------------------")
        main_password()

    else:

        print("\n-----------------------------------------------")
        print(f"|             Welcome, {name}!               |")
        print(f"|        You successfully logged in          |")
        print("-----------------------------------------------")
        return name, role 

