import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGroupBox, QLabel, QLineEdit, QPushButton, QMessageBox
import psycopg2
from datetime import datetime
import memberId

#postgresql credentials
DATABASE_NAME = "final"
DATABASE_USER = "postgres"
DATABASE_PASSWORD = "postgres"
DATABASE_HOST = "localhost"
DATABASE_PORT = "5432"

class functions:
    #execute the query passed in
    #with the parameters sepeaated to avoid SQL injection
    def execute_query(self, query, params= None):
        #connect to the database with the credentials above
        conn = psycopg2.connect(
            dbname=DATABASE_NAME,
            user=DATABASE_USER,
            password=DATABASE_PASSWORD,
            host=DATABASE_HOST,
            port=DATABASE_PORT)
        
        try:
            cur = conn.cursor()
            if params:
                cur.execute(query, params)
            else:
                cur.execute(query)

            #return the rows for printing get all students
            if query.strip().lower().startswith("select"):
                student_rows = cur.fetchall()
                cur.close()
                conn.close()
                return student_rows
            else:
                conn.commit()
                cur.close()
                conn.close()
        except psycopg2.Error as e:
            print("Query Execution Error", f"Error executing query: {e}")
            return -1
        

    def get_member_id(self, first_name, last_name, email):
        query = "SELECT member_id FROM Members WHERE first_name = %s AND last_name = %s AND email = %s;"
        params = (first_name, last_name, email)
        result = self.execute_query(query, params)
        if result != -1 and result:
            print("current member id" + str(result[0][0]))
            return result[0][0] 
        else:
            return None
        
    def get_trainer_id(self, first_name, last_name):
        query = "SELECT trainer_id FROM Trainers WHERE first_name = %s AND last_name = %s;"
        params = (first_name, last_name)
        result = self.execute_query(query, params)
        if result != -1 and result:
            #print("current trainer id" + str(result[0][0]))
            return result[0][0] 
        else:
            return None
        
    ####
    #### MEMBER FUNCTIONS
    ####

    ### 1
    def memberRegistration(self, firstName, lastName, phoneNumber, email, height=None, weight=None):
        query = "SELECT member_id, first_Name, last_Name, email FROM members"
        rows = self.execute_query(query)

        if rows == -1:
            print("Failed to execute query")
            return -1

        for row in rows:
            if (row[1], row[2], row[3]) == (firstName, lastName, email):
                print("Member already exists or logging in")
                return row[0]
        
        addMember = "INSERT INTO members (first_Name, last_Name, phone_number, email, amount, height, current_weight) VALUES (%s, %s, %s, %s, %s, %s, %s)"

        # 0 is the amount due and should be 0 initially
        if(weight == '0' and height == '0'):
            return -2
        
        parameters = (firstName, lastName, phoneNumber, email, 0, height.text(), weight.text())
        result = self.execute_query(addMember, parameters)
        if result == -1:
            print("could not insert")
        else:
            print("successfully added new member")
        
        return result
    
    #2
    def updateFirstName(self, memberId, newName):
        query = "UPDATE members SET first_name = %s WHERE member_id = '%s'"
        parameters = (newName, memberId)

        result = self.execute_query(query, parameters)
        if result == -1:
            print("member does not exist")
        else:
            print("successfully updated")
        
        return result

    #2
    def updateLastName(self, memberId, newName):
        query = "UPDATE members SET last_Name = %s WHERE member_id = '%s'"
        parameters = (newName, memberId)

        result = self.execute_query(query, parameters)
        if result == -1:
            print("member does not exist")
        else:
            print("successfully updated")
        
        return result
    
    #2
    def updateEmail(self, memberId, newEmail):
        query = "UPDATE members SET email = %s WHERE member_id = '%s'"
        parameters = (newEmail, memberId)

        result = self.execute_query(query, parameters)
        if result == -1:
            print("member does not exist")
        else:
            print("successfully updated")
        
        return result
    
    #2
    def updatePhone(self, memberId, newPhone):
        query = "UPDATE members SET phone_number = %s WHERE member_id = '%s'"
        parameters = (newPhone, memberId)

        result = self.execute_query(query, parameters)
        if result == -1:
            print("member does not exist")
        else:
            print("successfully updated")
        
        return result
    
    #2
    def updateHeight(self, memberId, newHeight):
        query = "UPDATE members SET height = %s WHERE member_id = '%s'"
        parameters = (newHeight, memberId)

        result = self.execute_query(query, parameters)
        if result == -1:
            print("member does not exist")
        else:
            print("successfully updated")
        
        return result
    
    #2
    def updateWeight(self, memberId, newWeight):
        query = "UPDATE members SET current_weight = %s WHERE member_id = '%s'"
        parameters = (newWeight, memberId)

        result = self.execute_query(query, parameters)
        if result == -1:
            print("member does not exist")
        else:
            print("successfully updated")
        
        return result
    #2
    def addFitnessGoal(self, memberId, goal):
        query = "UPDATE members SET description = %s WHERE member_id = '%s'"
        parameters = (goal, memberId)

        result = self.execute_query(query, parameters)
        if result == -1:
            print("member does not exist")
        else:
            print("fitness goal added")

    #3
    def getAllAchievements(self, memberId):
        query = "SELECT achievement FROM Achievement WHERE member_id = '%s'"
        parameters = (memberId,)

        result = self.execute_query(query, parameters)
        if result == []:
            print("no achievements")
            return "No achievements"
        else:
            print("achievements collected")
            print(result)
            return result[0][0]
    
    #3
    def getWeight(self, memberId):
        query = "SELECT current_weight FROM members WHERE member_id = '%s'"
        parameters = (memberId,)

        result = self.execute_query(query, parameters)
        if result == []:
            print("no weight")
        else:
            print("got weight")
            print(result)
            return result

    #3
    def getExerciseRoutines(self, memberId):
        query = "SELECT name, reps, sets FROM exercise WHERE member_id = '%s'"
        parameters = (memberId,)

        result = self.execute_query(query, parameters)
        if result == []:
            print("no member")
        else:
            print("exercises collected")
            print(result)
            return result

    #4
    def getTrainers(self):
        query = "SELECT * FROM trainers"

        result = self.execute_query(query)
        if result == []:
            print("no trainers")
        else:
            print("trainers collected")
            print(result)
            return result
        
    def getTrainerSessions(self, trainer_id):
        query = "SELECT day_of_week, session_time, status, member_id FROM Training_Session WHERE trainer_id = '%s' ORDER BY session_id ASC"
        params = (trainer_id,)

        result = self.execute_query(query, params)
        if result == []:
            print("no training sessions")
        else:
            print("training sessions found")
            print(result)
            return result

        return

    ###
    ### TRAINER FUNCTIONS
    ###
    def trainerLogin(self, firstName, lastName, phoneNumber, email):
        query = "SELECT first_name, last_name, phone_number, email FROM trainers"
        rows = self.execute_query(query)

        if rows == -1:
            print("Failed to execute query")
            return -1

        for i in range(len(rows)):
            if rows[i][0] == firstName and rows[i][1] == lastName:
                #maybe turn into pop up?
                print("successful login")
                return 0
        return -1

    #2
    def getMember(self, firstName, lastName):
        query = "SELECT first_name, last_name, phone_number, email, current_weight, height FROM Members WHERE first_name = %s AND last_name = %s"
        parameters = (firstName, lastName)
        result = self.execute_query(query, parameters)
        if result == []:
            print("no members by that name")
        else:
            print(result)
            print("member(s) found")
        return result
    
    
    #2
    def addToAchievements(self, memberId, achievement):
        query = "INSERT INTO Achievement (member_id, achievement) VALUES (%s, %s)"
        parameters = (memberId, achievement)

        result = self.execute_query(query, parameters)
        if result == -1:
            print("member does not exist")
        else:
            print("achievement added")

    #1
    def getAvailability(self, first_name, last_name):
        trainer_id = self.get_trainer_id(first_name, last_name)
        query = "SELECT * FROM Availability WHERE trainer_id = %s"
        parameters = (trainer_id,) 

        result = self.execute_query(query, parameters)
        if result == -1:
            print("Failed to get availability")
        else:
            print(result)
            return result

    #1
    def setAvailability(self, column, day, first_name, last_name, value):
        trainer_id = self.get_trainer_id(first_name, last_name)
        query = "UPDATE Availability SET {} = %s WHERE trainer_id = %s and day_of_week = %s".format(column)
        
        timestamp_value = datetime.strptime(value, "%H:%M").strftime("%Y-%m-%d %H:%M:%S")
        
        parameters = (timestamp_value, trainer_id, day)

        result = self.execute_query(query, parameters)
        if result == -1:
            print("failed to set avail")
        else:
            print("set avail")
        return result
    
    #1
    def updateTrainerSessions(self, first_name, last_name, day, start_time, end_time):
        #start_time is an integer representing the hour

        trainer_id = self.get_trainer_id(first_name, last_name)

        query = "SELECT status FROM Training_Session WHERE trainer_id = '%s' AND day_of_week = %s ORDER BY session_time ASC"
        params = (trainer_id, day)

        trainingTable = self.execute_query(query, params)

        for i in range(9, 17):
            if (i < start_time and trainingTable[i-9][0] != "NOT AVAILABLE") or (i > end_time and trainingTable != "NOT AVAILABLE"):
                if i == 9:
                    session_time = "2024-04-09 0" + str(i) + ":00:00"
                else:
                    session_time = "2024-04-09 " + str(i) + ":00:00"
                query = "UPDATE Training_Session SET status = 'NOT AVAILABLE' WHERE trainer_id = '%s' AND day_of_week = %s AND session_time = %s"
                parameters = (trainer_id, day, session_time)
                self.execute_query(query, parameters)

            elif i >= start_time and i < end_time and trainingTable[i-9][0] == "NOT AVAILABLE":
                if i == 9:
                    session_time = "2024-04-09 0" + str(i) + ":00:00"
                else:
                    session_time = "2024-04-09 " + str(i) + ":00:00"
                query = "UPDATE Training_Session SET status = 'AVAILABLE' WHERE trainer_id = '%s' AND day_of_week = %s AND session_time = %s"
                parameters = (trainer_id, day, session_time)
                self.execute_query(query, parameters)


    def removeTrainingSession(self, day, date, trainer_id):
        query = "UPDATE Training_Session SET status = 'AVAILABLE' WHERE day_of_week = %s AND status = 'BOOKED' AND session_time = %s AND trainer_id = '%s'"
        
        parameters = (day, date, trainer_id,) 

        result = self.execute_query(query, parameters)
        if result == -1:
            print("Failed to remove training session")
        else:
            print("successful delete")
            return result

    def addTrainingSession(self, day, date, trainer_id):
        query = "UPDATE Training_Session SET status = 'BOOKED', member_id = '%s' WHERE day_of_week = %s AND session_time = %s AND trainer_id = '%s'"
        parameters = (memberId.memberId, day, date, trainer_id,) 

        result = self.execute_query(query, parameters)
        if result == -1:
            print("Failed to add training session")
        else:
            print("successful add")
            return result

    
    ###
    ### ADMIN FUNCTIONS
    ###
    def adminLogin(self, firstName, lastName):
        query = "SELECT first_name, last_name, phone_number, email FROM admins"
        rows = self.execute_query(query)

        if rows == -1:
            print("Failed to execute query")
            return -1

        for i in range(len(rows)):
            if rows[i][0] == firstName and rows[i][1] == lastName:
                #maybe turn into pop up?
                print("successful login")
                return 0
        return -1
    
    #2
    def getEquipment(self, adminId):
        query = "SELECT equipment_id FROM Monitor WHERE admin_id = '%s'"
        parameters = (adminId,)
        result = self.execute_query(query, parameters)
        if result == []:
            print("no equipment mointored by that admin")
            return -1
        
        print(result)
        print("equipment found")

        finalResults = []
        for i in range(len(result)):
            query = "SELECT equipment_name, maintenance_status FROM Equipment WHERE equipment_id = '%s'"
            parameters = (result[i][0], )

            result2 = self.execute_query(query, parameters)
            if result2 != -1:
                finalResults.append(result2)
        
        print(finalResults)
        return finalResults

    #3
    def getRooms(self):
        query = "SELECT * FROM Room_Bookings"
        parameters = ()
        result = self.execute_query(query, parameters)
        if result == []:
            print("no room bookings")
            return -1
        
        print(result)
        print("room bookings")

        return result
    
    #3
    def updateRoomValue(self, room_number, column_name, value):
        query = f"UPDATE Room_Bookings SET {column_name} = %s WHERE room_number = %s"
        parameters = (value, room_number)

        result = self.execute_query(query, parameters)
        if result == -1:
            print("failed to update room")
        else:
            print("updateRoom")

    #3
    def getClasses(self):
        query = "SELECT class_name, class_time FROM Classes"
        result = self.execute_query(query)
        if result == []:
            print("No classes")
            return -1
        
        print("Here are the classes")
        print(result)
        return result
    
    def updateClassValue(self, class_name, column_name, newVal):
        column_name_parts = column_name.split(" ")
        realColumnName = column_name_parts[0] + "_" + column_name_parts[1]
        query = f"UPDATE Classes SET {realColumnName.lower()} = %s WHERE class_name = %s"

        if (newVal != None):
            newVal = datetime.strptime(newVal, '%Y-%m-%d %H:%M:%S')


        parameters = (newVal, class_name)

        result = self.execute_query(query, parameters)

        if result == -1:
            print("failed to update class")
            return None
        else:
            print("class updated")
            return 1
        
    def getActiveClasses(self):
        query = "SELECT * FROM Classes WHERE class_time IS NOT NULL"
        result = self.execute_query(query)
        if result == []:
            print("No classes")
            return -1
        
        print("Here are the active classes")
        print(result)
        return result
    
    def isMemberInClass(self, member_id, class_id):
        query = "SELECT * FROM Register WHERE class_id = '%s' AND member_id = '%s'"
        params = (class_id, member_id)
        result = self.execute_query(query, params)
        if result == []:
            return False
        return True
    
    def updateClassesRegistration(self, member_id, class_name):
        query = "SELECT class_id FROM Classes WHERE class_name = %s"
        params = (class_name,)
        class_id = self.execute_query(query, params)[0][0]

        query = "INSERT INTO Register (class_id, member_id) VALUES (%s, %s)"
        params=(class_id, member_id)
        result = self.execute_query(query, params)

        print()

    #4
    def checkMemberPaid(self, memberId):
        query = "SELECT payment_status FROM Members WHERE member_id = %s"
        parameters = (memberId)
        result = self.execute_query(query, parameters)

        if result[0][0] == 'Paid':
            print("paid")
            return 0
        else:
            print("unpaid")
            return -1
        
    def toggleMemberPaymentStatus(self, billing_id):
        query = "SELECT payment_status FROM Members WHERE billing_id = %s"
        parameters = (billing_id)
        result = self.execute_query(query, parameters)

        if result[0][0] == 'Paid':
            paymentStatus = "Unpaid"
        else:
            paymentStatus = "Paid"

        query = f"UPDATE Members SET payment_status = %s WHERE billing_id = %s"
        parameters = (paymentStatus, billing_id)

        result = self.execute_query(query, parameters)

        if result == -1:
            print("failed to toggle member payment status")
        else:
            print(f"Toggled member payment status to {paymentStatus}")


