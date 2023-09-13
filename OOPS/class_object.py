class Computer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram
    
    def config(self):
        print("Config is ", self.cpu, self.ram)

a = 5
# print(type(a))
com1= Computer("i5", 16)
com2= Computer("Rygen 3", 8)
# print(type(com1))

com1.config()
com2.config()

