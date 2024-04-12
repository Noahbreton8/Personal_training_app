from PyQt5.QtWidgets import QGroupBox, QHBoxLayout, QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QDialog, QRadioButton, QMessageBox
import psycopg2
from functionImplementation import functions
import memberId

#login or register as member/admin/trainer
class LoginRegisterPopup(QDialog):
    def __init__(self, user_type):
        super().__init__()
        self.setWindowTitle("Login or Register")
        self.user_type = user_type
        layout = QVBoxLayout()

        self.first_name = QLineEdit()
        self.last_name = QLineEdit()
        self.email = QLineEdit()

        layout.addWidget(QLabel("First Name:"))
        layout.addWidget(self.first_name)
        layout.addWidget(QLabel("Last Name:"))
        layout.addWidget(self.last_name)

        if self.user_type == "member":
            layout.addWidget(QLabel("Email:"))
            layout.addWidget(self.email)

        if self.user_type == "member":
            login_button = QPushButton("Login")
            register_button = QPushButton("Register")

            login_button.clicked.connect(lambda: self.addOrLoginMember(registration_dialog= None, login_dialog =self,login= True))
            layout.addWidget(login_button)

            register_button.clicked.connect(self.register)
            layout.addWidget(register_button)
        else:
            login_button = QPushButton("Login")
            login_button.clicked.connect(lambda: self.addOrLoginMember(registration_dialog= None, login_dialog =self,login= True))  # Pass registration_dialog instance)
            layout.addWidget(login_button)

        self.setLayout(layout)

    # def login(self):
    #     first_name = self.first_name.text()
    #     last_name = self.last_name.text()
    #     email = self.email.text()
    #     # check user is in db
    #     self.accept()

    def register(self):
        registration_dialog = QDialog()
        layout = QVBoxLayout()

        self.tallness = QLineEdit()
        self.weight = QLineEdit()

        layout.addWidget(QLabel("Height(cm):"))
        layout.addWidget(self.tallness)
        layout.addWidget(QLabel("Weight(kg):"))
        layout.addWidget(self.weight)

        register_button = QPushButton("Register Now!")
        register_button.clicked.connect(lambda: self.addOrLoginMember(registration_dialog,self, False))  # Pass registration_dialog instance
        layout.addWidget(register_button)

        registration_dialog.setLayout(layout)
        registration_dialog.setWindowTitle("Registration Form")

        registration_dialog.exec_()
        # self.accept()

    def addOrLoginMember(self, registration_dialog, login_dialog, login):
        # Add a user to the table
        func = functions()
        if self.user_type == 'member':
            retur = func.memberRegistration(firstName=self.first_name.text(), lastName= self.last_name.text(), email=self.email.text(), height=getattr(self, 'tallness', '0'), weight=getattr(self, 'weight', '0'), phoneNumber="123")
        if self.user_type == 'trainer':
            retur = func.trainerLogin(firstName=self.first_name.text(), lastName= self.last_name.text(), phoneNumber="123")
        if self.user_type == 'admin':
             retur = func.adminLogin(firstName=self.first_name.text(), lastName= self.last_name.text())

        if retur == 0: #try to register but already exist
            if login:
                QMessageBox.information(self, "Successful Login", "Welcome!.")
            else:
                 QMessageBox.information(self, "Member Already Registered", "The member is already registered.")
            login_dialog.accept()
        elif retur == -1:
            QMessageBox.information(self, "", "Bad Input or db connection!.")
        elif retur == -2:
            QMessageBox.information(self, "Please Register", "No account with us yet, please click Register.")
        
        else:
            if login == False:
                QMessageBox.information(self, "New Register", "Successly added!.")
                registration_dialog.accept()
            memberId.memberId = retur
            print(memberId)
            login_dialog.accept()
