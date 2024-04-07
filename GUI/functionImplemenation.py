import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGroupBox, QLabel, QLineEdit, QPushButton, QMessageBox
import psycopg2

#posgresql credentials
DATABASE_NAME = "finalProject"
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
        
    ####
    #### MEMBER FUNCTIONS
    ####

    ### 1
    def memberRegistration(self, firstName, lastName, phoneNumber, email, height = None, weight = None):
        query = "SELECT firstName, lastName, phone_number, email FROM members"
        rows = self.execute_query(query)
        for i in range(len(rows)):
            if rows[i][0] == firstName and rows[i][1] == lastName and rows[i][2] == str(phoneNumber) and rows[i][3] == email:
                #maybe turn into pop up?
                print("member already exists")
                return -1
        
        addMember = "INSERT INTO members (firstName, lastName, phone_number, email, amount) VALUES (%s, %s, %s, %s, %s)"

        # 0 is the amount due and should be 0 initially
        parameters = (firstName, lastName, phoneNumber, email, 0)
        result = self.execute_query(addMember, parameters)
        if result == -1:
            print("could not insert")
        else:
            print("successfully added new member")
        
        return result
    
    #2
    def updateFirstName(self, memberId, newName):
        query = "UPDATE members SET firstName = %s WHERE member_id = '%s'"
        parameters = (newName, memberId)

        result = self.execute_query(query, parameters)
        if result == -1:
            print("member does not exist")
        else:
            print("successfully updated")
        
        return result

    #2
    def updateLastName(self, memberId, newName):
        query = "UPDATE members SET lastName = %s WHERE member_id = '%s'"
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
        query = "INSERT INTO Fitness_Goal (member_id, fitness_goal) VALUES (%s, %s)"
        parameters = (memberId, goal)

        result = self.execute_query(query, parameters)
        if result == -1:
            print("member does not exist")
        else:
            print("fitness goal added")

    #3
    def addToAchievements(self, memberId, achievement):
        query = "INSERT INTO Achievement (member_id, achievement) VALUES (%s, %s)"
        parameters = (memberId, achievement)

        result = self.execute_query(query, parameters)
        if result == -1:
            print("member does not exist")
        else:
            print("achievement added")

    #3
    def getAllAchievements(self, memberId):
        query = "SELECT achievement FROM Achievement WHERE member_id = '%s'"
        parameters = (memberId,)

        result = self.execute_query(query, parameters)
        if result == []:
            print("no achievements")
        else:
            print("achievements collected")
            print(result)
    
    #3
    def getHealthStats(self, memberId):
        query = "SELECT height, current_weight FROM members WHERE member_id = '%s'"
        parameters = (memberId,)

        result = self.execute_query(query, parameters)
        if result == []:
            print("no member")
        else:
            print("stats collected")
            print(result)

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



    ###
    ### TRAINER FUNCTIONS
    ###
    def trainerRegistration(self, firstName, lastName, phoneNumber, email):
        query = "SELECT firstName, lastName, phone_number, email FROM trainers"
        rows = self.execute_query(query)
        for i in range(len(rows)):
            if rows[i][0] == firstName and rows[i][1] == lastName and rows[i][2] == str(phoneNumber) and rows[i][3] == email:
                #maybe turn into pop up?
                print("trainer already exists")
                return -1
        
        addTrainer = "INSERT INTO trainers (firstName, lastName, phone_number, email, status) VALUES (%s, %s, %s, %s, %s)"

        # available is the status of a new trainer
        parameters = (firstName, lastName, phoneNumber, email, "available")
        result = self.execute_query(addTrainer, parameters)
        if result == -1:
            print("could not insert")
        else:
            print("successfully added new trainer")
        
        return result
    
    #1

    #2
    def getMember(self, firstName, lastName):
        query = "SELECT firstName, lastName, phone_number, email FROM Members WHERE firstName = %s AND lastName = %s"
        parameters = (firstName, lastName)
        result = self.execute_query(query, parameters)
        if result == []:
            print("no members by that name")
        else:
            print(result)
            print("member(s) found")
    
    ###
    ### ADMIN FUNCTIONS
    ###
    def adminRegistration(self, firstName, lastName, phoneNumber, email):
        query = "SELECT firstName, lastName, phonenumber, email FROM admins"
        rows = self.execute_query(query)
        for i in range(len(rows)):
            if rows[i][0] == firstName and rows[i][1] == lastName and rows[i][2] == str(phoneNumber) and rows[i][3] == email:
                #maybe turn into pop up?
                print("admin already exists")
                return -1
        
        addTrainer = "INSERT INTO admins (firstName, lastName, phonenumber, email) VALUES (%s, %s, %s, %s)"

        # available is the status of a new trainer
        parameters = (firstName, lastName, phoneNumber, email)
        result = self.execute_query(addTrainer, parameters)
        if result == -1:
            print("could not insert")
        else:
            print("successfully added new admin")
        
        return result
    
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
            parameters = (result[i], )

            result2 = self.execute_query(query, parameters)
            if result2 != -1:
                finalResults.append(result2)
        
        print(finalResults)


functions_instance = functions()
#functions_instance.memberRegistration("Member", "1", 6131234567, "m1@gmail.com")
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
#functions_instance.getAllAchievements(1)
#functions_instance.getHealthStats(1)
#functions_instance.getExerciseRoutines(1)
#functions_instance.getMember("Member", "1")