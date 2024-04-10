from functionImplemenation import functions
from PyQt5.QtWidgets import QMessageBox, QPushButton, QDialog, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QTimeEdit
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


#member #1
class bookTrainingPopup(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Training Sessions (trainers)')
        layout = QVBoxLayout()
        layout.addWidget(QLabel('set avaalbity for Training Sessions'))
        self.setLayout(layout)