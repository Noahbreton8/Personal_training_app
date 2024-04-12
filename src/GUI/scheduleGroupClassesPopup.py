#should have both updating (for admin)
#and register (for users)
from functionImplementation import functions
import memberId

from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QMessageBox, QRadioButton, QPushButton
from PyQt5.QtCore import QSize

class registerGroupClassesPopup(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Register for Classes(for users)")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Register for Classes"))
        self.setLayout(layout)

        func = functions()
        result = func.getActiveClasses()

        if result != -1:
            self.classes_table = QTableWidget()
            self.classes_table.setMinimumSize(QSize(400, 200))
            self.classes_table.setColumnCount(3)
            self.classes_table.setHorizontalHeaderLabels(["Class Name", "Class Time", "Registration"])

            self.classes_table.setRowCount(len(result))

            for i in range(len(result)):
                self.classes_table.setItem(i, 0, QTableWidgetItem(result[i][1]))

                self.classes_table.setItem(i, 1, QTableWidgetItem(result[i][2].strftime('%Y-%m-%d %H:%M:%S')))

                if (func.isMemberInClass(memberId.memberId, result[i][0])):
                    self.classes_table.setItem(i, 2, QTableWidgetItem("ALREADY REGISTERED"))
                else:
                    index = QRadioButton("Register")
                    self.classes_table.setIndexWidget(self.classes_table.model().index(i, 2), index)

            layout.addWidget(self.classes_table)
            self.update_button = QPushButton("Update!")
            self.update_button.clicked.connect(self.update_class_registration)
            layout.addWidget(self.update_button)

        else:
            layout.addWidget(QLabel("No classes open for registration"))

        return
    
    def update_class_registration(self):
        func = functions()

        for i in range(self.classes_table.rowCount()):
            button = self.classes_table.cellWidget(i, 2)
            if isinstance(button, QRadioButton) and button.isChecked():
                class_name = self.classes_table.item(i, 0).text()
                func.updateClassesRegistration(memberId.memberId, class_name)

                QMessageBox.information(self, "Successful Class Registration!", "Successful Class Registration!")
                return

class updateGroupClassesPopup(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Update for Classes(for admin)")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Update Classes"))

        func = functions()
        result = func.getClasses()

        if result != -1:
            self.class_table = QTableWidget()
            self.class_table.setColumnCount(2)
            self.class_table.setHorizontalHeaderLabels(["Class Name", "Class Time"])

            for row, self.class_info in enumerate(result):
                class_name = self.class_info[0]  
                time_booked = self.class_info[1]  
                self.class_table.insertRow(row)
                self.class_table.setItem(row, 0, QTableWidgetItem(str(class_name)))
                self.class_table.setItem(row, 1, QTableWidgetItem(str(time_booked)))

            # Set column widths
            column_width = 145
            self.class_table.setColumnWidth(0, column_width)
            self.class_table.setColumnWidth(1, column_width)

            # Set minimum size
            self.class_table.setMinimumSize(QSize(325, 225))
            layout.addWidget(self.class_table)

            self.class_table.itemChanged.connect(self.updateClassesTable)

        self.setLayout(layout)
    

    def updateClassesTable(self, item):
        row = item.row()
        column = item.column()
        if column == 0:
            QMessageBox.information(self, "Class", "Cannot update class name")
            return
        value = item.text()

        class_name = self.class_table.item(row, 0).text()
        column_name = self.class_table.horizontalHeaderItem(column).text()

        print(row)
       
        func = functions()
        result = func.updateClassValue(class_name, column_name, value)
        if result == -1:
            QMessageBox.information(self, "Error", "Input a class time in this format: YYYY-mm-DD HH:MM") 
        elif result != None:
            QMessageBox.information(self, "Class", "Class Updated!")  
        else: 
            QMessageBox.warning(self, "Error", "Failed to update class.")