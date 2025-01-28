import sqlite3
import db_population_functions 
import checks
###############AGGIUNGERE VEDERE LISTA DOTTORI 



def get_patient_appointments(name):
    # Connect to the database
    conn = sqlite3.connect('hospital.db')  # Replace 'your_database.db' with your actual database name or connection details
    cursor = conn.cursor()

    # SQL query to retrieve appointments for a specific patient
    query = """
    SELECT a.date, a.time, d.name, d.specialization, a.status, a.appointment_id
    FROM Appointments a 
    JOIN Patients p ON a.patient_id = p.patient_id
    JOIN Doctors d ON a.doctor_id = d.doctor_id
    WHERE p.name = ?
    ORDER BY a.date, a.time;
    """
    # Execute the query with the given patient_id
    cursor.execute(query, (name,))
    # Fetch all results
    appointments = cursor.fetchall()
    # Close the connection
    conn.close()
    # Check if any appointments were found
    if not appointments:
        print("\n-----------------------------------------------")
        print("|            No appointments booked.           |")
        print("------------------------------------------------")

    else:
        # Print each appointment in a readable format
        for appointment in appointments:
            date, time, doctor_name, specialization, status, appointment_id = appointment
            print("\n------------------------------------------------------------")
            print(f"Date: {date}, Time: {time}, Doctor: {doctor_name}, "
                  f"Department: {specialization}, Status: {status}, ID: {appointment_id}")
            print("---------------------------------------------------------------")


def update_appointment_date_patient(name):

    appointment_id= input("Enter the appointment ID: ").strip()
    
    conn = sqlite3.connect('hospital.db') 
    cursor = conn.cursor()

    patient_id_query = """
    SELECT patient_id FROM Patients
    WHERE name = ?;
    """
    cursor.execute(patient_id_query, (name,))
    result = cursor.fetchone()
    patient_id = result[0]


    check_query = """
    SELECT 1 FROM Appointments
    WHERE appointment_id = ? AND patient_id = ?;
    """
    cursor.execute(check_query, (appointment_id, patient_id))
    result = cursor.fetchone()

    if result is None:
        print("\n-----------------------------------------------")
        print("|  No appointment found with the provided ID.  |")
        print("|      Please compare with the list below.     |")
        print("------------------------------------------------")
        get_patient_appointments(name)
        update_appointment_date_patient(name)
    else:
        new_date = input("Enter the new date (YYYY-MM-DD): ").strip()
        new_time = input("Enter the new time (HH:MM): ").strip()
 
        query = """
        UPDATE Appointments
        SET date = ?, time = ?
        WHERE appointment_id = ?;
        """

        cursor.execute(query, (new_date, new_time, appointment_id))

        conn.commit()
         

        print("\n-----------------------------------------------")
        print("|    Appointment updated successfully         |")
        print("-----------------------------------------------")

        conn.close()


def cancel_appointment_patient(name):
    conn = sqlite3.connect('hospital.db') 
    cursor = conn.cursor()

    patient_id_query = """
    SELECT patient_id FROM Patients
    WHERE name = ?;
    """
    cursor.execute(patient_id_query, (name,))
    result = cursor.fetchone()
    patient_id = result[0]

    while True:
        appointment_id= input("Enter the ID of the appointment to cancel: ").strip()
        if checks.appointment_belongs_to_patient(patient_id, appointment_id) == False:
                print("\n-----------------------------------------------")
                print("| No appointment found with the provided ID.  |")
                print("|     Please compare with the list below.     |")
                print("-----------------------------------------------")
                get_patient_appointments(name)
                cancel_appointment_patient(name)
        else: 
            break

    certain = input("Are you sure you want to cancel? [y/n]: ").strip()
    if certain == "y":
        query = """
            UPDATE Appointments
            SET status = "Cancelled"
            WHERE appointment_id = ?;
            """
        cursor.execute(query, (appointment_id))
        conn.commit()
        print("\n-----------------------------------------------")
        print("|     Appointment cancelled successfully      |")
        print("-----------------------------------------------")
        return
    conn.close()


