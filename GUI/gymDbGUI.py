import sys
from PyQt5.QtWidgets import QGroupBox, QHBoxLayout, QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QDialog, QRadioButton, QMessageBox
import psycopg2
from userSelectionPopup import UserTypeSelectionPopup
from loginRegisterPopup import LoginRegisterPopup
from scheduleGroupClassesPopup import scheduleGroupClassesPopup
from monitorEquipmentPopup import monitorEquipmentPopup, manageRoomsPopup
from scheduleGroupClassesPopup import scheduleGroupClassesPopup, registerGroupClassesPopup , updateGroupClassesPopup
from trainingSessionsPopup import setAvail, bookTrainingPopup
from viewMembersPopup import viewMembersPopup, manageProfilePopup
from billingAndPaymentPopup import manageBilingPopup
from functionImplemenation import functions
import memberId

def show_main_window(user_type, first_name, last_name):
    window = QWidget()
    window.setWindowTitle("Gym DB GUI")
    window.setFixedWidth(600)

    func = functions()

    gui_layout = QVBoxLayout()
    welcome_label = QLabel(f"Hello {user_type}, {first_name} {last_name}.")

    gui_layout.addWidget(welcome_label)

    if user_type == "member":

        #add dashboard
        dashboard = QGroupBox("Dashboard")

        #add a Qlabel for every exercise
        dashboard_layout = QVBoxLayout()
        exercise_result = func.getExerciseRoutines(memberId=memberId.memberId)
        
        dashboard_layout.addWidget(QLabel("Exercises:"))
        if exercise_result:
            for exercise in exercise_result:
                formatted_exercise = exercise[0] + ": " + str(exercise[1]) + " reps, " + str(exercise[2]) + " sets"
                dashboard_layout.addWidget(QLabel(formatted_exercise))

        achiev_result = func.getAllAchievements(memberId=memberId.memberId)
        dashboard_layout.addWidget(QLabel("Recent Achievment:"+str(achiev_result)) )

        weight_result = func.getWeight(memberId=memberId.memberId)
        if weight_result:
            dashboard_layout.addWidget(QLabel("Current Weight: " + str(weight_result[0][0]) + " KG"))

        #add layout to dashboard
        dashboard.setLayout(dashboard_layout)

        gui_layout.addWidget(dashboard)

        member_group = QGroupBox("Features")
        profile_management_button = QPushButton("Profile Management")
        manage_schedule_button = QPushButton("Register for Classes")
        book_training_button = QPushButton("Book Training")

        member_functions_layout = QVBoxLayout()

        profile_management_button.clicked.connect(profile_management)
        member_functions_layout.addWidget(profile_management_button)

        book_training_button.clicked.connect(book_training)
        member_functions_layout.addWidget(book_training_button)

        manage_schedule_button.clicked.connect(book_classes)
        member_functions_layout.addWidget(manage_schedule_button)

        member_group.setLayout(member_functions_layout)
        gui_layout.addWidget(member_group)

        #trainer buttons
    elif user_type == "trainer":
        trainer_group = QGroupBox("Features")
        manage_schedule_button = QPushButton("Schedule Management")
        view_profiles_button = QPushButton("Member Profile Viewing")

        trainer_layout = QVBoxLayout()
        def show_set_avail_dialog():
            dialog = setAvail(first_name=first_name, last_name=last_name)
            dialog.exec_()

        manage_schedule_button.clicked.connect(show_set_avail_dialog)
        trainer_layout.addWidget(manage_schedule_button)

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
    dialog = registerGroupClassesPopup()
    dialog.exec_()

def book_training():
    dialog = bookTrainingPopup()
    dialog.exec_()
    
# trainer function
def member_profile_viewing():
    dialog = viewMembersPopup()
    dialog.exec_()

def set_avail():
    print("Set availability")
    dialog = setAvail()
    dialog.exec_()

def schedule_classes():
    print("Schedule Classes")
    dialog = scheduleGroupClassesPopup()
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
    dialog = updateGroupClassesPopup()
    dialog.exec_()

def billing_and_payment_processing():
    print("Billing and Payment Processing")
    dialog = manageBilingPopup()
    dialog.exec_()

def get_member_id(first_name, last_name, email):
    func = functions()
    query = "SELECT member_id FROM Members WHERE first_name = %s AND last_name = %s AND email = %s;"
    params = (first_name, last_name, email)
    result = func.execute_query(query, params)
    if result != -1 and result:
        print("current member id" + str(result[0][0]))
        return result[0][0] 
    else:
        return None

app = QApplication(sys.argv)

# get user type from the first popup dialog
user_type_dialog = UserTypeSelectionPopup()
if user_type_dialog.exec_() == QDialog.Accepted:
    user_type = user_type_dialog.user_type

    # set names from the dialog and pass it to main window
    login_register_dialog = LoginRegisterPopup(user_type)

    # Connect the register_button to the register method of login_register_dialog
    register_button = login_register_dialog.findChild(QPushButton, "Register")
    if register_button is not None:
        register_button.clicked.connect(login_register_dialog.register)
    
    if login_register_dialog.exec_() == QDialog.Accepted:
        first_name = login_register_dialog.first_name.text()
        last_name = login_register_dialog.last_name.text()
        email = login_register_dialog.email.text()

        memberId.memberId = get_member_id(first_name, last_name, email)

        show_main_window(user_type, first_name, last_name)