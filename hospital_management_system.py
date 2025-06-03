import mysql.connector
from mysql.connector import Error

class HospitalManagementSystem:
    def __init__(self):
        self.host = 'localhost'
        self.database = 'hospital_management'
        self.user = 'root'
        self.password = 'root'

    def create_connection(self):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            return connection
        except Error as e:
            print(f"Error: {e}")

    def add_patient(self, name, email, phone, address):
        connection = self.create_connection()
        cursor = connection.cursor()
        query = "INSERT INTO patients (name, email, phone, address) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (name, email, phone, address))
        connection.commit()
        connection.close()

    def add_doctor(self, name, specialty, email, phone):
        connection = self.create_connection()
        cursor = connection.cursor()
        query = "INSERT INTO doctors (name, specialty, email, phone) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (name, specialty, email, phone))
        connection.commit()
        connection.close()

    def book_appointment(self, patient_id, doctor_id, appointment_date, appointment_time):
        connection = self.create_connection()
        cursor = connection.cursor()
        query = "INSERT INTO appointments (patient_id, doctor_id, appointment_date, appointment_time) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (patient_id, doctor_id, appointment_date, appointment_time))
        connection.commit()
        connection.close()

    def display_patients(self):
        connection = self.create_connection()
        cursor = connection.cursor()
        query = "SELECT * FROM patients"
        cursor.execute(query)
        patients = cursor.fetchall()
        for patient in patients:
            print(patient)
        connection.close()

    def display_doctors(self):
        connection = self.create_connection()
        cursor = connection.cursor()
        query = "SELECT * FROM doctors"
        cursor.execute(query)
        doctors = cursor.fetchall()
        for doctor in doctors:
            print(doctor)
        connection.close()

    def display_appointments(self):
        connection = self.create_connection()
        cursor = connection.cursor()
        query = "SELECT * FROM appointments"
        cursor.execute(query)
        appointments = cursor.fetchall()
        for appointment in appointments:
            print(appointment)
        connection.close()

# Example usage
hospital_system = HospitalManagementSystem()

while True:
    print("Hospital Management System")
    print("1. Add Patient")
    print("2. Add Doctor")
    print("3. Book Appointment")
    print("4. Display Patients")
    print("5. Display Doctors")
    print("6. Display Appointments")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter patient name: ")
        email = input("Enter patient email: ")
        phone = input("Enter patient phone: ")
        address = input("Enter patient address: ")
        hospital_system.add_patient(name, email, phone, address)
    elif choice == "2":
        name = input("Enter doctor name: ")
        specialty = input("Enter doctor specialty: ")
        email = input("Enter doctor email: ")
        phone = input("Enter doctor phone: ")
        hospital_system.add_doctor(name, specialty, email, phone)
    elif choice == "3":
        patient_id = input("Enter patient ID: ")
        doctor_id = input("Enter doctor ID: ")
        appointment_date = input("Enter appointment date (YYYY-MM-DD): ")
        appointment_time = input("Enter appointment time (HH:MM:SS): ")
        hospital_system.book_appointment(patient_id,doctor_id,appointment_date,appointment_time)
    elif choice == "4":
        hospital_system.display_patients()
    elif choice == "5":
        hospital_system.display_doctors()
    elif choice == "6":
        hospital_system.display_appointments()  
    elif choice == "7":
        break
