INSERT INTO Admins (first_name, last_name, email, phone_number)
VALUES
('John', 'Lakeman', 'johnlakeman@gmail.com', '4165512230');

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

INSERT INTO Trainers (first_name, last_name, phone_number, email)
VALUES
('Kylian', 'Mbappe', '123456789', 'mbappe@psg.com'),
('Robert', 'Lewandowski', '123456789', 'balondor2020@gmail.com');

INSERT INTO Room_Bookings (status, purpose, room_number, booking_time)
VALUES
('Free', 'Personal Training', 101, '2024-06-22'),
('Free', 'Personal Training', 102, '2024-06-22'),
('Free', 'Personal Training', 103, '2024-06-22'),
('Free', 'Personal Training', 104, '2024-06-22'),
('Free', 'Personal Training', 105, '2024-06-22');

INSERT INTO Class_Schedule (room_number, status, class_time)
VALUES
(106, 'Good', '2024-06-23');

-- INSERT INTO Training_Session (status, session_time, trainer_id, member_id)
-- VALUES
-- ('Finished', '2024-04-03', 1, 1),
-- ('Finished', '2024-04-03', 2, 2);

INSERT INTO Exercise (name, reps, sets, member_id)
VALUES
('Bench', 8, 3, 1),
('Incline Dumbbell Press', 9, 2, 1);

INSERT INTO Fitness_Goal (member_id, fitness_goal)
VALUES
(1, 'lose weight and hit 225 on bench'),
(2, 'gain weight and hit 5 plates on squat');

INSERT INTO Oversees (admin_id, member_id)
VALUES
(1, 1),
(1, 2);

INSERT INTO Monitor (admin_id, equipment_id)
VALUES
(1,1),
(1,2),
(1,3),
(1,4),
(1,5);

--trainer 1
INSERT INTO Availability (trainer_id, day_of_week, start_time, end_time)
VALUES 
    (1, 'Monday', '2024-04-09 09:00:00', '2024-04-09 17:00:00'),
    (1, 'Tuesday', '2024-04-10 09:00:00', '2024-04-10 17:00:00'),
    (1, 'Wednesday', '2024-04-11 09:00:00', '2024-04-11 17:00:00'),
    (1, 'Thursday', '2024-04-12 09:00:00', '2024-04-12 17:00:00'),
    (1, 'Friday', '2024-04-13 09:00:00', '2024-04-13 17:00:00'),
    (1, 'Saturday', '2024-04-14 09:00:00', '2024-04-14 17:00:00'),
    (1, 'Sunday', '2024-04-15 09:00:00', '2024-04-15 17:00:00');

--trainer 2
INSERT INTO Availability (trainer_id, day_of_week, start_time, end_time)
VALUES 
    (2, 'Monday', '2024-04-09 09:00:00', '2024-04-09 17:00:00'),
    (2, 'Tuesday', '2024-04-10 09:00:00', '2024-04-10 17:00:00'),
    (2, 'Wednesday', '2024-04-11 09:00:00', '2024-04-11 17:00:00'),
    (2, 'Thursday', '2024-04-12 09:00:00', '2024-04-12 17:00:00'),
    (2, 'Friday', '2024-04-13 09:00:00', '2024-04-13 17:00:00'),
    (2, 'Saturday', '2024-04-14 09:00:00', '2024-04-14 17:00:00'),
    (2, 'Sunday', '2024-04-15 09:00:00', '2024-04-15 17:00:00');


