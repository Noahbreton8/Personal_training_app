import sys
from PyQt5.QtWidgets import QGroupBox, QHBoxLayout, QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QDialog, QRadioButton, QMessageBox
import psycopg2
import userSelectionPopup , loginRegisterPopup

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
    welcome_label = QLabel(f"Hello {first_name} {last_name}.")
    gui_layout.addWidget(welcome_label)

    #add dashboard
    dashboard = QGroupBox("Dashboard")
    
    #add layout to dashboard

    gui_layout.addWidget(dashboard)

    if user_type == "member":
        member_group = QGroupBox("Features")
        profile_management_button = QPushButton("Profile Management")
        class_schedule_button = QPushButton("Schedule/Class Management")

        member_functions_layout = QVBoxLayout()

        profile_management_button.clicked.connect(profile_management)
        member_functions_layout.addWidget(profile_management_button)

        class_schedule_button.clicked.connect(schedule_management_member)
        member_functions_layout.addWidget(class_schedule_button)

        member_group.setLayout(member_functions_layout)
        gui_layout.addWidget(member_group)

        #trainer buttons
    elif user_type == "trainer":
        trainer_group = QGroupBox("Features")
        class_schedule_button = QPushButton("Schedule Management")
        view_profiles_button = QPushButton("Member Profile Viewing")

        trainer_layout = QVBoxLayout()

        class_schedule_button.clicked.connect(schedule_management)
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

def schedule_management_member():
    print("Personal training Management/ Classes")

# trainer functiom
def member_profile_viewing():
    print("Member Profile Viewing")

def schedule_management():
    print("Schedule Management")

# admin functions
def room_booking_management():
    print("Room Booking Management")

def equipment_maintenance_monitoring():
    print("Equipment Maintenance Monitoring")

def class_schedule_updating():
    print("Class Schedule Updating")

def billing_and_payment_processing():
    print("Billing and Payment Processing")

app = QApplication(sys.argv)

# get user type from the first popup dialog
user_type_dialog = userSelectionPopup.UserTypeSelectionPopup()
if user_type_dialog.exec_() == QDialog.Accepted:
    user_type = user_type_dialog.user_type

    # set names from the dialog and pass it to main window
    login_register_dialog = loginRegisterPopup.LoginRegisterPopup(user_type)
    if login_register_dialog.exec_() == QDialog.Accepted:

        first_name = login_register_dialog.first_name.text()
        last_name = login_register_dialog.last_name.text()

        show_main_window(user_type, first_name, last_name)
