--CREATE DATABASE GymDB;
CREATE TABLE Admins (
    admin_id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone_number VARCHAR(255) NOT NULL
);

CREATE TABLE Members (
    member_id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    phone_number VARCHAR(255),
    email VARCHAR(255) NOT NULL,
    height INT,
    current_weight INT,
    amount FLOAT NOT NULL,
    description VARCHAR(255),
    payment_status VARCHAR(255)
);

CREATE TABLE Equipment (
    equipment_id SERIAL PRIMARY KEY,
    equipment_name VARCHAR(255) NOT NULL,
    maintenance_status VARCHAR(255)
);

CREATE TABLE Trainers (
    trainer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    phone_number VARCHAR(255),
    email VARCHAR(255) NOT NULL,
    status VARCHAR(255)
);

CREATE TABLE Room_Bookings (
    booking_id SERIAL PRIMARY KEY,
    status VARCHAR(255),
    purpose VARCHAR(255),
    room_number INT NOT NULL,
    booking_time TIMESTAMP
);

CREATE TABLE Class_Schedule (
    schedule_id SERIAL PRIMARY KEY,
    room_number INT NOT NULL,
    status VARCHAR(255),
    class_time TIMESTAMP
);

CREATE TABLE Monitor (
    admin_id INT,
    equipment_id INT,
    FOREIGN KEY (admin_id) REFERENCES Admins(admin_id),
    FOREIGN KEY (equipment_id) REFERENCES Equipment(equipment_id)
);

CREATE TABLE Manages (
    admin_id INT,
    booking_id INT,
    FOREIGN KEY (admin_id) REFERENCES Admins(admin_id),
    FOREIGN KEY (booking_id) REFERENCES Room_Bookings(booking_id)
);

CREATE TABLE Updates (
    admin_id INT,
    schedule_id INT,
    FOREIGN KEY (admin_id) REFERENCES Admins(admin_id),
    FOREIGN KEY (schedule_id) REFERENCES Class_Schedule(schedule_id)
);

CREATE TABLE Classes (
    class_id SERIAL PRIMARY KEY,
    class_time TIMESTAMP,
    class_name VARCHAR(255),
    schedule_id INT,
    FOREIGN KEY (schedule_id) REFERENCES Class_Schedule(schedule_id)
);

CREATE TABLE Oversees (
    admin_id INT,
    member_id INT,
    FOREIGN KEY (admin_id) REFERENCES Admins(admin_id),
    FOREIGN KEY (member_id) REFERENCES Members(member_id)
);

CREATE TABLE Achievement (
    member_id INT,
    achievement VARCHAR(255),
    FOREIGN KEY (member_id) REFERENCES Members(member_id)
);

CREATE TABLE Fitness_Goal (
    member_id INT,
    fitness_goal VARCHAR(255),
    FOREIGN KEY (member_id) REFERENCES Members(member_id)
);

CREATE TABLE Training_Session (
    session_id SERIAL PRIMARY KEY,
    status VARCHAR(255),
    session_time TIMESTAMP,
    trainer_id INT,
    member_id INT,
    FOREIGN KEY (trainer_id) REFERENCES Trainers(trainer_id),
    FOREIGN KEY (member_id) REFERENCES Members(member_id)
);

CREATE TABLE Exercise (
    name VARCHAR(255),
    reps INT,
    sets INT,
    member_id INT,
    session_id INT,
    FOREIGN KEY (member_id) REFERENCES Members(member_id),
    FOREIGN KEY (session_id) REFERENCES Training_Session(session_id)
);

CREATE TABLE Organize (
    trainer_id INT,
    class_id INT,
    FOREIGN KEY (trainer_id) REFERENCES Trainers(trainer_id),
    FOREIGN KEY (class_id) REFERENCES Classes(class_id)
);
