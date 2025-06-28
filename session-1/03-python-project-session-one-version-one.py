# Bio Card Generator

print("===== Bio Card Generator =====\n")

# Input
name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
hobby = input("Enter your hobby: ")

# String Manipulation
name = name.title()
city = city.title()
hobby = hobby.capitalize()

# Output
print("\n===== Your Bio Card =====")
print("Name   :", name)
print("Age    :", age + " years old")
print("City   :", city)
print("Hobby  :", hobby)
print(f"Welcome {name}! Happy {hobby} 😊")
