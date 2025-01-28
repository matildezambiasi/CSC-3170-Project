import sqlite3
import db_population_functions 
import checks

####add to cheange the status of an appointment
def change_status_app(name):  
    conn = sqlite3.connect('hospital.db')  
    cursor = conn.cursor()

    doctor_id_query = """
    SELECT doctor_id FROM Doctors
    WHERE name = ?;
    """
    cursor.execute(doctor_id_query, (name,))
    result = cursor.fetchone()
    doctor_id = result[0]

    print("-----------------------------------------------")
    appointment_id= input("Enter the appointment ID: ").strip()
    print("-----------------------------------------------")
    
    check_query = """
    SELECT * FROM Appointments
    WHERE appointment_id = ? AND doctor_id = ?;
    """
    cursor.execute(check_query, (appointment_id, doctor_id))
    result = cursor.fetchone()

    if result is None:

        print("\n-----------------------------------------------")
        print("|  No appointment found with the provided ID.  |")
        print("|      Please compare with the list below.     |")
        print("------------------------------------------------")
        get_doctor_appointments(name)
        change_status_app(name)
   
    else:
        happen = input("did the appointment happen?[y/n] ")
        if happen == "y":
            status = "DONE"
            app_status_query = """
            UPDATE Appointments
            SET status = ?
            WHERE appointment_id = ?;
            """
            cursor.execute(app_status_query, (status, appointment_id))
            conn.commit()
            print("\n-----------------------------------------------")
            print("|   Appointment status updated successfully!   |")
            print("------------------------------------------------")
    conn.close()
    





def check_medications_doctor(name):

    conn = sqlite3.connect('hospital.db')  
    cursor = conn.cursor()

    doctor_id_query = """
    SELECT doctor_id FROM Doctors
    WHERE name = ?;
    """
    cursor.execute(doctor_id_query, (name,))
    result = cursor.fetchone()
    doctor_id = result[0]

    query = """
    SELECT m.medication_name, m.dispensed, p.name, m.high_risk 
    FROM Medication m
    JOIN Patients p ON m.patient_id = p.patient_id
    WHERE m.doctor_id = ?;
    """

    cursor.execute(query, (doctor_id,))

    medication = cursor.fetchall()

    if not medication:
        print("\n-----------------------------------------------")
        print("|          No prescribed medication           |")
        print("-----------------------------------------------")
    else:

        for medication in medication:
            medication_name, status, patient, risk = medication
            print("\n----------------------------------------------------------")
            print(f"medication {medication_name} was prescribed to {patient}")
            print(f"medicine was dispensed: {status}")     
            print(f"medicine is high risk: {risk}")
            print("\n----------------------------------------------------------")
              
    
    add = input("would you like to prescribe a medication? [y/n]")
    if add == "y":
        med_name = input("insert the name of the medication: ")
        while True:
            patient_id= input("insert the ID of the patient: ")
            if checks.check_patient_exists_id(patient_id) == False:
                    print("\n-----------------------------------------------")
                    print("|             Invalid patient ID              |")
                    print("-----------------------------------------------")
            else:
                break
        dispensed = "NO"
        high_risk = input("is the medication high risk? ")
        while True:
            date = input("add current date(YYYY-MM-DD): ")
            if checks.is_valid_date(date) == False:
                    print("\n-----------------------------------------------")
                    print("|    Invalid date. Format is YYYY-MM-DD       |")
                    print("-----------------------------------------------")
            else:
                break

        db_population_functions.add_medication(patient_id, doctor_id, date, med_name, dispensed, high_risk)
        conn.commit()
    conn.close()
          

def update_appointment_date_doctor(name):
    print("-----------------------------------------------")
    appointment_id= input("Enter the appointment ID: ").strip()
    print("-----------------------------------------------")
    
    conn = sqlite3.connect('hospital.db') 
    cursor = conn.cursor()

    doctor_id_query = """
    SELECT doctor_id FROM Doctors
    WHERE name = ?;
    """
    cursor.execute(doctor_id_query, (name,))
    result = cursor.fetchone()
    doctor_id = result[0]

    check_query = """
    SELECT * FROM Appointments
    WHERE appointment_id = ? AND doctor_id = ?;
    """
    cursor.execute(check_query, (appointment_id, doctor_id))
    result = cursor.fetchone()

    if result is None:

        print("\n-----------------------------------------------")
        print("|  No appointment found with the provided ID.  |")
        print("|      Please compare with the list below.     |")
        print("------------------------------------------------")
        get_doctor_appointments(name)
        update_appointment_date_doctor(name)

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


