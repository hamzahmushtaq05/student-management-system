students = [
    {
        "id": 1,
        "name": "Ali",
        "age": 20,
        "grades": [85, 90, 78]
    },
    {
        "id": 2,
        "name": "Sara",
        "age": 21,
        "grades": [95, 88, 92]
    }
]

def main_menu():
    print("\n-----Student Management App-----\n1.Log in as Student\n2.Log in as Admin\n0.Exit\n")

def student_menu():
    print("-----Student Menu----- \n1.View My Information \n0.Back to Main Menu \n")
    
    
def admin_menu():
    print("\n-----Admin menu----- \n1.Student Management \n2.Student Reports \n0.Back to Main Menu \n") 


def student_management_menu():
    print("\n-----Student Management Menu----- \n1.Add Student \n2.Search Student \n3.Edit Student info \n4.Delete Student \n0.Back to Admin Menu \n")


def student_report_menu():
    print("\n-----View Student menu----- \n1.Display all Students \n2.Display Passed Students \n3.Display Failed Student \n4.Display Honour Students \n5.Display valedictorian \n0.Back to Admin Menu")


def edit_student_menu():
    print("\n-----Edit Student Info menu----- \n1.Edit Name \n2.Edit Age \n3.Edit Grades \n0.Back to Admin Menu")
    
    
def search_student(student_name, students):
    for student in students:
        if student["name"] == student_name:
            return student
    return None

   
def find_avg(student):
    return sum(student["grades"]) / len(student["grades"])


def check_password(password):
    correct_pass = "Admin"
    if password == correct_pass:
            return True
    return False 

def display_all_students(students):
    if not students:
        print("No students found.")
        return
    for student in students:
        avg = find_avg(student)
        if avg >= 50:
            status = "Passed"
        else:
            status = "Failed"
        print(f"Student ID: {student['id']} \nName: {student['name']} \nAge: {student['age']} \nGrades: {student['grades']} \nAverage: {avg} \nStatus: {status}\n")


def display_student_info(student_name, students):
    display = search_student(student_name, students)
    if display is None:
        print("Student not found.")
        return
    else:
        avg = find_avg(display)
        if avg >= 50:
            status = "Passed"
        else:
            status = "failed"
        print(f"Student ID: {display['id']} \nName: {display['name']} \nAge: {display['age']} \nGrades: {display['grades']} \nAverage: {avg} \nStatus: {status}")

def Delete_student(student_name, students):
    student_to_delete = search_student(student_name, students)
    if student_to_delete is None:
        print("Student not found.")
        return
    else:
        students.remove(student_to_delete)
        print(f"Student {student_name} deleted successfully.")


def add_student(students):
    student_id = len(students) + 1
    student_name = input("Enter student name: ")
    check_age_valid = False
    while not check_age_valid:
        try:
            student_age = int(input("Enter student age: "))
            if student_age < 0:
                print("Age cannot be negative. Please enter a valid age.")
                continue
            check_age_valid = True
        except ValueError:
            print("Invalid input. Please enter a valid integer for age.")
    check_grades_valid = False
    while not check_grades_valid:
        try:
            student_grades = list(input("Enter student grades (comma-separated): ").split(','))
            student_grades = student_grades[:3]
            student_grades = list(map(int, student_grades))         
            while len(student_grades) < 3:
                missing_grades = 3 - len(student_grades)
                print(f"You have entered {len(student_grades)} grades. Please enter {missing_grades} more grade(s).") 
                try:
                    new_grades = list(input("Enter additional grades (comma-separated): ").split(','))
                    new_grades = new_grades[:missing_grades]
                    new_grades = list(map(int, new_grades))
                    student_grades.extend(new_grades)
                except ValueError:
                            print("Invalid input. Please enter valid integers for grades.")
            for index in range(len(student_grades)):
                while student_grades[index] < 0 or student_grades[index] > 100:
                    print("Grades must be between 0 and 100. Please enter valid grades.")
                    try:
                        student_grades[index] = int(input("Please enter a valid grade: "))
                    except ValueError:
                                print("Invalid input. Please enter valid integers for grades.")
            check_grades_valid = True
        except ValueError:
            print("Invalid input. Please enter valid integers for grades.")
    new_student = {
        "id": student_id,
        "name": student_name,
        "age": student_age,
        "grades": student_grades
    }
    students.append(new_student)
    print(f"Student {student_name} added successfully.")  
    
 
 
         
while True:
    main_menu()
    main_menu_op = input("input: ")
    if main_menu_op == "1":
        print("Student login selected.")
        while True:
            student_menu()
            student_menu_op = input("input: ")
            if student_menu_op == "1":
                student_name = input("Enter your name: ")
                display_student_info(student_name, students)
            elif student_menu_op == "0":
                break
            else:
                print("Invalid option. Please try again.")
    elif main_menu_op == "2":
        print("Admin login selected.")
        for i in range(3):
            password = input("Enter password: ")
            check = check_password(password)
            if check == True:
                break
            else:
                continue
        if check == True:
            while True:
                admin_menu()
                admin_menu_op = input("input: ")
                if admin_menu_op == "1":
                    while True:
                        student_management_menu()
                        student_management_menu_op = input("input: ")
                        if student_management_menu_op == "1":
                            add_student(students)
                        elif student_management_menu_op == "2":
                            student_name = input("Enter your name: ")
                            display_student_info(student_name, students)
                        elif student_management_menu_op == "3":
                            while True:
                                edit_student_menu()
                                edit_student_menu_op = input("input: ")
                                if edit_student_menu_op == "1":
                                    # Edit Name
                                    pass
                                elif edit_student_menu_op == "2":
                                    # Edit Age
                                    pass
                                elif edit_student_menu_op == "3":
                                    # Edit Grades
                                    pass
                                elif edit_student_menu_op == "0":
                                    break
                                else:
                                    print("Invalid option. Please try again.")
                        elif student_management_menu_op == "4":
                            student_name = input("Enter the name of the student to delete: ")
                            Delete_student(student_name, students)
                        elif student_management_menu_op == "0":
                            break
                        else:
                            print("Invalid option. Please try again.")
                elif admin_menu_op == "2":
                    while True:
                        student_report_menu()
                        student_report_menu_op = input("input: ")
                        if student_report_menu_op == "1":
                            display_all_students(students)
                        elif student_report_menu_op == "2":
                            # Display Passed Students
                            pass
                        elif student_report_menu_op == "3":
                            # Display Failed Student
                            pass
                        elif student_report_menu_op == "4":
                            # Display Honour Students
                            pass
                        elif student_report_menu_op == "5":
                            # Display valedictorian
                            pass
                        elif student_report_menu_op == "0":
                            break
                        else:
                            print("Invalid option. Please try again.")
                elif admin_menu_op == "0":
                    break
                else:
                    print("Invalid option. Please try again.")
        elif check == False:
            print("Incorrect password. Access denied.")
    elif main_menu_op == "0":
        print("Exiting the application.")
        break
    else:
        print("Invalid option. Please try again.")