--trainer 1
INSERT INTO Training_Session (trainer_id, day_of_week, session_time, status)
VALUES 
    (1, 'Monday', '2024-04-09 09:00:00', 'NOT AVAILABLE'),
    (1, 'Monday', '2024-04-09 10:00:00', 'NOT AVAILABLE'),
    (1, 'Monday', '2024-04-09 11:00:00', 'NOT AVAILABLE'),
    (1, 'Monday', '2024-04-09 12:00:00', 'NOT AVAILABLE'),
    (1, 'Monday', '2024-04-09 13:00:00', 'NOT AVAILABLE'),
    (1, 'Monday', '2024-04-09 14:00:00', 'NOT AVAILABLE'),
    (1, 'Monday', '2024-04-09 15:00:00', 'NOT AVAILABLE'),
    (1, 'Monday', '2024-04-09 16:00:00', 'NOT AVAILABLE'),
    (1, 'Tuesday', '2024-04-09 09:00:00', 'NOT AVAILABLE'),
    (1, 'Tuesday', '2024-04-09 10:00:00', 'NOT AVAILABLE'),
    (1, 'Tuesday', '2024-04-09 11:00:00', 'NOT AVAILABLE'),
    (1, 'Tuesday', '2024-04-09 12:00:00', 'NOT AVAILABLE'),
    (1, 'Tuesday', '2024-04-09 13:00:00', 'NOT AVAILABLE'),
    (1, 'Tuesday', '2024-04-09 14:00:00', 'NOT AVAILABLE'),
    (1, 'Tuesday', '2024-04-09 15:00:00', 'NOT AVAILABLE'),
    (1, 'Tuesday', '2024-04-09 16:00:00', 'NOT AVAILABLE'),
    (1, 'Wednesday', '2024-04-09 09:00:00', 'NOT AVAILABLE'),
    (1, 'Wednesday', '2024-04-09 10:00:00', 'NOT AVAILABLE'),
    (1, 'Wednesday', '2024-04-09 11:00:00', 'NOT AVAILABLE'),
    (1, 'Wednesday', '2024-04-09 12:00:00', 'NOT AVAILABLE'),
    (1, 'Wednesday', '2024-04-09 13:00:00', 'NOT AVAILABLE'),
    (1, 'Wednesday', '2024-04-09 14:00:00', 'NOT AVAILABLE'),
    (1, 'Wednesday', '2024-04-09 15:00:00', 'NOT AVAILABLE'),
    (1, 'Wednesday', '2024-04-09 16:00:00', 'NOT AVAILABLE'),
    (1, 'Thursday', '2024-04-09 09:00:00', 'NOT AVAILABLE'),
    (1, 'Thursday', '2024-04-09 10:00:00', 'NOT AVAILABLE'),
    (1, 'Thursday', '2024-04-09 11:00:00', 'NOT AVAILABLE'),
    (1, 'Thursday', '2024-04-09 12:00:00', 'NOT AVAILABLE'),
    (1, 'Thursday', '2024-04-09 13:00:00', 'NOT AVAILABLE'),
    (1, 'Thursday', '2024-04-09 14:00:00', 'NOT AVAILABLE'),
    (1, 'Thursday', '2024-04-09 15:00:00', 'NOT AVAILABLE'),
    (1, 'Thursday', '2024-04-09 16:00:00', 'NOT AVAILABLE'),
    (1, 'Friday', '2024-04-09 09:00:00', 'NOT AVAILABLE'),
    (1, 'Friday', '2024-04-09 10:00:00', 'NOT AVAILABLE'),
    (1, 'Friday', '2024-04-09 11:00:00', 'NOT AVAILABLE'),
    (1, 'Friday', '2024-04-09 12:00:00', 'NOT AVAILABLE'),
    (1, 'Friday', '2024-04-09 13:00:00', 'NOT AVAILABLE'),
    (1, 'Friday', '2024-04-09 14:00:00', 'NOT AVAILABLE'),
    (1, 'Friday', '2024-04-09 15:00:00', 'NOT AVAILABLE'),
    (1, 'Friday', '2024-04-09 16:00:00', 'NOT AVAILABLE'),
    (1, 'Saturday', '2024-04-09 09:00:00', 'NOT AVAILABLE'),
    (1, 'Saturday', '2024-04-09 10:00:00', 'NOT AVAILABLE'),
    (1, 'Saturday', '2024-04-09 11:00:00', 'NOT AVAILABLE'),
    (1, 'Saturday', '2024-04-09 12:00:00', 'NOT AVAILABLE'),
    (1, 'Saturday', '2024-04-09 13:00:00', 'NOT AVAILABLE'),
    (1, 'Saturday', '2024-04-09 14:00:00', 'NOT AVAILABLE'),
    (1, 'Saturday', '2024-04-09 15:00:00', 'NOT AVAILABLE'),
    (1, 'Saturday', '2024-04-09 16:00:00', 'NOT AVAILABLE'),
    (1, 'Sunday', '2024-04-09 09:00:00', 'NOT AVAILABLE'),
    (1, 'Sunday', '2024-04-09 10:00:00', 'NOT AVAILABLE'),
    (1, 'Sunday', '2024-04-09 11:00:00', 'NOT AVAILABLE'),
    (1, 'Sunday', '2024-04-09 12:00:00', 'NOT AVAILABLE'),
    (1, 'Sunday', '2024-04-09 13:00:00', 'NOT AVAILABLE'),
    (1, 'Sunday', '2024-04-09 14:00:00', 'NOT AVAILABLE'),
    (1, 'Sunday', '2024-04-09 15:00:00', 'NOT AVAILABLE'),
    (1, 'Sunday', '2024-04-09 16:00:00', 'NOT AVAILABLE');