def get_doctor_appointments(name):

    conn = sqlite3.connect('hospital.db')  
    cursor = conn.cursor()

    query = """
    SELECT a.date, a.time, p.name, p.patient_id, a.status, a.appointment_id
    FROM Appointments a 
    JOIN Patients p ON a.patient_id = p.patient_id
    JOIN Doctors d ON a.doctor_id = d.doctor_id
    WHERE d.name = ?
    ORDER BY a.date, a.time;
    """

    cursor.execute(query, (name,))

    appointments = cursor.fetchall()

    conn.close()

    if not appointments:
        print("\n-----------------------------------------------")
        print("|        You have no booked appointments       |")
        print("------------------------------------------------")
    else:
        print("\n-----------------------------------------------")

        for appointment in appointments:
            date, time, patient_name, patient_id, status, appointment_id = appointment
            print(f"Date: {date}, Time: {time}, Patient: {patient_name}")
            print(f"Patient id: {patient_id}, Status: {status}, ID: {appointment_id}")
        print("-----------------------------------------------")


def book_appointment_doctor(name):
    conn = sqlite3.connect('hospital.db') 
    cursor = conn.cursor()
    
    while True:
        patient = input("What patient would you like to meet? ").strip()
        if checks.check_patient_exists_name(patient) == False:
                print("\n-----------------------------------------------")
                print("|      Patient doesn't exist. Try again.      |")
                print("-----------------------------------------------")
        else:
            break


    while True:
        date = input("Enter the date(YYYY-MM-DD): ").strip()
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

    doctor_id_query = """
    SELECT doctor_id FROM Doctors
    WHERE name = ?;
    """
    cursor.execute(doctor_id_query, (name,))
    result = cursor.fetchone()
    doctor_id = result[0]

    patient_id_query = """
    SELECT patient_id FROM Patients
    WHERE name = ?;
    """
    cursor.execute(patient_id_query, (patient,))
    result = cursor.fetchone()
    patient_id = result[0]
    db_population_functions.add_appointment(patient_id, doctor_id, date, time)


def cancel_appointment_doctor(name): 
    conn = sqlite3.connect('hospital.db') 
    cursor = conn.cursor()
    
    doctor_id_query = """
    SELECT doctor_id FROM Doctors
    WHERE name = ?;
    """
    cursor.execute(doctor_id_query, (name,))
    result = cursor.fetchone()
    doctor_id = result[0]

    while True:
        appointment_id= input("Enter the ID of the appointment to cancel: ").strip()
        if checks.appointment_belongs_to_doctor(doctor_id, appointment_id) == False:
                print("\n-----------------------------------------------")
                print("|           Invalid appointment ID            |")
                print("|     Please compare with the list below.     |")
                print("-----------------------------------------------")
                get_doctor_appointments(name)
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

    conn.close()


def patient_list(name):
    
    conn = sqlite3.connect('hospital.db') 
    cursor = conn.cursor()

    doctor_id_query = """
    SELECT doctor_id FROM Doctors
    WHERE name = ?;
    """
    cursor.execute(doctor_id_query, (name,))
    result = cursor.fetchone()
    doctor_id = result[0]

    patient_list_query = """
    SELECT p.name 
    FROM Patients p
    JOIN Appointments a ON a.patient_id = p.patient_id
    JOIN Doctors d ON a.doctor_id = d.doctor_id
    WHERE d.doctor_id = ?
    """
    cursor.execute(patient_list_query, (doctor_id,))
    patient_list = cursor.fetchall()
    print("\n-----------------------")
    for name in patient_list:
        print(name[0])
    print("\n-----------------------")


def main_doctors(name):
    action = input("what would you like to do? (check_medication, appointments, patient_list) ")
    if action == "check_medication":
        check_medications_doctor(name)
    elif action == "appointments":
        action_appointment = input("book, change, cancel, see, set_as_done: ")
        if action_appointment == "book":
            book_appointment_doctor(name)
        elif action_appointment == "change":
            update_appointment_date_doctor(name)
        elif action_appointment == "cancel":
            cancel_appointment_doctor(name)
        elif action_appointment == "see":
            get_doctor_appointments(name)
        elif action_appointment == "set_as_done":
            change_status_app(name)
        else: 
            print("\n-----------------------------------------------")
            print("|               Invalid action                |")
            print("-----------------------------------------------")
    elif action == "patient_list":
        patient_list(name)
    else:
            print("\n-----------------------------------------------")
            print("|               Invalid action                |")
            print("-----------------------------------------------")

