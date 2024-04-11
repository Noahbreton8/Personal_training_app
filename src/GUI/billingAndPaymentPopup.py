#billing for admin
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel
from functionImplementation import functions

class manageBilingPopup(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Manage billing (admin)")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Manage billing"))
        self.setLayout(layout)

class makePaymentsPopup(QDialog):
    def __init__(self):
        super().__init__()
        
        func = functions

        layout = QVBoxLayout()
        self.setWindowTitle("Make Payment")

        result = func.checkMemberPaid()

        #test by remaking db, trying to pay as a member


        #display nothing to pay
       # if :
        #    layout.addWidget(QLabel("Nothing to pay!"))
        # else: #display amount with pay button
        #     layout.addWidget(QLabel("Ammount due: 25.99$ - One standard membership fee"))
        #     pay_fees_button = QPushButton("Pay")
        #     layout.addWidget(pay_fees_button)
        #     pay_fees_button.clicked.connect(func.makePayment())
        self.setLayout(layout)