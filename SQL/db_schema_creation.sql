--CREATE DATABASE GymDB;
CREATE TABLE Admins (
    Admin_Id SERIAL PRIMARY KEY,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL,
    PhoneNumber VARCHAR(255) NOT NULL
);

CREATE TABLE Members (
    Member_Id SERIAL PRIMARY KEY,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Phone_Number VARCHAR(255),
    Email VARCHAR(255) NOT NULL,
    Height INT,
    Current_Weight INT,
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
    Phone_Number VARCHAR(255),
    Email VARCHAR(255) NOT NULL,
    Status VARCHAR(255)
);

CREATE TABLE Room_Bookings (
    Booking_Id SERIAL PRIMARY KEY,
    Status VARCHAR(255),
    Purpose VARCHAR(255),
    Room_Number INT NOT NULL,
    Booking_Time TIMESTAMP
);

CREATE TABLE Class_Schedule (
    Schedule_Id SERIAL PRIMARY KEY,
    Room_Number INT NOT NULL,
    Status VARCHAR(255),
    Class_Time TIMESTAMP
);

CREATE TABLE Monitor (
    Admin_Id INT,
    Equipment_Id INT,
    FOREIGN KEY (Admin_Id) REFERENCES Admins(Admin_Id),
    FOREIGN KEY (Equipment_Id) REFERENCES Equipment(Equipment_Id)
);

CREATE TABLE Manages (
    Admin_Id INT,
    Booking_Id INT,
    FOREIGN KEY (Admin_Id) REFERENCES Admins(Admin_Id),
    FOREIGN KEY (Booking_Id) REFERENCES Room_Bookings(Booking_Id)
);

CREATE TABLE Updates (
    Admin_Id INT,
    Schedule_Id INT,
    FOREIGN KEY (Admin_Id) REFERENCES Admins(Admin_Id),
    FOREIGN KEY (Schedule_Id) REFERENCES Class_Schedule(Schedule_Id)
);

CREATE TABLE Classes (
    Class_ID SERIAL PRIMARY KEY,
    Class_Time TIMESTAMP,
    Class_Name VARCHAR(255),
    Schedule_Id INT,
    FOREIGN KEY (Schedule_Id) REFERENCES Class_Schedule(Schedule_Id)
);

CREATE TABLE Oversees (
    Admin_Id INT,
    Member_Id INT,
    FOREIGN KEY (Admin_Id) REFERENCES Admins(Admin_Id),
    FOREIGN KEY (Member_Id) REFERENCES Members(Member_Id)
);

CREATE TABLE Achievement (
    Member_Id INT,
    Achievement VARCHAR(255),
    FOREIGN KEY (Member_Id) REFERENCES Members(Member_Id)
);

CREATE TABLE Fitness_Goal (
    Member_Id INT,
    Fitness_Goal VARCHAR(255),
    FOREIGN KEY (Member_Id) REFERENCES Members(Member_Id)
);

CREATE TABLE Exercise (
    Name VARCHAR(255),
    Reps INT,
    Sets INT,
    Member_Id INT,
    Session_Id INT,
    FOREIGN KEY (Member_Id) REFERENCES Members(Member_Id),
    FOREIGN KEY (Session_Id) REFERENCES Training_Session(Session_Id)
);

CREATE TABLE Training_Session (
    Session_Id SERIAL PRIMARY KEY,
    Status VARCHAR(255),
    Session_Time TIMESTAMP,
    Trainer_Id INT,
    Member_Id INT,
    FOREIGN KEY (Trainer_Id) REFERENCES Trainers(Trainer_Id),
    FOREIGN KEY (Member_Id) REFERENCES Members(Member_Id)
);

CREATE TABLE Organize (
    Trainer_Id INT,
    Class_Id INT,
    FOREIGN KEY (Trainer_Id) REFERENCES Trainers(Trainer_Id),
    FOREIGN KEY (Class_Id) REFERENCES Classes(Class_ID)
);
