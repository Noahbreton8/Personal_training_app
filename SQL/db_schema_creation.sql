--CREATE DATABASE GymDB;

CREATE TABLE Admins (
    Admin_Id SERIAL PRIMARY KEY,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL,
    PhoneNumber INTEGER NOT NULL
);

CREATE TABLE Members (
    Member_Id SERIAL PRIMARY KEY,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Phone_Number INT,
    Email VARCHAR(255) NOT NULL,
    Height INT,
    Current_Weight INT,
    Billing_Id SERIAL PRIMARY KEY,
    Amount FLOAT NOT NULL,
    Description VARCHAR(255),
    Payment_Status VARCHAR(255)
);

CREATE TABLE Equipment (
    Equipment_Id SERIAL PRIMARY KEY,
    Equipment_Name VARCHAR(255) NOT NULL,
    Maintenance_Status VARCHAR(255)
);

CREATE TABLE Trainers (
    Trainer_Id SERIAL PRIMARY KEY,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Phone_Number INT,
    Email VARCHAR(255) NOT NULL,
    Status VARCHAR(255)
);

CREATE TABLE Room_Bookings (
    Booking_Id SERIAL PRIMARY KEY,
    Status VARCHAR(255),
    Purpose VARCHAR(255),
    Room_Number INT NOT NULL,
    Booking_Time DATETIME
);

CREATE TABLE Class_Schedule (
    Schedule_Id SERIAL PRIMARY KEY,
    Room_Number INT NOT NULL,
    Status VARCHAR(255),
    Class_Time DATETIME
);

CREATE TABLE Monitor (
    Admin_Id INT FOREIGN KEY REFERENCES Admins,
    Equipment_Id INT FOREIGN KEY REFERENCES Equipment
);

CREATE TABLE Manages (
    Admin_Id INT FOREIGN KEY REFERENCES Admins,
    Booking_Id INT FOREIGN KEY REFERENCES Room_Bookings
);

CREATE TABLE Updates (
    Admin_Id INT FOREIGN KEY REFERENCES Admins,
    Schedule_Id INT FOREIGN KEY REFERENCES Class_Schedule
);

CREATE TABLE Classes (
    Class_ID SERIAL PRIMARY KEY,
    Class_Time DATETIME,
    Class_Name VARCHAR(255),
    Schedule_Id INT FOREIGN KEY REFERENCES Class_Schedule
);

CREATE TABLE Oversees (
    Admin_Id INT FOREIGN KEY REFERENCES Admins,
    Billing_Id INT FOREIGN KEY REFERENCES Members
);

CREATE TABLE Achievement (
    Member_Id INT FOREIGN KEY REFERENCES Members,
    Achievement VARCHAR(255)
);

CREATE TABLE Fitness_Goal (
    Member_Id INT FOREIGN KEY REFERENCES Members,
    Fitness_Goal VARCHAR(255)
);

CREATE TABLE Exercise (
    Name VARCHAR(255),
    Reps INT,
    Sets INT,
    Member_Id INT FOREIGN KEY REFERENCES Members,
);

CREATE TABLE Training_Session (
    Session_Id SERIAL PRIMARY KEY,
    Status VARCHAR(255),
    Session_Time DATETIME,
    Trainer_Id INT FOREIGN KEY REFERENCES Trainers,
    Member_Id INT FOREIGN KEY REFERENCES Members
);

CREATE TABLE Organize (
    Trainer_Id INT FOREIGN KEY REFERENCES Trainers,
    Class_Id INT FOREIGN KEY REFERENCES Classes
);