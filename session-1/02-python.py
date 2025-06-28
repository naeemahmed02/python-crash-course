# Text Type Example

# Declaring string variables
name = "Naeem"
greeting = "Hello"

# String concatenation
message = greeting + ", " + name + "!"
print(message)

# String methods
print(name.upper())     # Output: NAEEM
print(name.lower())     # Output: naeem
print(name.replace("e", "3"))  # Output: Na3em

# String slicing
print(name[0:3])  # Output: Nae


# Numeric Type Examples

# Integer
age = 25
print("Age:", age)             # Output: Age: 25

# Float
pi = 3.1416
print("Value of Pi:", pi)      # Output: Value of Pi: 3.1416

# Complex
z = 2 + 3j
print("Complex Number:", z)    # Output: Complex Number: (2+3j)

# Type checking
print(type(age))   # <class 'int'>
print(type(pi))    # <class 'float'>
print(type(z))     # <class 'complex'>


# Boolean Type Example

# Boolean values
is_student = True
has_passed = False

# Using booleans in conditions
if is_student:
    print("Welcome, student!")      # This will print

if has_passed:
    print("Congratulations!")       # This will NOT print

# Boolean from expressions
x = 10
y = 5
print(x > y)    # True
print(x == y)   # False
print(bool(0))  # False
print(bool("Hello"))  # True

# String Manipulation

# Indexing

name = "Naeem"

print(name[0])   # Output: N
print(name[2])   # Output: e

# [-1] will get the last
print(name[-1])  # Output: m


# Slicing

text = "Python Programming"

print(text[0:6])   # Output: Python
print(text[7:])    # Output: Programming
print(text[:6])    # Output: Python

# Syntax: string[start:end] (end is not included)


# Built-in Methods

word = "python is fun"

print(word.upper())       # Output: PYTHON IS FUN
print(word.lower())       # Output: python is fun
print(word.title())       # Output: Python Is Fun
print(word.replace("fun", "awesome"))  # Output: python is awesome




