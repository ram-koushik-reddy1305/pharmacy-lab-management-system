import mysql.connector
from mysql.connector import Error
from datetime import datetime

DB_CONFIG = {
    'host': 'localhost',
    'database': 'Pharmacydb',
    'user': 'root',
    'password': '1934'
}

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

# --- Input Helpers ---
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Please enter a valid number.")

def get_str(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        else:
            print("❌ This field cannot be empty.")

# -------- Patient Functions --------
def add_patient():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        name = get_str("Enter name: ")
        while True:
            age = get_int("Enter age: ")
            if age>0:
                break
            else:
                print(" please enter valid age which is a postive integer")
        while True:
            gender = get_str("Enter gender (M/F): ").upper()
            if gender in ['M', 'F']:
                break
            else:
                print("❌ Invalid gender. Please enter 'M' for Male or 'F' for Female.")
        while True:
            contact = get_str("Enter contact number: ")
            if contact.isdigit() and 7 <= len(contact) <= 15:
                break
            else:
                print("❌ Invalid contact. Enter digits only (7–15 characters).")

        cursor.execute(
            "INSERT INTO Patients (name, age, gender, contact) VALUES (%s, %s, %s, %s)",
            (name, age, gender, contact)
        )

        commit_choice = get_str("Do you want to commit the changes? (yes/no): ").lower()
        if commit_choice == 'yes':
            conn.commit()
            print("✅ Patient added successfully.")
        else:
            conn.rollback()
            print("❌ Changes rolled back.")
    except Error as e:
        if conn:
            conn.rollback()
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

def modify_patient():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        id = get_int("Enter Patient ID to modify: ")
        name = get_str("Enter new name: ")
        age = get_int("Enter new age: ")
        while True:
            gender = get_str("Enter gender (M/F): ").upper()
            if gender in ['M', 'F']:
                break
            else:
                print("❌ Invalid gender. Please enter 'M' for Male or 'F' for Female.")
        while True:
            contact = get_str("Enter contact number: ")
            if contact.isdigit() and 7 <= len(contact) <= 15:
                break
            else:
                print("❌ Invalid contact. Enter digits only (7–15 characters).")

        cursor.execute(
            "UPDATE Patients SET name = %s, age = %s, gender = %s, contact = %s WHERE patient_id = %s",
            (name, age, gender, contact, id)
        )

        commit_choice = get_str("Do you want to commit the changes? (yes/no): ").lower()
        if commit_choice == 'yes':
            conn.commit()
            print("✅ Patient updated." if cursor.rowcount else "Patient not found.")
        else:
            conn.rollback()
            print("❌ Changes rolled back.")
    except Error as e:
        if conn:
            conn.rollback()
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()
def retrieve_patient():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        patient_id = get_int("Enter Patient ID to retrieve: ")

        cursor.execute("SELECT * FROM Patients WHERE patient_id = %s", (patient_id,))
        record = cursor.fetchone()

        if record:
            print("\n--- Patient Details ---")
            print(f"ID      : {record[0]}")
            print(f"Name    : {record[1]}")
            print(f"Age     : {record[2]}")
            print(f"Gender  : {record[3]}")
            print(f"Contact : {record[4]}")
        else:
            print("❌ No patient found with that ID.")

    except Error as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

# -------- Report Functions --------
def add_report():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        patient_id = get_int("Enter patient ID: ")
        test_name = get_str("Enter test name: ")
        test_date = get_str("Enter test date (YYYY-MM-DD): ")
        result = get_str("Enter test result: ")

        cursor.execute(
            "INSERT INTO TestReports (patient_id, test_name, test_date, result) VALUES (%s, %s, %s, %s)",
            (patient_id, test_name, test_date, result)
        )

        commit_choice = get_str("Do you want to commit the changes? (yes/no): ").lower()
        if commit_choice == 'yes':
            conn.commit()
            print("✅ Report added.")
        else:
            conn.rollback()
            print("❌ Changes rolled back.")
    except Error as e:
        if conn:
            conn.rollback()
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

def modify_report():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        id = get_int("Enter Report ID to modify: ")
        patient_id = get_int("Enter new patient ID: ")
        test_name = get_str("Enter new test name: ")
        test_date = get_str("Enter new test date (YYYY-MM-DD): ")
        result = get_str("Enter new test result: ")

        cursor.execute(
            "UPDATE TestReports SET patient_id = %s, test_name = %s, test_date = %s, result = %s WHERE report_id = %s",
            (patient_id, test_name, test_date, result, id)
        )

        commit_choice = get_str("Do you want to commit the changes? (yes/no): ").lower()
        if commit_choice == 'yes':
            conn.commit()
            print("✅ Report updated." if cursor.rowcount else "Report not found.")
        else:
            conn.rollback()
            print("❌ Changes rolled back.")
    except Error as e:
        if conn:
            conn.rollback()
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()
def retrieve_report():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        report_id = get_int("Enter Report ID to retrieve: ")

        cursor.execute("SELECT * FROM TestReports WHERE report_id = %s", (report_id,))
        record = cursor.fetchone()

        if record:
            print("\n--- Test Report Details ---")
            print(f"Report ID   : {record[0]}")
            print(f"Patient ID  : {record[1]}")
            print(f"Test Name   : {record[2]}")
            print(f"Test Date   : {record[3]}")
            print(f"Result      : {record[4]}")
        else:
            print("❌ No report found with that ID.")

    except Error as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

# -------- Admin Lab Functions --------
def maintain_lab_data():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        while True:
            print("\n--- Maintain Lab Data ---")
            print("1. Add Lab")
            print("2. Update Lab")
            print("3. View All Labs")
            print("0. Back")
            choice = get_str("Enter your choice: ")

            if choice == "1":
                lab_name = get_str("Enter lab name: ")
                specialization = get_str("Enter specialization: ")
                cursor.execute("INSERT INTO Labs (lab_name, lab_specialization) VALUES (%s, %s)", (lab_name, specialization))

                commit_choice = get_str("Do you want to commit the changes? (yes/no): ").lower()
                if commit_choice == 'yes':
                    conn.commit()
                    print("✅ Lab added.")
                else:
                    conn.rollback()
                    print("❌ Changes rolled back.")

            elif choice == "2":
                lab_id = get_int("Enter Lab ID to update: ")
                lab_name = get_str("Enter new lab name: ")
                specialization = get_str("Enter new specialization: ")
                cursor.execute("UPDATE Labs SET lab_name = %s, lab_specialization = %s WHERE lab_id = %s", (lab_name, specialization, lab_id))

                commit_choice = get_str("Do you want to commit the changes? (yes/no): ").lower()
                if commit_choice == 'yes':
                    conn.commit()
                    print("✅ Lab updated." if cursor.rowcount else "Lab not found.")
                else:
                    conn.rollback()
                    print("❌ Changes rolled back.")

            elif choice == "3":
                cursor.execute("SELECT * FROM Labs")
                for row in cursor.fetchall():
                    print(f"Lab ID: {row[0]}, Name: {row[1]}, Specialization: {row[2]}")
            elif choice == "0":
                break
            else:
                print("Invalid choice.")
    except Error as e:
        if conn:
            conn.rollback()
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

# -------- Admin Lab Operator Functions --------
def maintain_lab_operator_data():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        while True:
            print("\n--- Maintain Lab Operator Data ---")
            print("1. Add Lab Operator")
            print("2. Update Lab Operator")
            print("3. View All Lab Operators")
            print("0. Back")
            choice = get_str("Enter your choice: ")

            if choice == "1":
                name = get_str("Enter operator name: ")
                contact = get_str("Enter contact info: ")
                cursor.execute("INSERT INTO LabOperators (name, contact) VALUES (%s, %s)", (name, contact))

                commit_choice = get_str("Do you want to commit the changes? (yes/no): ").lower()
                if commit_choice == 'yes':
                    conn.commit()
                    print("✅ Lab operator added.")
                else:
                    conn.rollback()
                    print("❌ Changes rolled back.")

            elif choice == "2":
                operator_id = get_int("Enter Operator ID to update: ")
                name = get_str("Enter new operator name: ")
                contact = get_str("Enter new contact info: ")
                cursor.execute("UPDATE LabOperators SET name = %s, contact = %s WHERE operator_id = %s", (name, contact, operator_id))

                commit_choice = get_str("Do you want to commit the changes? (yes/no): ").lower()
                if commit_choice == 'yes':
                    conn.commit()
                    print("✅ Lab operator updated." if cursor.rowcount else "Lab operator not found.")
                else:
                    conn.rollback()
                    print("❌ Changes rolled back.")

            elif choice == "3":
                cursor.execute("SELECT * FROM LabOperators")
                for row in cursor.fetchall():
                    print(f"Operator ID: {row[0]}, Name: {row[1]}, Contact: {row[2]}")
            elif choice == "0":
                break
            else:
                print("Invalid choice.")
    except Error as e:
        if conn:
            conn.rollback()
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()
