# === Step 1: Registration ===

print("===== Welcome to Course Portal =====\n")

# Get user details (input + string manipulation)
name = input("Enter your full name: ").title()
email = input("Enter your email: ").lower()
password = input("Set a password: ")

# Store student info as a tuple
student = (name, email, password)

print("\nRegistration successful!\n")

# === Step 2: Show Available Courses ===

print("Available Courses:")
courses = ["Python", "Web Development", "Data Science", "AI", "Flutter"]

# Print courses one by one using index manually (no loops yet)
print("1.", courses[0])
print("2.", courses[1])
print("3.", courses[2])
print("4.", courses[3])
print("5.", courses[4])

# === Step 3: Course Selection ===

fav_course = input("\nEnter your favorite course from the list above: ").title()

# Add the course to a list of registered courses
registered_courses = []
registered_courses.append(fav_course)

# Optional: Add another course (just to show list can grow)
second_course = input("Enter another course you want to register (or press Enter to skip): ").title()

if second_course != "":
    registered_courses.append(second_course)

# === Step 4: Display Final Student Profile ===

print("\n===== Registration Complete =====")
print("Name     :", student[0])
print("Email    :", student[1])
print("Password :", "*" * len(student[2]))  # hide password with asterisks

print("\nRegistered Courses:")
print(", ".join(registered_courses))
