#billing for admin
from PyQt5.QtWidgets import QMessageBox, QPushButton, QDialog, QVBoxLayout, QLabel
from functionImplementation import functions
import memberId

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
        func = functions()

        self.setWindowTitle("Make Payment")
        layout = QVBoxLayout()
        
        result = func.checkMemberPaid(memberId=memberId.memberId)

        #display nothing to pay
        if result == 0:
           layout.addWidget(QLabel("Nothing to pay!"))

        elif result == -1:
            amount = func.getPayment()[0][0]
            layout.addWidget(QLabel("Ammount due: " + str(amount) + "$ - One standard membership fee"))
            pay_fees_button = QPushButton("Pay")
            layout.addWidget(pay_fees_button)
            pay_fees_button.clicked.connect(lambda: makePayment(self))

        self.setLayout(layout)

def makePayment(self):
    func = functions()
    result = func.makePayment()

    if result == 0:
        QMessageBox.information(self, "Successful payment", "Successful payment!") 
    else:
        QMessageBox.information(self, "Payment failed", "Payment failed!") 

    self.accept()