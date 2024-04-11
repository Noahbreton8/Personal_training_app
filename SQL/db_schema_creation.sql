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
    billing_id SERIAL NOT NULL UNIQUE,
    amount FLOAT NOT NULL,
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
    email VARCHAR(255) NOT NULL
);

CREATE TABLE Room_Bookings (
    booking_id SERIAL PRIMARY KEY,
    status VARCHAR(255),
    purpose VARCHAR(255),
    room_number INT NOT NULL,
    booking_time TIMESTAMP
);


CREATE TABLE Monitor (
    -- monitor_id SERIAL PRIMARY KEY,
    admin_id INT,
    equipment_id INT,
    FOREIGN KEY (admin_id) REFERENCES Admins(admin_id),
    FOREIGN KEY (equipment_id) REFERENCES Equipment(equipment_id)
);

CREATE TABLE Manages (
    -- manage_id SERIAL PRIMARY KEY,
    admin_id INT,
    booking_id INT,
    FOREIGN KEY (admin_id) REFERENCES Admins(admin_id),
    FOREIGN KEY (booking_id) REFERENCES Room_Bookings(booking_id)
);

CREATE TABLE Classes (
    class_id SERIAL PRIMARY KEY,
    class_name VARCHAR(255),
    class_time TIMESTAMP
);

CREATE TABLE Register (
    class_id INT,
    member_id INT,
    FOREIGN KEY (member_id) REFERENCES Members(member_id),
    FOREIGN KEY (class_id) REFERENCES Classes(class_id)
);

CREATE TABLE Updates (
    -- update_id SERIAL PRIMARY KEY,
    admin_id INT,
    class_id INT,
    FOREIGN KEY (admin_id) REFERENCES Admins(admin_id),
    FOREIGN KEY (class_id) REFERENCES Classes(class_id)
);

CREATE TABLE Oversees (
    -- oversee_id SERIAL PRIMARY KEY,
    admin_id INT,
    billing_id INT,
    FOREIGN KEY (admin_id) REFERENCES Admins(admin_id),
    FOREIGN KEY (billing_id) REFERENCES Members(billing_id)
);

CREATE TABLE Achievement (
    -- achievement_id SERIAL PRIMARY KEY,
    member_id INT,
    achievement VARCHAR(255),
    FOREIGN KEY (member_id) REFERENCES Members(member_id)
);

CREATE TABLE Fitness_Goal (
    -- fitness_goal_id SERIAL PRIMARY KEY,
    member_id INT,
    fitness_goal VARCHAR(255),
    FOREIGN KEY (member_id) REFERENCES Members(member_id)
);

CREATE TABLE Training_Session (
    session_id SERIAL PRIMARY KEY,
    day_of_week VARCHAR(255) NOT NULL,
    session_time TIMESTAMP,
    status VARCHAR(255),
    trainer_id INT,
    member_id INT,
    FOREIGN KEY (trainer_id) REFERENCES Trainers(trainer_id),
    FOREIGN KEY (member_id) REFERENCES Members(member_id)
);

CREATE TABLE Exercise (
    -- exercise_id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    reps INT,
    sets INT,
    member_id INT NOT NULL,
    FOREIGN KEY (member_id) REFERENCES Members(member_id)
);

CREATE TABLE Availability (
    avail_id SERIAL PRIMARY KEY,
    trainer_id INT,
    day_of_week VARCHAR(255) NOT NULL,
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP NOT NULL,
    FOREIGN KEY (trainer_id) REFERENCES Trainers(trainer_id)
);