CREATE TABLE Patients (
    patient_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    gender VARCHAR(10) NOT NULL,
    contact VARCHAR(15) NOT NULL
);

CREATE TABLE LabOperators (
    operator_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    contact VARCHAR(15) NOT NULL
);
CREATE TABLE Labs (
    lab_id INT PRIMARY,
    lab_name VARCHAR(100) NOT NULL,
    lab_specialization VARCHAR(100) NOT NULL
);

CREATE TABLE TestReports (
    report_id INT PRIMARY KEY,
    patient_id INT,
    test_name VARCHAR(100) NOT NULL,
    test_date DATE NOT NULL,
    result TEXT NOT NULL,
        FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
);

CREATE TABLE LabOperatorAssignments (
    assignment_id INT PRIMARY KEY ,
    operator_id INT,
    lab_id INT,
    FOREIGN KEY (operator_id) REFERENCES LabOperators(operator_id),
    FOREIGN KEY (lab_id) REFERENCES Labs(lab_id)
);
