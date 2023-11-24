
INSERT INTO Members (FirstName, LastName, DateOfBirth, ContactInfo, Address, MembershipStart, MembershipExpiry) VALUES
('John', 'Doe', '1990-01-15', 'john.doe@email.com', '123 Main St', '2022-01-01', '2023-01-01'),
('Alice', 'Smith', '1985-05-20', 'alice.smith@email.com', '456 Oak St', '2022-02-01', '2023-02-01'),
('Bob', 'Johnson', '1992-09-10', 'bob.johnson@email.com', '789 Pine St', '2022-03-01', '2023-03-01'),
('Eva', 'Williams', '1988-04-25', 'eva.williams@email.com', '101 Cedar St', '2022-04-01', '2023-04-01'),
('Michael', 'Brown', '1995-11-05', 'michael.brown@email.com', '202 Elm St', '2022-05-01', '2023-05-01');


INSERT INTO Trainers (FirstName, LastName, Specialization, ContactInfo) VALUES
('Trainer1', 'Lastname1', 'Strength Training', 'trainer1@email.com'),
('Trainer2', 'Lastname2', 'Cardio Fitness', 'trainer2@email.com'),
('Trainer3', 'Lastname3', 'Yoga', 'trainer3@email.com'),
('Trainer4', 'Lastname4', 'CrossFit', 'trainer4@email.com'),
('Trainer5', 'Lastname5', 'Pilates', 'trainer5@email.com');

INSERT INTO Classes (ClassName, Description, ScheduleDate, ScheduleTime, MaxCapacity, InstructorID) VALUES
('Class1', 'Strength training class', '2022-01-10', '10:00:00', 20, 1),
('Class2', 'Cardio fitness class', '2022-02-15', '12:00:00', 25, 2),
('Class3', 'Yoga class', '2022-03-20', '14:00:00', 15, 3),
('Class4', 'CrossFit class', '2022-04-25', '16:00:00', 30, 4),
('Class5', 'Pilates class', '2022-05-30', '18:00:00', 18, 5);

INSERT INTO Equipment (EquipmentName, QuantityAvailable, EquipmentCondition, LastMaintenanceDate) VALUES
('Treadmill', 5, 'Good', '2022-01-05'),
('Dumbbells', 10, 'Excellent', '2022-02-10'),
('Yoga Mats', 20, 'Fair', '2022-03-15'),
('Kettlebells', 8, 'Good', '2022-04-20'),
('Resistance Bands', 15, 'Excellent', '2022-05-25');


INSERT INTO Attendance (MemberID, ClassID, AttendanceDate, AttendanceStatus) VALUES
(1, 1, '2022-01-10', 'Present'),
(2, 2, '2022-02-15', 'Present'),
(3, 3, '2022-03-20', 'Present'),
(4, 4, '2022-04-25', 'Present'),
(5, 5, '2022-05-30', 'Present');


INSERT INTO Payments (MemberID, PaymentDate, Amount, PaymentMethod) VALUES
(1, '2022-01-05', 50.00, 'Credit Card'),
(2, '2022-02-10', 60.00, 'PayPal'),
(3, '2022-03-15', 40.00, 'Cash'),
(4, '2022-04-20', 70.00, 'Credit Card'),
(5, '2022-05-25', 55.00, 'PayPal');


INSERT INTO Invoices (MemberID, IssueDate, DueDate, TotalAmount) VALUES
(1, '2022-01-05', '2022-01-15', 50.00),
(2, '2022-02-10', '2022-02-20', 60.00),
(3, '2022-03-15', '2022-03-25', 40.00),
(4, '2022-04-20', '2022-04-30', 70.00),
(5, '2022-05-25', '2022-06-05', 55.00);

INSERT INTO PersonalTraining (MemberID, TrainerID) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);
