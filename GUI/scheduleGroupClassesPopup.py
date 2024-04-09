#should have both updating (for admin)
#and register (for users)
#and organizing (for trainers)

from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel

class scheduleGroupClassesPopup(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Schedule Classes(for trainers)")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Schedule Classes"))
        self.setLayout(layout)

class registerGroupClassesPopup(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Register for Classes(for users)")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Register for Classes"))
        self.setLayout(layout)

class updateGroupClassesPopup(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Update for Classes(for admin)")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Update Classes"))
        self.setLayout(layout)
