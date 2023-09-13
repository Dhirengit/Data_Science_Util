class Computer():

    make = "Dell" # This is Class or Static Variable
    
    def __init__(self):
        self.name = "Dhiren"
        self.age = 28
        # above 2 is instance variable

    # def update(self):
    #     self.age =30
    
    def compare(self, other):
        if self.age == other.age :
            return True
        else :
            return False

c1 = Computer()
c1.age = 30
c2 = Computer()

if c1.compare(c2):
    print("Object Same")

# c1.update()
print(c1.name)
print(c2.name)