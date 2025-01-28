import sqlite3
import doctor_actions_p
import patient_actions_p
import pharmacist_actions_p
import passwords_p


def _main_():
    
    name, role = passwords_p.main_password()

    if role == "doctor":
        doctor_actions_p.main_doctors(name)
        while True:
            repeat = input("do you need to do anything more? [y/n] ")
            if repeat == "y":
                doctor_actions_p.main_doctors(name)
            if repeat == "n":
                _main_()
    elif role == "patient":
        patient_actions_p._main_patient(name)
        while True:
            repeat = input("do you need to do anything more? [y/n] ")
            if repeat == "y":
                patient_actions_p._main_patient(name)
            if repeat == "n":
                _main_()
    elif role == "pharmacist":
        pharmacist_actions_p.dispense_medication()
        while True:
            repeat = input("do you need to do anything more? [y/n] ")
            if repeat == "y":
                pharmacist_actions_p.dispense_medication()
            if repeat == "n":
                _main_()


_main_()