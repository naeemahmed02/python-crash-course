# Enhanced Mini Resume Generator

print("="*35)
print("         MINI RESUME GENERATOR         ")
print("="*35)

# Inputs
name = input("Enter your full name: ").title()
age = input("Enter your age: ")
email = input("Enter your email: ").lower()
phone = input("Enter your phone number: ")
city = input("Enter your city: ").title()
hobby = input("Enter your favorite hobby: ").capitalize()
goal = input("What is your career goal? ").capitalize()

# Output
print("\n" + "="*35)
print("           YOUR MINI RESUME            ")
print("="*35)

print("Name      :", name)
print("Age       :", age + " years")
print("Email     :", email)
print("Phone     :", phone)
print("City      :", city)
print("Hobby     :", hobby)
print("Goal      :", goal)

print("\nThank you", name + "! Keep chasing your dream 🎯")
