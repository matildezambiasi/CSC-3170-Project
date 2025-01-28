import sqlite3

# Connect to the database
with sqlite3.connect('hospital.db') as connection:
    cursor = connection.cursor()
    
    # Drop tables one by one
    cursor.execute("DROP TABLE IF EXISTS Patients")
    cursor.execute("DROP TABLE IF EXISTS Doctors")
    cursor.execute("DROP TABLE IF EXISTS Appointments")
    cursor.execute("DROP TABLE IF EXISTS Medication")
    cursor.execute("DROP TABLE IF EXISTS Pharmacist")
    
    # Commit changes
    connection.commit()
    
print("All tables have been dropped and the database is now empty.")