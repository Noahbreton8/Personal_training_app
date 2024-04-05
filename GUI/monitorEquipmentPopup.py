#for admins monitoring equiptment
from PyQt5.QtWidgets import QGroupBox, QHBoxLayout, QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QDialog, QRadioButton, QMessageBox
import psycopg2

class monitorEquipmentPopup(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Monitor Equipment(for admin)")
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Monitor Equipment"))

        self.setLayout(layout)

class manageRoomsPopup(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Manage rooms(for admin)")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Manage rooms"))
        self.setLayout(layout)