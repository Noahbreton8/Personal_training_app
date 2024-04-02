from PyQt5.QtWidgets import QGroupBox, QHBoxLayout, QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QDialog, QRadioButton, QMessageBox
import psycopg2

#login or register as member/admin/trainer
class LoginRegisterPopup(QDialog):
    def __init__(self, user_type):
        super().__init__()
        self.setWindowTitle("Login or Register")
        self.user_type = user_type
        layout = QVBoxLayout()

        self.first_name = QLineEdit()
        self.last_name = QLineEdit()

        layout.addWidget(QLabel("First Name:"))
        layout.addWidget(self.first_name)
        layout.addWidget(QLabel("Last Name:"))
        layout.addWidget(self.last_name)

        if self.user_type == "member":
            login_button = QPushButton("Login")
            register_button = QPushButton("Register")

            login_button.clicked.connect(self.login)
            layout.addWidget(login_button)

            register_button.clicked.connect(self.register)
            layout.addWidget(register_button)
        else:
            login_button = QPushButton("Login")
            login_button.clicked.connect(self.login)
            layout.addWidget(login_button)

        self.setLayout(layout)

    def login(self):
        first_name = self.first_name.text()
        last_name = self.last_name.text()
        # check user is in db
        self.accept()

    def register(self):
        first_name = self.first_name.text()
        last_name = self.last_name.text()
        # add new member to db
        self.accept()
