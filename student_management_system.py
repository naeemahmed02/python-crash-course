# Student Management System using Lists and Dictionaries

students = []   # List to store all student records

def add_student():
    print("\n--- Add Student ---")
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    student = {
        "roll": roll,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    print("Student added successfully!\n")


def view_students():
    print("\n--- Student List ---")

    if not students:
        print("No student records found!\n")
        return

    for student in students:
        print("Roll No:", student["roll"])
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Course:", student["course"])
        print("----------------------")
    print()


def search_student():
    print("\n--- Search Student ---")
    roll = input("Enter Roll Number to search: ")

    for student in students:
        if student["roll"] == roll:
            print("Student Found!")
            print(student)
            return

    print("Student not found!\n")


def update_student():
    print("\n--- Update Student ---")
    roll = input("Enter Roll Number to update: ")

    for student in students:
        if student["roll"] == roll:
            student["name"] = input("Enter New Name: ")
            student["age"] = input("Enter New Age: ")
            student["course"] = input("Enter New Course: ")

            print("Student updated successfully!\n")
            return

    print("Student not found!\n")


def delete_student():
    print("\n--- Delete Student ---")
    roll = input("Enter Roll Number to delete: ")

    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            print("Student deleted successfully!\n")
            return

    print("Student not found!\n")


def main():
    while True:
        print("====== Student Management System ======")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting Program...")
            break
        else:
            print("Invalid Choice! Try Again.\n")


# Run the program
main()
