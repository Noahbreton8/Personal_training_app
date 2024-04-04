INSERT INTO Admins (first_name, last_name, email, phone_number)
VALUES
("John", "Lakeman", "johnlakeman@gmail.com", "4165512230"),
("Erica", "Oceanman", "ericaoceanman@yahoo.ca", "6478527418");

INSERT INTO Members (first_name, last_name, phone_number, email, height, current_weight, amount, description, payment_status)
VALUES
('Alice', 'Johnson', '555-123-4567', 'alice.johnson@example.com', 170, 65, 50.00, 'fat', 'Paid'),
('Bob', 'Williams', '555-987-6543', 'bob.williams@example.com', 180, 75, 70.00, 'fat', 'Paid');

INSERT INTO Equipment (equipment_name, maintenance_status)
VALUES
('Bench Press', 'Good'),
('Dumbbells', "Good"),
('Cable Row Machine', "Good"),
("Pec Deck", "Good"),
("Treadmill", "Bad");

INSERT INTO Trainers (first_name, last_name, phone_number, email, status)
VALUES
("Kylian", "Mbappe", "123456789", "mbappe@psg.com", "Free"),
("Robert", "Lewandowski", "123456789", "balondor2020@gmail.com", "Busy");

INSERT INTO Room_Bookings (status, purpose, room_number, booking_time)
VALUES
("Free", "Personal Training", 105, '2024-06-22');

INSERT INTO Class_Schedule (room_number, status, class_time)
VALUES
(106, "Good", '2024-06-23');

INSERT INTO Training_Session (status, session_time, trainer_id, member_id)
VALUES
("Finished", "2024-04-03", 1, 1);

INSERT INTO Exercise (name, reps, sets, member_id, session_id)
VALUES
("Bench", 8, 3, 1, 1),
("Incline Dumbbell Press", 9, 2, 1, 1);

INSERT INTO Fitness_Goal (member_id, fitness_goal)
VALUES
(1, "lose weight and hit 225 on bench"),
(2, "gain weight and hit 5 plates on squat");

INSERT INTO Oversees (admin_id, member_id)
VALUES
(1, 1),
(2, 2);