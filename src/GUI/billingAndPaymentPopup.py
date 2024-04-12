#billing for admin
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QCheckBox, QTableWidget, QTableWidgetItem,  QMessageBox, QPushButton, QDialog, QVBoxLayout, QLabel
from functionImplementation import functions
from PyQt5.QtCore import Qt, QSize
import memberId

class manageBilingPopup(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Manage billing (admin)")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Manage billing"))
        self.setLayout(layout)

        func = functions()

        result = func.getMembers()

        print (result)

        if result != -1:
            self.table = QTableWidget()
            self.table.setRowCount(len(result))
            self.table.setColumnCount(5)
            self.table.setHorizontalHeaderLabels(["First Name", "Last Name", "Email", "Payment Status", "Charge Member"])

            for row, (first_name, last_name, email, status) in enumerate(result):
                item_first_name = QTableWidgetItem(first_name)
                item_last_name = QTableWidgetItem(last_name)
                item_email = QTableWidgetItem(email)
                item_status = QTableWidgetItem(status)

                item_first_name.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                item_last_name.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                item_email.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                item_status.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

                self.table.setItem(row, 0, item_first_name)
                self.table.setItem(row, 1, item_last_name)
                self.table.setItem(row, 2, item_email)
                self.table.setItem(row, 3, item_status)

                checkbox = QCheckBox()
                checkbox.setEnabled(status != 'Unpaid')  
                self.table.setCellWidget(row, 4, checkbox)

            self.table.setMinimumSize(QSize(1000, 400))

            self.table.setColumnWidth(0, 190)
            self.table.setColumnWidth(1, 190)
            self.table.setColumnWidth(2, 190)
            self.table.setColumnWidth(3, 190)
            self.table.setColumnWidth(4, 150)

            layout.addWidget(self.table)

            saveButton = QPushButton("Save Changes")
            saveButton.clicked.connect(self.saveChanges)
            layout.addWidget(saveButton)

            self.setLayout(layout)

    def saveChanges(self):
        func = functions()
        updateAll = True
        
        allChecked = []
        for row in range(self.table.rowCount()):
            chkBox = self.table.cellWidget(row, 4)
            if chkBox.isChecked():
                row_data = tuple(self.table.item(row, col).text() for col in range(4))
                allChecked.append((row, row_data))

        if not allChecked:
            QMessageBox.information(self, "Update", "No members selected for updating.")
            return
        
        for row_index, row_data in allChecked:
            result2 = func.toggleMemberPaymentStatus(paymentStatus='Unpaid', firstname=row_data[0], lastname=row_data[1], email=row_data[2])
            if result2 == None:
                self.table.item(row_index, 3).setText('Unpaid')
            else:
                updateAll = False

        if updateAll:
            QMessageBox.information(self, "Update Success", "All members have been sent new charges.")
        else:
            QMessageBox.warning(self, "Update Failure", "Not all members updated")
      
        #make a QTable
        #have it display every user with 4 columns
        #first name, last name, email and paid status
        #make it so that admin can edit it to be paid or unpaid
        #and then update the member row in the database

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