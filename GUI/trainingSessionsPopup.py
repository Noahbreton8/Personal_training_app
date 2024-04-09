from PyQt5.QtWidgets import QMessageBox, QDialog, QTableWidget, QTableWidgetItem, QVBoxLayout, QLabel
from functionImplemenation import functions
from PyQt5.QtCore import QSize, Qt

#trainer #1
class setAvail(QDialog):
    def __init__(self, first_name, last_name):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        
        self.setWindowTitle("Training Sessions (Trainers)")
        
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Set Availability for Training Sessions"))
        
        table = QTableWidget()
        table.setColumnCount(3) 
        table.setHorizontalHeaderLabels(["Day", "Start Time", "End Time"])
        
        func = functions()
        results = func.getAvailability(self.first_name, self.last_name)
        
        table.setRowCount(len(results))
        
        for row, data in enumerate(results):
            for column, item in enumerate(data[2:]): 
                table.setItem(row, column, QTableWidgetItem(str(item)))
        
        #190 fits nicely with width 200, no scrollwheel
        table.setColumnWidth(0, 194)
        table.setColumnWidth(1, 194)
        table.setColumnWidth(2, 194)

        #set width
        table.setMinimumSize(QSize(600, 300))    

        table.itemChanged.connect(self.updateAvail)
 

        layout.addWidget(table)
        self.setLayout(layout)

    def updateAvail():
        return
        #do this

#member #1
class bookTrainingPopup(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Training Sessions (trainers)")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("set avaalbity for Training Sessions"))
        self.setLayout(layout)