def book_appointment_patient(name):
    conn = sqlite3.connect('hospital.db') 
    cursor = conn.cursor()
    print("\n-----------------------------------------------")
    while True:
        doctor = input("What doctor would you like to meet? ").strip()
        if checks.check_doctor_exists_name(doctor) == False:
                print("\n-----------------------------------------------")
                print("|      Doctor doesn't exist. Try again        |")
                print("-----------------------------------------------")
        else:
            break
    while True:
        date = input("Enter the date (YYYY-MM-DD): ")
        if checks.is_valid_date(date) == False:
                print("\n-----------------------------------------------")
                print("|    Invalid date. Format is YYYY-MM-DD       |")
                print("-----------------------------------------------")
        else:
            break
    while True:
        time = input("Enter the time (HH:MM): ").strip()
        if checks.is_valid_time(time) == False:
            print("\n-----------------------------------------------")
            print("|       Invalid time. Format is HH:MM         |")
            print("-----------------------------------------------")
        else:
            break

        
    patient_id_query = """
    SELECT patient_id FROM Patients
    WHERE name = ?;
    """
    cursor.execute(patient_id_query, (name,))
    result = cursor.fetchone()
    patient_id = result[0]

    doctor_id_query = """
    SELECT doctor_id FROM Doctors
    WHERE name = ?;
    """
    cursor.execute(doctor_id_query, (doctor,))
    result = cursor.fetchone()
    doctor_id = result[0]
    db_population_functions.add_appointment(patient_id, doctor_id, date, time)


def check_medications_patient(name):

    conn = sqlite3.connect('hospital.db')  
    cursor = conn.cursor()

    patient_id_query = """
    SELECT patient_id FROM Patients
    WHERE name = ?;
    """
    cursor.execute(patient_id_query, (name,))
    result = cursor.fetchone()
    patient_id = result[0]

  
    query = """
    SELECT m.medication_name, m.dispensed 
    FROM Medication m
    JOIN Patients p ON m.patient_id = p.patient_id
    WHERE m.patient_id = ?;
    """

    cursor.execute(query, (patient_id,))

    medication = cursor.fetchall()

    if not medication:
            print("\n-----------------------------------------------")
            print("|  You have not been prescribed any medicine  |")
            print("-----------------------------------------------")
    else:
     
        for medication in medication:
            medication_name, dispensed = medication
            print("\n-----------------------------------------------")
            print(f"name of the medication: {medication_name}")

            if dispensed == "YES":
                 print("the medicine was dispensed")
                 print("-----------------------------------------------")
            if dispensed == "NO":
                print("the medicine was not dispensed")
                print("-----------------------------------------------")
                call = input ("do you want to talk to a pharmacist to get your medicine? [y/n] ")
                if call == "y":
                    pharmacist_query = """
                        SELECT name, phone FROM Pharmacist
                        """
                    cursor.execute(pharmacist_query, ())
            
                    contacts = cursor.fetchone()
                    
                    conn.close()
                    print("\n-----------------------------------------------")
                    print(f"name of the pharmacist: {contacts[0]}, phone number: {contacts[1]}")
                    print("-----------------------------------------------")

def see_doctors():
    conn = sqlite3.connect('hospital.db')  
    cursor = conn.cursor()

    patient_id_query = """
    SELECT name, specialization
    FROM Doctors
    """
    cursor.execute(patient_id_query, ())
    doctors = cursor.fetchall()
    
    for doctor in doctors:
        doc_name, doc_specialization = doctor
        print("\n-----------------------------------------------")
        print(f"Doctor {doc_name} is specialized in {doc_specialization}")
        print("-----------------------------------------------")

def _main_patient(name):
    action = input("What would you like to do? (see_doctors, see_app, book_app, cancel_app, update_app, see_medication) ")
    if action == "see_app":
        get_patient_appointments(name)
    elif action == "see_doctors":
        see_doctors()
    elif action == "book_app":
        book_appointment_patient(name)
    elif action == "cancel_app":
        cancel_appointment_patient(name)
    elif action == "update_app":
        update_appointment_date_patient(name)
    elif action == "see_medication":
        check_medications_patient(name)
    else:
        print("\n-----------------------------------------------")
        print("|               Invalid action                |")
        print("-----------------------------------------------")