functions_instance = functions()
# functions_instance.checkMemberPaid("1")
# functions_instance.toggleMemberPaymentStatus("1")
# functions_instance.checkMemberPaid("1")
# functions_instance.memberRegistration("Member", "1", 6131234567, "m1@gmail.com")
#functions_instance.trainerRegistration("Trainer", "1", 6137654321, "t1@gmail.com")
#functions_instance.adminRegistration("Admin", "1", 6137162534, "a1@gmail.com")
#functions_instance.updateFirstName(1, "New")
#functions_instance.updateLastName(1, "newLast")
#functions_instance.updateEmail(1, "newEmail")
#functions_instance.updatePhone(1, "1234567890")
#functions_instance.updateHeight(1, 6)
#functions_instance.updateWeight(1, 200)
#functions_instance.addFitnessGoal(1, "reach 250 pounds")
#functions_instance.addToAchievements(1, "reach 250 pounds")
# functions_instance.getAllAchievements(1)
#functions_instance.getHealthStats(1)
#functions_instance.getExerciseRoutines(1)
# functions_instance.getMember("Alice", "Johnson")
#functions_instance.setUpTrainingSession(1, 'Monday', "09:00", "15:00")
#functions_instance.updateTrainerSessions("Kylian", "Mbappe", "Monday", 11, 13)