#should have viewing/managing (for trainers)
from PyQt5.QtWidgets import QMessageBox, QDialog, QVBoxLayout, QLabel,QLineEdit, QHBoxLayout, QPushButton, QFormLayout
from functionImplemenation import functions
import memberId

class viewMembersPopup(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("View Members (trainers)")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("View Members"))
        self.setLayout(layout)

class manageProfilePopup(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Manage Profile (user)")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Manage Profile"))
        self.setLayout(layout)

        self.memberId = memberId.memberId

        self.buttons = []
        self.line_edits = []

        labels = ["Change First Name:", "Change Last Name:", "Change Email:", "Change Phone Number:", "Update Height(cm):", "Update Weight(kg):", "Alter Fitness Goal:"]
        for label_text in labels:
            row_layout = QHBoxLayout()
            label = QLabel(label_text)
            line_edit = QLineEdit()
            button = QPushButton("Update")
            button.clicked.connect(self.update_clicked)
            row_layout.addWidget(label)
            row_layout.addWidget(line_edit)
            row_layout.addWidget(button)
            layout.addLayout(row_layout)
            self.buttons.append(button)
            self.line_edits.append(line_edit)
        
        self.setLayout(layout)

    def update_clicked(self):
        button = self.sender()
        index = self.buttons.index(button)
        new_value = self.line_edits[index].text()
        func = functions()

        if index == 0:  # firstname
            result = func.updateFirstName(memberId.memberId, newName=new_value)
        elif index == 1:  # lastname
            result = func.updateLastName(memberId.memberId, newName=new_value)
        elif index == 2:  # email
            result = func.updateEmail(memberId.memberId, newEmail=new_value)
        elif index == 3:  # phonenumber
            result = func.updatePhone(memberId.memberId, newPhone=new_value)
        elif index == 4:  # height
            result = func.updateHeight(memberId.memberId, newHeight=new_value)
        elif index == 5:  # weight
            result = func.updateWeight(memberId.memberId, newWeight=new_value)
        elif index == 6:  # fitnessgoal
            result = func.addFitnessGoal(memberId.memberId, goal=new_value)

        if result == -1:
            QMessageBox.information(self, "Could not change", "Failed to change!")     
        else:
            QMessageBox.information(self, "Successful change", "Successful change!") 
        