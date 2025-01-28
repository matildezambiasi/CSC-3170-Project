import sqlite3
import db_population_functions 
import checks

def dispense_medication():

    print("\n-----------------------------------------------")
    print("|      You can now dispense medication        |")
    print("-----------------------------------------------")

    name_patient = input("patient name: ")
    medication_name = input("medication name: ")
    
    exist = checks.check_medication_exists(name_patient, medication_name)
    
    if exist == 1:
        conn = sqlite3.connect('hospital.db')  
        cursor = conn.cursor()

        highrisk_query = """
        SELECT m.high_risk
            FROM Medication m
            JOIN Patients p ON m.patient_id = p.patient_id
            WHERE p.name = ?
            AND m.medication_name = ?;
            """
        cursor.execute(highrisk_query, (name_patient, medication_name,))
        result = cursor.fetchall()

        if result[0] == "YES":
            phone_number_query = """
                SELECT d.phone_number
                FROM Medication m
                JOIN Patients p ON m.patient_id = p.patient_id
                JOIN Doctors d ON m.doctor_id = d.doctor_id
                WHERE p.name = ?
                AND m.medication_name = ?;
            """
            cursor.execute(phone_number_query, (name_patient, medication_name,))
            phone = cursor.fetchall()
        
            print("\n------------------------------------------------------------------------------")
            print(f"| please contact the doctor at {phone[0]} before dispensing high risk medicine |")
            print("---------------------------------------------------------------------------------")

            approval = input("Did you get approval from the doctor? [y/n] ")
            if approval == "n":
                print("\n-----------------------------------------------")
                print("|       Medication cannot be dispensed        |")
                print("-----------------------------------------------")
                return
        
        dispensing_query = """
            UPDATE Medication
            SET dispensed = 'YES'
            WHERE patient_id = (
            SELECT patient_id
            FROM Patients
            WHERE name = ?
            )
            AND medication_name = ?
            AND dispensed = 'NO';
            """
        cursor.execute(dispensing_query, (name_patient, medication_name,))
        print("\n-----------------------------------------------")
        print("|       Medication dispensed correctly        |")
        print("-----------------------------------------------")
    
    else: 
        print("\n-----------------------------------------------")
        print("|   Name or medication are wrong. Try again   |")
        print("-----------------------------------------------")
        dispense_medication()





