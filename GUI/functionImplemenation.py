import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGroupBox, QLabel, QLineEdit, QPushButton, QMessageBox
import psycopg2

#posgresql credentials
DATABASE_NAME = "finalProject"
DATABASE_USER = "postgres"
DATABASE_PASSWORD = "student"
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
        
        addMember = "INSERT INTO members (first_Name, last_Name, phone_number, email, amount, height, current_weight, description) VALUES (%s, %s, %s, %s, %s, %s, %s, '')"

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
    
    #1

    #2
    def getMember(self, firstName, lastName):
        query = "SELECT first_name, last_name, phone_number, email, current_weight, height, description FROM Members WHERE first_name = %s AND last_name = %s"
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