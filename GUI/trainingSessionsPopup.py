from functionImplemenation import functions
from PyQt5.QtWidgets import QRadioButton, QMessageBox, QPushButton, QDialog, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QTimeEdit
from PyQt5.QtCore import QSize, Qt
from PyQt5 import QtCore

#trainer #1
class setAvail(QDialog):
    def __init__(self, first_name, last_name):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        
        self.setWindowTitle('Training Sessions (Trainers)')
        
        layout = QVBoxLayout()
        layout.addWidget(QLabel('Set Availability for Training Sessions'))
        
        self.table = QTableWidget()
        self.table.setColumnCount(3) 
        self.table.setHorizontalHeaderLabels(['Day', 'Start', 'End'])
        
        func = functions()
        results = func.getAvailability(self.first_name, self.last_name)
        
        self.table.setRowCount(len(results))
        
        for row, data in enumerate(results):
            for column, item in enumerate(data[2:]): 
                if column == 1 or column == 2: 
                    time_edit = QTimeEdit()
                    time_edit.setDisplayFormat('HH:mm')  
                    if item: 
                        time = QtCore.QTime.fromString(item.strftime('%H:%M'), 'HH:mm')
                        time_edit.setTime(time)
                    self.table.setCellWidget(row, column, time_edit)
                else:
                    self.table.setItem(row, column, QTableWidgetItem(str(item)))
        
        #190 fits nicely with width 200, no scrollwheel
        self.table.setColumnWidth(0, 194)
        self.table.setColumnWidth(1, 194)
        self.table.setColumnWidth(2, 194)

        #set width
        self.table.setMinimumSize(QSize(600, 270))    
        layout.addWidget(self.table)

        update_button = QPushButton('Update!')
        layout.addWidget(update_button)
        update_button.clicked.connect(self.updateAvail)
        self.setLayout(layout)



    def updateAvail(self):
        success = True
        
        func = functions()
        for row in range(self.table.rowCount()):  
            day = self.table.item(row, 0).text()  
            start_time_item = self.table.cellWidget(row, 1) 
            end_time_item = self.table.cellWidget(row, 2)  
            start_time = start_time_item.time().toString('HH:mm')  
            end_time = end_time_item.time().toString('HH:mm')

            startHour = int(start_time.split(':')[0]) #gets the hour of start_time as an integer
            endHour = int(end_time.split(':')[0])
            
            func.updateTrainerSessions(self.first_name, self.last_name, day, startHour, endHour)

            start_result = func.setAvailability('start_time', day, self.first_name, self.last_name, start_time)
            end_result = func.setAvailability('end_time', day, self.first_name, self.last_name, end_time)
            
            if start_result == -1 or end_result == -1:
                success = False 

        if success:
            QMessageBox.information(self, 'Availability', 'Availability updated!')  
        else: 
            QMessageBox.warning(self, 'Error', 'Failed to change availability:(')


#member #4
class bookTrainingPopup(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Training Sessions (trainers)")
        self.layout = QVBoxLayout()
        self.layout.addWidget(QLabel("Book availability for Training Sessions"))
        self.trainer = ""
        self.func = functions()

        result = self.func.getTrainers()
        first_name_t1 = result[0][1]
        last_name_t1 = result[0][2]
        first_name_t2 = result[1][1]
        last_name_t2 = result[1][2]
        self.trainer1_button = QRadioButton(first_name_t1 + " " + last_name_t1)
        self.trainer2_button = QRadioButton(first_name_t2 + " " + last_name_t2)

        self.select_button = QPushButton("Select Trainer")
        self.select_button.setDisabled(True)

        self.layout.addWidget(self.trainer1_button)
        self.layout.addWidget(self.trainer2_button)
        self.layout.addWidget(self.select_button)

        self.trainer1_button.toggled.connect(self.update_select_button_state)
        self.trainer2_button.toggled.connect(self.update_select_button_state)

        self.select_button.clicked.connect(self.display_trainer_sessions)

        self.update_button = QPushButton("Update!")
        self.update_button.clicked.connect(self.update_trainer_sessions)

        self.setLayout(self.layout)

    def update_select_button_state(self):
        # Enable the button only if one of the radio buttons is selected
        self.select_button.setEnabled(self.trainer1_button.isChecked() or self.trainer2_button.isChecked())

    def display_trainer_sessions(self):
        if self.trainer1_button.isChecked():
            self.trainer = 1
        elif self.trainer2_button.isChecked():
            self.trainer = 2
        self.select_button.setDisabled(True)

        result = self.func.getTrainerSessions(self.trainer)

        arrayOfTrainerSessions = [[0 for col in range(7)] for row in range (8)]

        innerIndex = 0
        OuterIndex = 0

        if result is not None:

            for row in result:

                if innerIndex % 7 == 0 and innerIndex != 0:
                    OuterIndex +=1
                    innerIndex = 0

                arrayOfTrainerSessions[OuterIndex][innerIndex] = row[2]
                innerIndex += 1

            self.training_table = QTableWidget()
            self.training_table.setMinimumSize(QSize(950, 305))
            self.training_table.setColumnCount(8)
            self.training_table.setHorizontalHeaderLabels(["Times", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])

            time_slots = ["9:00 - 10:00", "10:00 - 11:00", "11:00 - 12:00", "12:00 - 13:00", "13:00 - 14:00", "14:00 - 15:00", "15:00 - 16:00", "16:00 - 17:00"]
            self.training_table.setRowCount(len(time_slots))
            for row, time_slot in enumerate(time_slots):
                self.training_table.setItem(row, 0, QTableWidgetItem(time_slot))
                
            print(self.training_table.rowCount())
            print(self.training_table.columnCount())

            #fill out the busy and unavailable time slots
            for row in range(0, self.training_table.rowCount()):
                for column in range(0, self.training_table.columnCount()-1):

                    if(arrayOfTrainerSessions[row][column] != "BOOKED" and arrayOfTrainerSessions[row][column] != 'NOT AVAILABLE'):
                        index = QRadioButton("Book")
                        #self.training_table.setItem(row, column, QTableWidgetItem(selecte))
                        self.training_table.setIndexWidget(self.training_table.model().index(row, column+1), index)
                    else:
                        self.training_table.setItem(row, column+1, QTableWidgetItem(arrayOfTrainerSessions[row][column]))
                       # self.training_table.setIndexWidget(self.training_table.model().index(row, column+1), )

        self.layout.addWidget(self.training_table)
        self.layout.addWidget(self.update_button)

        return

        #show trainer selection and auto select the current training booked if any, based on trainer selection query all possible slots
        #display all slots as selectable options 
        #have update buttons, 
        #remove if there is an existitng one, then add
    

    def update_trainer_sessions():

        #delete old, add new
        return
    