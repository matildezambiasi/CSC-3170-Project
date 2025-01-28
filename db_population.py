import db_population_functions 

patients = [

['Ludovica', '2003-9-16', 'female', 111222333],
['Niklas', '1998-11-23', 'male', 111222334],
['Andrea', '2007-12-24', 'male', 111222335],
['Emma', '2006-02-17', 'female', 111222336],
['Cinzia', '1973-04-14', 'female', 111222337],
['Luca', '1965-03-17', 'male', 111222338],
['Giulia', '2003-6-12', 'female', 111222339],
['Nicole', '2003-5-3', 'female', 111222341],
['Giuseppina', '1952-2-23', 'female', 111222342],
['Attilio', '1938-7-27', 'male', 111222343],
['Elsa', '1938-1-1', 'female', 111222344]
]


for i in range (len(patients)):
    db_population_functions.add_patient(
                                        patients[i][0],
                                        patients[i][1],
                                        patients[i][2],
                                        patients[i][3])
    
doctors = [
['Lana', 'Cardiology', 211222333],
['Troye', 'Geriatrics', 211222334],
['Frida', 'Radiology', 211222335],
['Mika', 'Psychiatry', 211222336],
['Harry', 'Surgery', 211222337],
['Jessie', 'Pediatrics', 211222338],
['Taylor', 'Oncology', 211222339],
]


for i in range (len(doctors)):
    db_population_functions.add_doctor(doctors[i][0],
                                       doctors[i][1],
                                       doctors[i][2])


pharmacists = [
    ['Nike', 31222339],
    ['Matilde', 31222340]
]

for i in range (len(pharmacists)):
    db_population_functions.add_pharmacist(pharmacists[i][0],
                                       pharmacists[i][1])


appointments = [
[2, 7, '2024-10-31', '10:00', 'Missed'],
[4, 3, '2024-10-30', '10:00', 'Done'],
[1, 5, '2024-11-7', '10:00', 'Scheduled'],
[9, 2, '2024-11-10', '10:00', 'Scheduled'],
[10, 2, '2024-9-4', '10:00', 'Done'],
[11, 2, '2024-10-30', '10:00', 'Done'],
[3, 6, '2024-11-20', '10:00', 'Scheduled']
]


for i in range (len(appointments)):
    db_population_functions.add_appointment(
                                        appointments[i][0],
                                        appointments[i][1],
                                        appointments[i][2],
                                        appointments[i][3],
                                        appointments[i][4])
    

medication = [
[4, 3, '2024-10-30', 'ABC', 'YES', 'NO'],
[10, 2, '2024-9-4', 'XYZ', 'YES', 'YES'],
[9, 2, '2024-3-4', 'XYZ', 'NO', 'NO'],
[1, 2, '2024-2-4', 'ABC', 'YES', 'YES'],
[3, 2, '2024-9-19', 'LMZ', 'YES', 'YES'],
[6, 2, '2024-9-4', 'XYZ', 'YES', 'YES'],
[11, 2, '2024-10-30', 'LMN', 'NO', 'NO'],
]

for i in range (len(medication)):
    db_population_functions.add_medication(
                                        medication[i][0],
                                        medication[i][1],
                                        medication[i][2],
                                        medication[i][3],
                                        medication[i][4])
    

users = [
['Ludovica', 'patient', '111222333'],
['Niklas', 'patient', '111222334'],
['Andrea', 'patient', '111222335'],
['Emma', 'patient', '111222336'],
['Cinzia', 'patient', '111222337'],
['Luca', 'patient', '111222338'],
['Giulia','patient', '111222339'],
['Nicole', 'patient', '111222341'],
['Giuseppina', 'patient', '111222342'],
['Attilio', 'patient', '111222343'],
['Elsa', 'patient', '111222344'],
['Lana', 'doctor', '211222333'],
['Troye', 'doctor', '211222334'],
['Frida', 'doctor', '211222335'],
['Mika', 'doctor', '211222336'],
['Harry', 'doctor', '211222337'],
['Jessie', 'doctor', '211222338'],
['Taylor', 'doctor', '211222339'],
['Nike', 'pharmacist', '31222339'],
['Matilde', 'pharmacist', '31222340']
]

for i in range(len(users)):
       db_population_functions.add_user(
                                        users[i][0],
                                        users[i][1],
                                        users[i][2])
       

def first_time(generate):
    print("i am running for no reason")
    if generate == "y":
        with open("db_creation_1.py") as creation:
            exec(creation.read())

        with open("db_population.py") as population:
            exec(population.read())