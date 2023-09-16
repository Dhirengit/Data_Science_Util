'''
1. Single Inheritance A, B(A)
2. Multilevel  A, B(A) , C(B)
3. Multiple Inheritance A, B, C(A,B)
4. Hiercharical
'''


'''
If you create object of sub class it will first try init of sub class
If it is not found then it will call init of Super class
'''
class SuperClass:

    def __init__(self):
        print("init Superclass")

    def feature1(self):
        print("Feature 1 Called")


class SubClass():

    def __init__(self):
        super().__init__() #  super() You can Access all of Super/Parent Class
        print("init SubClass")

    def feature2(self):
        print("Feature 2 Called")


class MultipleClass(SuperClass,SubClass):
    def __init__(self):
        super().__init__() #  super() You can Access all of Super/Parent Class
        print("init MultipleClass")

# a = SuperClass()
# a.feature1()

# child = SubClass()
# child.feature1()
# child.feature2()

# multi = MultipleClass()
