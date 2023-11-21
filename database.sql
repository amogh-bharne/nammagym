-- Members table with ON DELETE CASCADE
CREATE TABLE Members (
    MemberID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    DateOfBirth DATE,
    ContactInfo VARCHAR(100),
    Address VARCHAR(255),
    MembershipStart DATE,
    MembershipExpiry DATE
);

-- Trainers table with ON DELETE CASCADE
CREATE TABLE Trainers (
    TrainerID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Specialization VARCHAR(100),
    ContactInfo VARCHAR(100)
);

-- Classes table with ON DELETE CASCADE
CREATE TABLE Classes (
    ClassID INT AUTO_INCREMENT PRIMARY KEY,
    ClassName VARCHAR(50) NOT NULL,
    Description TEXT,
    ScheduleDate DATE,
    ScheduleTime TIME,
    MaxCapacity INT,
    InstructorID INT,
    FOREIGN KEY (InstructorID) REFERENCES Trainers(TrainerID) ON DELETE CASCADE
);

-- Equipment table
CREATE TABLE Equipment (
    EquipmentID INT AUTO_INCREMENT PRIMARY KEY,
    EquipmentName VARCHAR(50) NOT NULL,
    QuantityAvailable INT,
    EquipmentCondition VARCHAR(50),
    LastMaintenanceDate DATE
);

-- Attendance table with ON DELETE CASCADE
CREATE TABLE Attendance (
    AttendanceID INT AUTO_INCREMENT PRIMARY KEY,
    MemberID INT,
    ClassID INT,
    AttendanceDate DATE,
    AttendanceStatus VARCHAR(20),
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID) ON DELETE CASCADE,
    FOREIGN KEY (ClassID) REFERENCES Classes(ClassID) ON DELETE CASCADE
);

-- Payments table with ON DELETE CASCADE
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY,
    MemberID INT,
    PaymentDate DATE,
    Amount FLOAT,
    PaymentMethod VARCHAR(50),
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID) ON DELETE CASCADE
);

-- Invoices table with ON DELETE CASCADE
CREATE TABLE Invoices (
    InvoiceID INT AUTO_INCREMENT PRIMARY KEY,
    MemberID INT,
    IssueDate DATE,
    DueDate DATE,
    TotalAmount FLOAT,
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID) ON DELETE CASCADE
);

-- PersonalTraining table with ON DELETE CASCADE
CREATE TABLE PersonalTraining (
    PTID INT AUTO_INCREMENT PRIMARY KEY,
    MemberID INT,
    TrainerID INT,
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID) ON DELETE CASCADE,
    FOREIGN KEY (TrainerID) REFERENCES Trainers(TrainerID) ON DELETE CASCADE,
    CONSTRAINT UC_PersonalTraining UNIQUE (MemberID, TrainerID)
);
