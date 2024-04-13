#should have viewing/managing (for trainers)
from PyQt5.QtWidgets import QTextEdit, QMessageBox, QDialog, QVBoxLayout, QLabel,QLineEdit, QHBoxLayout, QPushButton, QFormLayout
from functionImplementation import functions
import memberId

class viewMembersPopup(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("View Members (trainers)")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("View Member:"))

        self.first_name_input = QLineEdit()
        layout.addWidget(QLabel("First Name:"))
        layout.addWidget(self.first_name_input)

        self.last_name_input = QLineEdit()
        layout.addWidget(QLabel("Last Name:"))
        layout.addWidget(self.last_name_input)

        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.search)
        layout.addWidget(self.search_button)

        self.achievement_button = QPushButton("Give Achievement:")
        self.achievement = QLineEdit()
        self.achievement_button.setDisabled(True)
        self.achievement_button.clicked.connect(self.giveAchievement)
        layout.addWidget(self.achievement_button)
        layout.addWidget(self.achievement)

        self.exercise_button = QPushButton("Give Exercise:")
        self.exercise = QLineEdit()
        self.exercise_button.setDisabled(True)
        self.exercise_button.clicked.connect(self.giveExercise)
        layout.addWidget(self.exercise_button)
        layout.addWidget(self.exercise)

        self.result_text_edit = QTextEdit()
        layout.addWidget(self.result_text_edit)

        self.setLayout(layout)

    def search(self):
        func = functions()
        self.result = func.getMember(self.first_name_input.text(), self.last_name_input.text())

        if self.result:
            formatted_result = ""
            descriptors = ["First Name", "Last Name", "Phone Number", "Email", "Weight", "Height", "Goal"]
            for i, item in enumerate(self.result[0]):
                formatted_result += descriptors[i] + ": " + str(item) + "\n"
                if descriptors[i] == "Email":
                    self.email = item
            self.result_text_edit.setPlainText(formatted_result)
            self.achievement_button.setEnabled(True)
            self.exercise_button.setEnabled(True)
        else:
            self.result_text_edit.setPlainText("Member not found.")
            self.achievement_button.setDisabled(True)
            self.exercise_button.setDisabled(True)
        #display this

    def giveAchievement(self):
        func = functions()
        result = func.addToAchievements(self.result[0][6], self.achievement.text())
        if result != -1:
            QMessageBox.information(self, "Achievement", "Added Achievement!")     
        #display this
            
    def giveExercise(self):
        func = functions()
        result = func.addToExercise(self.result[0][6], self.exercise.text())
        if result != -1:
            QMessageBox.information(self, "Exercise", "Added Exercise!")     
        #display this


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

        labels = ["Change First Name:", "Change Last Name:", "Change Email:", "Change Phone Number:", "Update Height(cm):", "Update Weight(kg):", "Add Fitness Goal:"]
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
        