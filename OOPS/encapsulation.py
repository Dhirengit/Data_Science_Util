'''
Encapsulation is a fundamental principle in object-oriented programming that focuses on bundling data and the methods that operate
on that data into a single unit called a class.It allows you to control the access and visibility  of the data and methods, 
providing a way to protect and organize your code
'''

# Access Modifier ---> Encalsulation
# Private Access Modifiers

class Person:
    # Constructor
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def display_info(self):
        print(f"the person name is {self.__name} and age is {self.__age}")

person = Person("Dhiren", 28)
# print("person", person._Person__name) # __ means this variable or method is private DOn not assign Private variable  Not Good Practice
# print(dir(person)) # Get all methods 

# person.display_info()

# Protected Access Modifiers
class Person:
    # Constructor
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def display_info(self):
        print(f"the person name is {self._name} and age is {self._age}")

# person = Person("Dhiren", 28)
# print("person", person._age) # _ means this variable or method is protected  Do not assign Private variable 
# print(dir(person))

# person.display_info()

class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def display_info(self):
        print(f"the Person name is {self._name} and age is {self._age}")

student1 = Student("DB", 29)
student1.display_info( )


# Public Access Modifiers
class Person:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age