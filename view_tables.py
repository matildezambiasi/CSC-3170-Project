import sqlite3

def view_table_contents(table_name):
    with sqlite3.connect('hospital.db') as connection:
        cursor = connection.cursor()
        

        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()  

        print(f"Contents of the '{table_name}' table:")
        for row in rows:
            print(row)


# view_table_contents("Patients")
# view_table_contents("Doctors")
# view_table_contents("Pharmacist")
# view_table_contents("Appointments")
view_table_contents("Medication")
# view_table_contents("Users")