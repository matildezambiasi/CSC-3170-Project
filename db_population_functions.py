import sqlite3
import bcrypt

def add_patient(name, dob, gender, phone):
    # Connect to the database
    with sqlite3.connect('hospital.db') as connection:
        cursor = connection.cursor()
        
        # Insert a new patient record
        cursor.execute('''
        INSERT INTO Patients (name, date_of_birth, gender, phone)
        VALUES (?, ?, ?, ?)
        ''', (name, dob, gender, phone))
        
        # Commit the transaction
        connection.commit()
        
        print("Patient added successfully.")


def add_doctor(name, specialization, phone):
    # Connect to the database
    with sqlite3.connect('hospital.db') as connection:
        cursor = connection.cursor()
        
        # Insert a new patient record
        cursor.execute('''
        INSERT INTO Doctors (name, specialization, phone)
        VALUES (?, ?, ?)
        ''', (name, specialization, phone))
        
        # Commit the transaction
        connection.commit()
        
        print("Doctor added successfully.")


def add_appointment(patient_id, doctor_id, date, time, status = 'Scheduled'):
    # Connect to the database
    with sqlite3.connect('hospital.db') as connection:
        cursor = connection.cursor()
        
        # Insert a new patient record
        cursor.execute('''
        INSERT INTO Appointments (patient_id, doctor_id, date, time, status)
        VALUES (?, ?, ?, ?, ?)
        ''', (patient_id, doctor_id, date, time, status))
        
        # Commit the transaction
        connection.commit()

        print("Appointment added successfully.")



def add_medication(patient_id, doctor_id, prescription_date, medication_name, dispensed = 'NO', high_risk = 'NO'):

    with sqlite3.connect('hospital.db') as connection:
        cursor = connection.cursor()
        
 
        cursor.execute('''
        INSERT INTO Medication (patient_id, doctor_id, prescription_date, medication_name, dispensed, high_risk)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (patient_id, doctor_id, prescription_date, medication_name, dispensed, high_risk))
        
   
        connection.commit()
        
        print("Medication added successfully.")


def add_pharmacist(name, phone):
    # Connect to the database
    with sqlite3.connect('hospital.db') as connection:
        cursor = connection.cursor()
        
        # Insert a new patient record
        cursor.execute('''
        INSERT INTO Pharmacist (name, phone)
        VALUES (?, ?)
        ''', (name, phone))
        
        # Commit the transaction
        connection.commit()
        
        print("Pharmacist added successfully.")

def add_user(name, role, password):
    connection  = sqlite3.connect("hospital.db")
    cursor = connection.cursor()
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    cursor.execute("INSERT INTO Users (name, role, hashed_password) VALUES (?, ?, ?)", (name, role, hashed_password))
    connection.commit()

    print ("user added successfully.")