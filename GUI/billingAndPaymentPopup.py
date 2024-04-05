#billing for admin
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel

class manageBilingPopup(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Manage billing (admin)")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Manage billing"))
        self.setLayout(layout)