--trainer 2
INSERT INTO Training_Session (trainer_id, day_of_week, session_time, status)
VALUES 
    (2, 'Monday', '2024-04-09 09:00:00', 'NOT AVAILABLE'),
    (2, 'Monday', '2024-04-09 10:00:00', 'NOT AVAILABLE'),
    (2, 'Monday', '2024-04-09 11:00:00', 'NOT AVAILABLE'),
    (2, 'Monday', '2024-04-09 12:00:00', 'NOT AVAILABLE'),
    (2, 'Monday', '2024-04-09 13:00:00', 'NOT AVAILABLE'),
    (2, 'Monday', '2024-04-09 14:00:00', 'NOT AVAILABLE'),
    (2, 'Monday', '2024-04-09 15:00:00', 'NOT AVAILABLE'),
    (2, 'Monday', '2024-04-09 16:00:00', 'NOT AVAILABLE'),
    (2, 'Tuesday', '2024-04-09 09:00:00', 'NOT AVAILABLE'),
    (2, 'Tuesday', '2024-04-09 10:00:00', 'NOT AVAILABLE'),
    (2, 'Tuesday', '2024-04-09 11:00:00', 'NOT AVAILABLE'),
    (2, 'Tuesday', '2024-04-09 12:00:00', 'NOT AVAILABLE'),
    (2, 'Tuesday', '2024-04-09 13:00:00', 'NOT AVAILABLE'),
    (2, 'Tuesday', '2024-04-09 14:00:00', 'NOT AVAILABLE'),
    (2, 'Tuesday', '2024-04-09 15:00:00', 'NOT AVAILABLE'),
    (2, 'Tuesday', '2024-04-09 16:00:00', 'NOT AVAILABLE'),
    (2, 'Wednesday', '2024-04-09 09:00:00', 'NOT AVAILABLE'),
    (2, 'Wednesday', '2024-04-09 10:00:00', 'NOT AVAILABLE'),
    (2, 'Wednesday', '2024-04-09 11:00:00', 'NOT AVAILABLE'),
    (2, 'Wednesday', '2024-04-09 12:00:00', 'NOT AVAILABLE'),
    (2, 'Wednesday', '2024-04-09 13:00:00', 'NOT AVAILABLE'),
    (2, 'Wednesday', '2024-04-09 14:00:00', 'NOT AVAILABLE'),
    (2, 'Wednesday', '2024-04-09 15:00:00', 'NOT AVAILABLE'),
    (2, 'Wednesday', '2024-04-09 16:00:00', 'NOT AVAILABLE'),
    (2, 'Thursday', '2024-04-09 09:00:00', 'NOT AVAILABLE'),
    (2, 'Thursday', '2024-04-09 10:00:00', 'NOT AVAILABLE'),
    (2, 'Thursday', '2024-04-09 11:00:00', 'NOT AVAILABLE'),
    (2, 'Thursday', '2024-04-09 12:00:00', 'NOT AVAILABLE'),
    (2, 'Thursday', '2024-04-09 13:00:00', 'NOT AVAILABLE'),
    (2, 'Thursday', '2024-04-09 14:00:00', 'NOT AVAILABLE'),
    (2, 'Thursday', '2024-04-09 15:00:00', 'NOT AVAILABLE'),
    (2, 'Thursday', '2024-04-09 16:00:00', 'NOT AVAILABLE'),
    (2, 'Friday', '2024-04-09 09:00:00', 'NOT AVAILABLE'),
    (2, 'Friday', '2024-04-09 10:00:00', 'NOT AVAILABLE'),
    (2, 'Friday', '2024-04-09 11:00:00', 'NOT AVAILABLE'),
    (2, 'Friday', '2024-04-09 12:00:00', 'NOT AVAILABLE'),
    (2, 'Friday', '2024-04-09 13:00:00', 'NOT AVAILABLE'),
    (2, 'Friday', '2024-04-09 14:00:00', 'NOT AVAILABLE'),
    (2, 'Friday', '2024-04-09 15:00:00', 'NOT AVAILABLE'),
    (2, 'Friday', '2024-04-09 16:00:00', 'NOT AVAILABLE'),
    (2, 'Saturday', '2024-04-09 09:00:00', 'NOT AVAILABLE'),
    (2, 'Saturday', '2024-04-09 10:00:00', 'NOT AVAILABLE'),
    (2, 'Saturday', '2024-04-09 11:00:00', 'NOT AVAILABLE'),
    (2, 'Saturday', '2024-04-09 12:00:00', 'NOT AVAILABLE'),
    (2, 'Saturday', '2024-04-09 13:00:00', 'NOT AVAILABLE'),
    (2, 'Saturday', '2024-04-09 14:00:00', 'NOT AVAILABLE'),
    (2, 'Saturday', '2024-04-09 15:00:00', 'NOT AVAILABLE'),
    (2, 'Saturday', '2024-04-09 16:00:00', 'NOT AVAILABLE'),
    (2, 'Sunday', '2024-04-09 09:00:00', 'NOT AVAILABLE'),
    (2, 'Sunday', '2024-04-09 10:00:00', 'NOT AVAILABLE'),
    (2, 'Sunday', '2024-04-09 11:00:00', 'NOT AVAILABLE'),
    (2, 'Sunday', '2024-04-09 12:00:00', 'NOT AVAILABLE'),
    (2, 'Sunday', '2024-04-09 13:00:00', 'NOT AVAILABLE'),
    (2, 'Sunday', '2024-04-09 14:00:00', 'NOT AVAILABLE'),
    (2, 'Sunday', '2024-04-09 15:00:00', 'NOT AVAILABLE'),
    (2, 'Sunday', '2024-04-09 16:00:00', 'NOT AVAILABLE');