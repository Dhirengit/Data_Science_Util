'''
Poly Morphism
Many Form 

Way to create Polymorphism
1. Duck Typing
2. Operator Overloading
3. Method Overloading
4. Method Overriding
'''

# Duck Typing
class VSCode:
    def execute(self):
        print("Compliling")
        print("Running")

class MyEditor:
    def execute(Self):
        print("Optimize Code")
        print("Auto correction")
class Laptop:
    def code(self, ide):
        ide.execute()

# ide = VSCode()
ide = MyEditor()

lap1 = Laptop()
lap1.code(ide)

# 2. Operator Overloading
a= '5'
b = '6'

# print(7str.__add__(a,b))


class Student:

    def __init__(self, m1, m2):
        self.m1=m1
        self.m2=m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)

        return s3
    
    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = self.m1 + self.m2
        if r1 > r2:
            return True
        else:
            return False
        
    def __str__(self):
        return "{} {}".format(self.m1, self.m2)
            


s1 = Student(50,65)
s2 = Student(95,80)

# s3 = s1+s2
# print("s3", s3.m1)

if s1 > s2:
    print("S1 Win")
else:
    print("S2 Win")

a = 11
print("a", a,"a __str__", a.__str__())

print("s1", s1, "__str__",s1.__str__())

# Method Over loading

class OverLoading:

    def sum(self, a=None, b=None, c=None):
        s= 0
        if a!=None and b!=None and c!=None:
            s = a+b+c
        elif a!=None and b!=None:
            s = a+b
        else:
            s = a
        return s

check = OverLoading()
print(check.sum(11,15,3) )

