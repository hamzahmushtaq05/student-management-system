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

def admin_menu():
    print("\n-----Admin menu----- \n1.Add Students \n2.Display Students \n3.Delete Student \n") 
 
def search_student(student_name, students):
    for student in students:
        if student["name"] == student_name:
            return student
    return None

   
def find_avg(student):
    return sum(student["grades"]) / len(student["grades"])

def check_password(password):
    correct_pass = "Admin123456"
    if password == correct_pass:
            return True
    return False    

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
        

while True:
    main_menu()
    main_menu_op = input("input: ")

    if main_menu_op == "1":
        print("Student login selected.")
        student_name = input("Enter your name: ")
        display_student_info(student_name, students)
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
            admin_menu()
            admin_menu_op = input("input: ")
        elif check == False:
            print("Incorrect password. Access denied.")
    elif main_menu_op == "0":
        print("Exiting the application.")
        break
    else:
        print("Invalid option. Please try again.")