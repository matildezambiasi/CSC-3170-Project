from datetime import datetime
import sqlite3

def is_valid_date(date_string):

    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False
    

def check_patient_exists_id(patient_id):
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()

    cursor.execute("""
        SELECT EXISTS (
            SELECT 1
            FROM Patients
            WHERE patient_id = ?
        );
    """, (patient_id,))
    result = cursor.fetchone()[0]
    conn.close()
    return result == 1


def check_patient_exists_name(name):

    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()

    cursor.execute("""
        SELECT EXISTS (
            SELECT 1
            FROM Patients
            WHERE name = ?
        );
    """, (name,))
    result = cursor.fetchone()[0]
    conn.close()
    return result == 1


def check_doctor_exists_name(name):

    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()

    cursor.execute("""
        SELECT EXISTS (
            SELECT 1
            FROM Doctors
            WHERE name = ?
        );
    """, (name,))
    result = cursor.fetchone()[0]
    conn.close()
    return result == 1


def is_valid_time(time_string):

    try:
        datetime.strptime(time_string, "%H:%M")
        return True
    except ValueError:
        return False


def appointment_belongs_to_doctor(doctor_id, appointment_id):

    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()

    # Execute the SQL query to check if the appointment belongs to the doctor
    cursor.execute("""
        SELECT EXISTS (
            SELECT 1
            FROM Appointments
            WHERE doctor_id = ? AND appointment_id = ?
        );
    """, (doctor_id, appointment_id))

    result = cursor.fetchone()[0]
    conn.close()
    return result == 1


def appointment_belongs_to_patient(patient_id, appointment_id):


    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()

    # Execute the SQL query to check if the appointment belongs to the doctor
    cursor.execute("""
        SELECT EXISTS (
            SELECT 1
            FROM Appointments
            WHERE patient_id = ? AND appointment_id = ?
        );
    """, (patient_id, appointment_id))

    result = cursor.fetchone()[0]
    conn.close()
    return result == 1

def check_medication_exists(name, med_name):
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()

    patient_id_query = """
    SELECT patient_id FROM Patients
    WHERE name = ?;
    """
    cursor.execute(patient_id_query, (name,))
    patient_id = cursor.fetchone()[0]
    print(patient_id)
    cursor.execute("""
        SELECT EXISTS (
            SELECT 1
            FROM Medication
            WHERE patient_id = ? AND medication_name = ?
        );
    """, (patient_id, med_name))
    result = cursor.fetchone()[0]
    conn.close()
    return result == 1

check_medication_exists("Elsa", "LMN")