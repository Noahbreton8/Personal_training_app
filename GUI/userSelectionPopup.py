from PyQt5.QtWidgets import QGroupBox, QHBoxLayout, QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QDialog, QRadioButton, QMessageBox

#select the user type
class UserTypeSelectionPopup(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("User Type Selection")
        layout = QVBoxLayout()
        self.setFixedSize(300, 200)

        self.user_type = None

        self.admin_button = QRadioButton("Admin")
        self.trainer_button = QRadioButton("Trainer")
        self.member_button = QRadioButton("Member")

        layout.addWidget(self.admin_button)
        layout.addWidget(self.trainer_button)
        layout.addWidget(self.member_button)

        select_button = QPushButton("Select")
        select_button.clicked.connect(self.select_user_type)
        layout.addWidget(select_button)

        self.setLayout(layout)

    def select_user_type(self):
        if self.admin_button.isChecked():
            self.user_type = "admin"
        elif self.trainer_button.isChecked():
            self.user_type = "trainer"
        elif self.member_button.isChecked():
            self.user_type = "member"

        self.accept()
