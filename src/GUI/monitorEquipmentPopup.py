#for admins monitoring equiptment
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget, QGroupBox, QHBoxLayout, QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QDialog, QRadioButton, QMessageBox
from PyQt5.QtCore import QSize, Qt
from GUI.functionImplementation import functions

class monitorEquipmentPopup(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Monitor Equipment(for admin)")
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Monitor Equipment"))

        func = functions()
        result = func.getEquipment(1)

        if result is not None:
            equip_table = QTableWidget()
            equip_table.setColumnCount(2)
            equip_table.setHorizontalHeaderLabels(["Equipment Name", "Maintenance Status"])

            for row, equipment in enumerate(result):
                if equipment:
                    equip_name, maintenance_status = equipment[0]
                    equip_table.insertRow(row)
                    equip_table.setItem(row, 0, QTableWidgetItem(equip_name))
                    equip_table.setItem(row, 1, QTableWidgetItem(maintenance_status))

            #190 fits nicely with width 200, no scrollwheel
            equip_table.setColumnWidth(0, 190)
            equip_table.setColumnWidth(1, 190)

            #set width
            equip_table.setMinimumSize(QSize(400, 300))
            layout.addWidget(equip_table)

        self.setLayout(layout)

class manageRoomsPopup(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Manage rooms(for admin)")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Manage rooms"))

        func = functions()
        result = func.getRooms()

        if result is not None:
            self.room_table = QTableWidget()
            self.room_table.setColumnCount(4)
            self.room_table.setHorizontalHeaderLabels(["Room Number", "Status", "Time Booked", "Reason"])

            for row, self.room_info in enumerate(result):
                #slice out roomnumber at 3 and the other values 1,2,4
                room_number = self.room_info[3] 
                status = self.room_info[1]  
                time_booked = self.room_info[4]  
                reason = self.room_info[2] 
                self.room_table.insertRow(row)
                self.room_table.setItem(row, 0, QTableWidgetItem(str(room_number)))
                self.room_table.setItem(row, 1, QTableWidgetItem(str(status)))
                self.room_table.setItem(row, 2, QTableWidgetItem(str(time_booked)))
                self.room_table.setItem(row, 3, QTableWidgetItem(str(reason)))

                self.room_table.item(row, 0).setFlags(self.room_table.item(row, 0).flags() & ~Qt.ItemIsEditable)

            # Set column widths
            column_width = 145
            self.room_table.setColumnWidth(0, column_width)
            self.room_table.setColumnWidth(1, column_width)
            self.room_table.setColumnWidth(2, column_width)
            self.room_table.setColumnWidth(3, column_width)

            # Set minimum size
            self.room_table.setMinimumSize(QSize(600, 300))
            layout.addWidget(self.room_table)

            self.room_table.itemChanged.connect(self.updateDatabase)

        self.setLayout(layout)

    def updateDatabase(self, item):
        row = item.row()
        column = item.column()
        value = item.text()

        room_number = int(self.room_table.item(row, 0).text())
        column_name = self.room_table.horizontalHeaderItem(column).text()

        print(row)
       
        func = functions()
        result =func.updateRoomValue(room_number, column_name, value)
        
        if result != None:
            QMessageBox.information(self, "Room", "Room Updated!")  
        else: 
            QMessageBox.warning(self, "Error", "Failed to update room.")