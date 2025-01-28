import sqlite3

# Connect to the database
connection = sqlite3.connect('hospital.db')
cursor = connection.cursor()

# SQL to create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS Patients (
    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    date_of_birth TEXT,
    gender TEXT,
    phone INTEGER          
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Doctors (
    doctor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    specialization TEXT,
    phone TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Appointments (
    appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER NOT NULL,
    doctor_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    time TEXT NOT NULL,
    status TEXT,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Medication (
    patient_id INTEGER NOT NULL,
    doctor_id INTEGER NOT NULL,
    prescription_date TEXT NOT NULL,
    medication_name TEXT NOT NULL, 
    dispensed TEXT DEFAULT 'NO',
    high_risk TEXT DEFAULT 'NO',
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Pharmacist (
    pharmacist_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT
)
''')


cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        name TEXT NOT NULL PRIMARY KEY,
        role TEXT CHECK(role IN ('doctor', 'patient', 'pharmacist')) NOT NULL,
        hashed_password TEXT NOT NULL
    )
''')



# Commit changes and close the connection
connection.commit()
connection.close()

