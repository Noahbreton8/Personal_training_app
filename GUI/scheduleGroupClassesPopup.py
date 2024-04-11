#should have both updating (for admin)
#and register (for users)
from functionImplemenation import functions

from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import QSize, Qt

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
        
        if result != None:
            QMessageBox.information(self, "Class", "Class Updated!")  
        else: 
            QMessageBox.warning(self, "Error", "Failed to update class.")