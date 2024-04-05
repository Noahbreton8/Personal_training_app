import sys
from PyQt5.QtWidgets import QGroupBox, QHBoxLayout, QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QDialog, QRadioButton, QMessageBox
import psycopg2
import userSelectionPopup , loginRegisterPopup, scheduleClassesPopup, viewMembersPopup
from monitorEquipmentPopup import monitorEquipmentPopup, manageRoomsPopup
from scheduleClassesPopup import scheduleClassesPopup, registerClassesPopup , updateClassesPopup
from trainingSessionsPopup import bookTrainingPopup, setAvail
from viewMembersPopup import viewMembersPopup, manageProfilePopup
from billingAndPaymentPopup import manageBilingPopup

#posgresql credentials
DATABASE_NAME = ""
DATABASE_USER = ""
DATABASE_PASSWORD = ""
DATABASE_HOST = ""
DATABASE_PORT = ""

def execute_query(query, params= None):
    #connect to the database with the credentials above
    conn = psycopg2.connect(
        dbname=DATABASE_NAME,
        user=DATABASE_USER,
        password=DATABASE_PASSWORD,
        host=DATABASE_HOST,
        port=DATABASE_PORT)
    
    try:
        cur = conn.cursor()
        if params:
            cur.execute(query, params)
        else:
            cur.execute(query)

        #return the rows for printing get all students
        if query.strip().lower().startswith("select"):
            student_rows = cur.fetchall()
            cur.close()
            conn.close()
            return student_rows
        else:
            conn.commit()
            cur.close()
            conn.close()
    except psycopg2.Error as e:
        QMessageBox.critical(None, "Query Execution Error", f"Error executing query: {e}")
        return -1

def show_main_window(user_type, first_name, last_name):
    window = QWidget()
    window.setWindowTitle("Gym DB GUI")
    window.setFixedSize(300, 200)

    gui_layout = QVBoxLayout()
    welcome_label = QLabel(f"Hello {user_type}, {first_name} {last_name}.")
    gui_layout.addWidget(welcome_label)

    if user_type == "member":

        #add dashboard
        dashboard = QGroupBox("Dashboard")
        
        #add layout to dashboard

        gui_layout.addWidget(dashboard)

        member_group = QGroupBox("Features")
        profile_management_button = QPushButton("Profile Management")
        class_schedule_button = QPushButton("Register for Classes")
        book_training_button = QPushButton("Book Training")

        member_functions_layout = QVBoxLayout()

        profile_management_button.clicked.connect(profile_management)
        member_functions_layout.addWidget(profile_management_button)

        book_training_button.clicked.connect(book_training)
        member_functions_layout.addWidget(book_training_button)

        class_schedule_button.clicked.connect(book_classes)
        member_functions_layout.addWidget(class_schedule_button)

        member_group.setLayout(member_functions_layout)
        gui_layout.addWidget(member_group)

        #trainer buttons
    elif user_type == "trainer":
        trainer_group = QGroupBox("Features")
        class_schedule_button = QPushButton("Schedule Management")
        view_profiles_button = QPushButton("Member Profile Viewing")

        trainer_layout = QVBoxLayout()

        class_schedule_button.clicked.connect(set_avail)
        trainer_layout.addWidget(class_schedule_button)

        view_profiles_button.clicked.connect(member_profile_viewing)
        trainer_layout.addWidget(view_profiles_button)

        trainer_group.setLayout(trainer_layout)
        gui_layout.addWidget(trainer_group)

        # admin buttons
    elif user_type == "admin":
        admin_group = QGroupBox("Features")
        room_booking_button = QPushButton("Room Booking Management")
        equipment_maintenance_button = QPushButton("Equipment Maintenance Monitoring")
        update_sched_button = QPushButton("Class Schedule Updating")
        payment_processing_button = QPushButton("Billing and Payment Processing")

        admin_layout = QVBoxLayout()
       
        room_booking_button.clicked.connect(room_booking_management)
        admin_layout.addWidget(room_booking_button)

        equipment_maintenance_button.clicked.connect(equipment_maintenance_monitoring)
        admin_layout.addWidget(equipment_maintenance_button)

        update_sched_button.clicked.connect(class_schedule_updating)
        admin_layout.addWidget(update_sched_button)

        payment_processing_button.clicked.connect(billing_and_payment_processing)
        admin_layout.addWidget(payment_processing_button)

        admin_group.setLayout(admin_layout)
        gui_layout.addWidget(admin_group)

    window.setLayout(gui_layout)
    window.show()

    sys.exit(app.exec_())

#member funciton
def profile_management():
    print("Profile Management")
    dialog = manageProfilePopup()
    dialog.exec_()

def book_classes():
    print("Register for Classes")
    dialog = registerClassesPopup()
    dialog.exec_()

def book_training():
    dialog = bookTrainingPopup()
    dialog.exec_()
    
# trainer functiom
def member_profile_viewing():
    dialog = viewMembersPopup()
    dialog.exec_()

def set_avail():
    print("Set availability")
    dialog = setAvail()
    dialog.exec_()

def schedule_classes():
    print("Schedule Classes")
    dialog = scheduleClassesPopup()
    dialog.exec_()

# admin functions
def room_booking_management():
    print("Room Booking Management")
    dialog = manageRoomsPopup()
    dialog.exec_()

def equipment_maintenance_monitoring():
    print("Equipment Maintenance Monitoring")
    dialog = monitorEquipmentPopup()
    dialog.exec_()

def class_schedule_updating():
    print("Class Schedule Updating")
    dialog = updateClassesPopup()
    dialog.exec_()

def billing_and_payment_processing():
    print("Billing and Payment Processing")
    dialog = manageBilingPopup()
    dialog.exec_()

app = QApplication(sys.argv)

# get user type from the first popup dialog
user_type_dialog = userSelectionPopup.UserTypeSelectionPopup()
if user_type_dialog.exec_() == QDialog.Accepted:
    user_type = user_type_dialog.user_type

    # set names from the dialog and pass it to main window
    login_register_dialog = loginRegisterPopup.LoginRegisterPopup(user_type)

    # Connect the register_button to the register method of login_register_dialog
    register_button = login_register_dialog.findChild(QPushButton, "Register")
    if register_button is not None:
        register_button.clicked.connect(login_register_dialog.register)
    
    if login_register_dialog.exec_() == QDialog.Accepted:
        first_name = login_register_dialog.first_name.text()
        last_name = login_register_dialog.last_name.text()

        show_main_window(user_type, first_name, last_name)