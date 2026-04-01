#multiple inheritance in python

class employee:
    def __init__(self, name):
        self.name = name
    def show(self):
        print(f"The dance is being performed by {self.name}")

class dancer:
    def __init__(self, dance):
        self.dance = dance
    def show(self):
        print(f"The name of the dance is {self.dance} ")

class danceremployee(employee, dancer):
    def __init__(self, name, dance):
        self.name = name
        self.dance = dance

n = danceremployee("Priya","Rajleela")
print(n.name)
print(n.dance)
n.show()
