# Parent class
class Person:
    
    def __init__(self, name, father_name, city, email, phone_number, age):
        self.name = name
        self.father_name = father_name
        self.city = city
        self.email = email
        self.phone_number = phone_number
        self.age = age
    
    def showInfo(self):
        return f"Name: {self.name}\nFather Name: {self.father_name}\nAge: {self.age}"
    
    def contact(self):
        return f"Email: {self.email}\nPhone Number: {self.phone_number}"
    

class Student(Person):
    
    def __init__(self, student_id, course, stu_class,
                 name, father_name, city, email, phone_number, age, balance):
        self.student_id = student_id
        self.__balance = balance
        self.course = course
        self.stu_class = stu_class
        super().__init__(name, father_name, city, email, phone_number, age)
        
    
    def showInfo(self):
        return f"{super().showInfo()}\n Student Id: {self.student_id}\n Course: {self.course}\nClass: {self.stu_class}\nBalance: {self.get_balance()}"
    
    def get_balance(self):
        return self.__balance
    
    
stud_obj = Student(
   101,
    "Computer Science",
    "CS-3A",
    "Ali Khan",
    "Ahmed Khan",
    "Lahore",
    "ali.khan@example.com",
    "+92-300-1234567",
    20,
    979759
)

print(stud_obj.get_balance())
