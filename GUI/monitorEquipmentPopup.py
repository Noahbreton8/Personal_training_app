#for admins monitoring equiptment
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget, QGroupBox, QHBoxLayout, QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QDialog, QRadioButton, QMessageBox
from PyQt5.QtCore import QSize
from functionImplemenation import functions

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
        self.setLayout(layout)