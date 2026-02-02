print("--------------------------------------------------")
print("------------- Student Management System -----------")
print("--------------------------------------------------")

# declaring an empty dictionary for students (acts as a student table)
students = {}

# ---------------- CREATE ----------------
student_id = int(input("Please enter student id: "))
name = input("Please enter student name: ")
father_name = input("Please enter father name: ")
class_ = input("Please enter class: ")
school_name = input("Please enter school name: ")

students[student_id] = {
    "name": name,
    "father_name": father_name,
    "class": class_,
    "school_name": school_name
}

# ---------------- READ ----------------
print("\nStudent Details:")
print("ID:", student_id)
print("Name:", students[student_id]["name"])
print("Father Name:", students[student_id]["father_name"])
print("Class:", students[student_id]["class"])
print("School Name:", students[student_id]["school_name"])

# ---------------- UPDATE ----------------
print("\nUpdate Student Name")
students[student_id]["name"] = input("Enter new name: ")

# Display updated record
print("\nUpdated Student Details:")
print("Name:", students[student_id]["name"])
print("Father Name:", students[student_id]["father_name"])
print("Class:", students[student_id]["class"])
print("School Name:", students[student_id]["school_name"])

# ---------------- DELETE ----------------
print("\nDeleting student record...")
students[student_id].clear()

print("Student record after deletion:")
print(students[student_id])
