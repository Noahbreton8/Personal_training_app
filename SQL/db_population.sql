INSERT INTO Admins (first_name, last_name, email, phone_number)
VALUES
('John', 'Lakeman', 'johnlakeman@gmail.com', '4165512230'),
('Erica', 'Oceanman', 'ericaoceanman@yahoo.ca', '6478527418');

INSERT INTO Members (first_name, last_name, phone_number, email, height, current_weight, amount, description, payment_status)
VALUES
('Alice', 'Johnson', '555-123-4567', 'alice.johnson@example.com', 170, 65, 50.00, 'fat', 'Paid'),
('Bob', 'Williams', '555-987-6543', 'bob.williams@example.com', 180, 75, 70.00, 'fat', 'Paid');

INSERT INTO Equipment (equipment_name, maintenance_status)
VALUES
('Bench Press', 'Good'),
('Dumbbells', 'Good'),
('Cable Row Machine', 'Good'),
('Pec Deck', 'Good'),
('Treadmill', 'Bad');

INSERT INTO Trainers (first_name, last_name, phone_number, email, status)
VALUES
('Kylian', 'Mbappe', '123456789', 'mbappe@psg.com', 'Free'),
('Robert', 'Lewandowski', '123456789', 'balondor2020@gmail.com', 'Busy');

INSERT INTO Room_Bookings (status, purpose, room_number, booking_time)
VALUES
('Free', 'Personal Training', 105, '2024-06-22');

INSERT INTO Class_Schedule (room_number, status, class_time)
VALUES
(106, 'Good', '2024-06-23');

INSERT INTO Training_Session (status, session_time, trainer_id, member_id)
VALUES
('Finished', '2024-04-03', (SELECT trainer_id from Trainers WHERE last_name='Kylian'), (SELECT member_id from Members WHERE last_name='Johnson'));

INSERT INTO Exercise (name, reps, sets, member_id)
VALUES
('Bench', 8, 3, (SELECT member_id from Members WHERE last_name='Johnson')),
('Incline Dumbbell Press', 9, 2, (SELECT member_id from Members WHERE last_name='Johnson'));

INSERT INTO Fitness_Goal (member_id, fitness_goal)
VALUES
((SELECT member_id from Members WHERE last_name='Johnson'), 'lose weight and hit 225 on bench'),
((SELECT member_id from Members WHERE last_name='Williams'), 'gain weight and hit 5 plates on squat');

INSERT INTO Oversees (admin_id, member_id)
VALUES
((SELECT admin_id from Admins WHERE last_name='Lakeman'), (SELECT member_id from Members WHERE last_name='Johnson')),
((SELECT admin_id from Admins WHERE last_name='Oceanman'), (SELECT member_id from Members WHERE last_name='Williams'));

INSERT INTO Monitor (admin_id, equipment_id)
VALUES
((SELECT admin_id from Admins WHERE last_name='Lakeman'), (SELECT equipment_id from Equipment WHERE equipment_name='Bench Press'));

INSERT INTO Updates (admin_id, schedule_id)
VALUES
((SELECT admin_id from Admins WHERE last_name='Lakeman'), (SELECT schedule_id from Class_Schedule WHERE room_number=106));

INSERT INTO Classes (class_time, class_name, schedule_id)
VALUES
('2024-06-23', 'Bench Press 101', (SELECT schedule_id from Class_Schedule WHERE room_number=106));

INSERT INTO Achievement (member_id, achievement)
VALUES
((SELECT member_id from Members WHERE last_name='Johnson'), 'hit 135 lbs on bench');

INSERT INTO Organize (trainer_id, class_id)
VALUES
((SELECT trainer_id from Trainers WHERE last_name='Kylian'), (SELECT class_id from Classes WHERE class_name='Bench Press 101'));