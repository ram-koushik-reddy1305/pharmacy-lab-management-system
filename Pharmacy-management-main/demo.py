import mysql.connector
from mysql.connector import Error
import db_tasks

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '1934'
}

DB_NAME = 'Pharmacydb'


def create_database():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        print(f"Database '{DB_NAME}' is ready.")
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def create_tables():
    try:
        conn = mysql.connector.connect(**DB_CONFIG, database=DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Patients (
                patient_id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                age INT NOT NULL,
                gender VARCHAR(10) NOT NULL,
                contact VARCHAR(15) NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS LabOperators (
                operator_id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                contact VARCHAR(15) NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Labs (
                lab_id INT AUTO_INCREMENT PRIMARY KEY,
                lab_name VARCHAR(100) NOT NULL,
                lab_specialization VARCHAR(100) NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS TestReports (
                report_id INT AUTO_INCREMENT PRIMARY KEY,
                patient_id INT,
                test_name VARCHAR(100) NOT NULL,
                test_date DATE NOT NULL,
                result TEXT NOT NULL,
                FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS LabOperatorAssignments (
                assignment_id INT AUTO_INCREMENT PRIMARY KEY,
                operator_id INT,
                lab_id INT,
                FOREIGN KEY (operator_id) REFERENCES LabOperators(operator_id),
                FOREIGN KEY (lab_id) REFERENCES Labs(lab_id)
            )
        """)

        print("All required tables are ready.")
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

def authenticate_admin():
    username = input("Enter Admin Username: ")
    password = input("Enter Admin Password: ")

    ADMIN_USERNAME = "mithun"
    ADMIN_PASSWORD = "1934"

    return username == ADMIN_USERNAME and password == ADMIN_PASSWORD


def lab_operator_menu():
    while True:
        print("\n--- Lab Operator Menu ---")
        print("1. Add Patient")
        print("2. Modify Patient")
        print("3. Retrieve Patient")
        print("4. Add Report")
        print("5. Modify Report")
        print("6. Retrieve Report")
        print("0. Exit to Main Menu")
        choice_input = input("Enter your choice: ")

        if not choice_input.isdigit():
            print("Invalid input. Enter a number.")
            continue

        choice = int(choice_input)

        if choice == 1:
            db_tasks.add_patient()
        elif choice == 2:
            db_tasks.modify_patient()
        elif choice == 3:
            db_tasks.retrieve_patient()
        elif choice == 4:
            db_tasks.add_report()
        elif choice == 5:
            db_tasks.modify_report()
        elif choice == 6:
            db_tasks.retrieve_report()
        elif choice == 0:
            print("Returning to Main Menu...")
            return
        else:
            print("Invalid choice. Try again.")
        
def admin_menu():
    while True:
        print("1. Maintain Lab Data")
        print("2. Maintain Lab Operator Data")
        print("0. Back")
        choice = input("Enter choice: ")

        if choice == "1":
            db_tasks.maintain_lab_data()
        elif choice == "2":
            db_tasks.maintain_lab_operator_data()
        elif choice == "0":
            break
        else:
            print("Invalid choice")


def main():
    create_database()
    create_tables()
    print("Welcome to Lab Management System")
    role = input("Enter your role (1 - Lab Operator, 2 - Admin): ")

    if role == "1":
        lab_operator_menu()
    elif role == "2":
        if authenticate_admin():
            admin_menu()
        else:
            print("Authentication failed. Access denied.")
    else:
        print("Invalid role selected.")


if __name__ == "__main__":
    main()