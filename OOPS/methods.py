'''
Method's Type 
1. Instance methods
2. Class methods
3. Static methods
'''

class Student:

    school = "Sarva Vidhyalay"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def awg(self):
        return (self.m1+self.m2+self.m3) /3
    
    @classmethod
    def getschool(cls):
        return cls.school
    
    @staticmethod
    def info():
        print("This is Student Class...")
    
s1 = Student(31,58,65)
# s2 = Student(85,16,98)

print(s1.awg())
print(Student.getschool())

Student.info()
