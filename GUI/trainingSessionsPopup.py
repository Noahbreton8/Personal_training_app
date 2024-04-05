#should have both schedlign (for trainers)
#and booking (for users)
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel

class setAvail(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Training Sessions (trainers)")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("set avaalbity for Training Sessions"))
        self.setLayout(layout)

class bookTrainingPopup(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Book Sessions (users)")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("book Training Sessions"))
        self.setLayout(layout)