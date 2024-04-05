#should have viewing/managing (for trainers)
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel

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