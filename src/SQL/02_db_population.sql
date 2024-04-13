INSERT INTO Admins (first_name, last_name, phone_number)
VALUES
('john', 'lakeman', '4165512230'),
('victor', 'sandru', '6131234567');

INSERT INTO Members (first_name, last_name, phone_number, email, height, current_weight, amount, payment_status)
VALUES
('alice', 'johnson', '555-123-4567', 'alice.johnson@example.com', 170, 65, 50.00, 'Paid'),
('bob', 'williams', '555-987-6543', 'bob.williams@example.com', 180, 75, 70.00, 'Paid');

INSERT INTO Equipment (equipment_name, maintenance_status)
VALUES
('Bench Press', 'Good'),
('Dumbbells', 'Good'),
('Cable Row Machine', 'Good'),
('Pec Deck', 'Good'),
('Treadmill', 'Bad');

INSERT INTO Trainers (first_name, last_name, phone_number)
VALUES
('kylian', 'mbappe', '123456789'),
('robert', 'lewandowski', '123456789');

INSERT INTO Room_Bookings (status, purpose, room_number, booking_time)
VALUES
('Free', 'Personal Training', 101, '2024-06-22'),
('Free', 'Personal Training', 102, '2024-06-22'),
('Free', 'Personal Training', 103, '2024-06-22'),
('Free', 'Personal Training', 104, '2024-06-22'),
('Free', 'Personal Training', 105, '2024-06-22');

INSERT INTO Monitor (admin_id, equipment_id)
VALUES
(1,1),
(1,2),
(1,3),
(1,4),
(1,5),
(2,1),
(2,2),
(2,3),
(2,4),
(2,5);

INSERT INTO Manages (admin_id, booking_id)
VALUES
(1, 1), (1, 2), (1, 3), (1, 4), (1, 5); --admin 1 deals with room bookings

INSERT INTO Classes (class_name)
VALUES
('Boxing'), ('Yoga'), ('Fitness'), ('Spin Class');

INSERT INTO Updates (admin_id, class_id)
VALUES
(2,1), (2,2), (2,3), (2,4); --admin 2 deals with classes

INSERT INTO Oversees (admin_id, billing_id)
VALUES
(1, 1),
(1, 2); --admin 1 deals with the billing information

INSERT INTO Exercise (name, reps, sets, member_id)
VALUES
('Bench', 8, 3, 1),
('Incline Dumbbell Press', 9, 2, 1),
('Squats', 10, 3, 1),
('Dips', 15, 2, 2),
('Bench', 5, 5, 2),
('Pushups', 20, 2, 2);

INSERT INTO Fitness_Goal (member_id, fitness_goal)
VALUES
(1, 'lose weight and hit 225 on bench'),
(2, 'gain weight and hit 5 plates on squat');


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