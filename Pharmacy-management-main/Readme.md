# Pharmacy Lab Management System

## Overview
This project implements a **Pharmacy Laboratory Management System** using **Python and MySQL**. It demonstrates how to design and interact with a relational database to manage laboratory operations such as patients, lab operators, laboratories, and test reports.

The system allows users to create and manage records while ensuring data integrity through **transactions, input validation, and relational constraints**.

---

## Features

### Database Management
- Automatically creates the **Pharmacydb** database
- Creates all required relational tables

### Patient Management
- Add new patient records
- Input validation for age, gender, and contact number
- Transaction control using **commit / rollback**

### Laboratory Management
- Store details of laboratories
- Store lab operator information
- Assign operators to labs

### Test Report Management
- Store patient test reports
- Maintain relationships between patients and reports

---

## Database Schema

The system contains the following tables:

### Patients
Stores patient information.

| Column | Description |
|------|-------------|
| patient_id | Unique patient ID |
| name | Patient name |
| age | Patient age |
| gender | Patient gender |
| contact | Contact number |

---

### LabOperators
Stores information about lab operators.

| Column | Description |
|------|-------------|
| operator_id | Unique operator ID |
| name | Operator name |
| contact | Contact number |

---

### Labs
Stores laboratory details.

| Column | Description |
|------|-------------|
| lab_id | Unique lab ID |
| lab_name | Name of the lab |
| lab_specialization | Type of tests handled |

---

### TestReports
Stores patient test results.

| Column | Description |
|------|-------------|
| report_id | Unique report ID |
| patient_id | Linked patient |
| test_name | Name of the test |
| test_date | Date of the test |
| result | Test result |

---

### LabOperatorAssignments
Links lab operators with laboratories.

| Column | Description |
|------|-------------|
| assignment_id | Unique assignment ID |
| operator_id | Assigned operator |
| lab_id | Assigned lab |

---

## Project Structure

```
pharmacy_lab/
│
├── demo.py          # Creates database and tables
├── db_tasks.py      # Contains functions for database operations
├── file.sql         # SQL schema definitions
└── README.md        # Project documentation
```

---

## Technologies Used

- Python
- MySQL
- mysql-connector-python

---

## Installation

### 1 Install dependencies

```bash
pip install mysql-connector-python
```

### 2 Configure database credentials

Edit the configuration in **db_tasks.py**

```python
DB_CONFIG = {
    'host': 'localhost',
    'database': 'Pharmacydb',
    'user': 'root',
    'password': 'your_password'
}
```

### 3 Run the database setup

```bash
python demo.py
```

This will:
- Create the database
- Create required tables

---

## Example Functionality

Example: Adding a patient

```
Enter name: John
Enter age: 25
Enter gender (M/F): M
Enter contact number: 9876543210
Do you want to commit the changes? (yes/no): yes
```

If committed, the patient record is stored in the database.

---

## Learning Outcomes

This project demonstrates:

- Database schema design
- Relational constraints and foreign keys
- Python–MySQL integration
- Input validation
- Transaction handling (commit and rollback)