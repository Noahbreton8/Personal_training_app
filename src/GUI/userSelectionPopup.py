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

        self.select_button = QPushButton("Select")
        self.select_button.clicked.connect(self.select_user_type)
        layout.addWidget(self.select_button)

        self.setLayout(layout)

        self.update_select_button_state()

        # turn select on if selected type
        self.admin_button.toggled.connect(self.update_select_button_state)
        self.trainer_button.toggled.connect(self.update_select_button_state)
        self.member_button.toggled.connect(self.update_select_button_state)

    def update_select_button_state(self):
        # Enable the button only if one of the radio buttons is selected
        self.select_button.setDisabled(not (self.admin_button.isChecked() or
                                            self.trainer_button.isChecked() or
                                            self.member_button.isChecked()))


    def select_user_type(self):
        if self.admin_button.isChecked():
            self.user_type = "admin"
        elif self.trainer_button.isChecked():
            self.user_type = "trainer"
        elif self.member_button.isChecked():
            self.user_type = "member"

        self.accept()
