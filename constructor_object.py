
class computer:

    def __init__(self):
        self.name = 'surendra'
        self.age = 32


obj1 = computer()
obj2 = computer()

print(obj1.name,obj1.age)
print(obj2.name,obj2.age)




class computer:

    def __init__(self):
        self.name = 'surendra'
        self.age = 32


obj1 = computer()
obj2 = computer()

print(obj1.name,obj1.age)
print(obj2.name,obj2.age)

obj1.name = 'madhu'
obj1.age = 28

print(obj1.name,obj1.age)
print(obj2.name,obj2.age)




class computer:

    def __init__(self):
        self.name = 'surendra'
        self.age = 32


    def update(self):
        self.age = 35

obj1 = computer()
obj2 = computer()

obj1.name = 'naveen'
obj1.update()

print(obj1.name,obj1.age)
print(obj2.name,obj2.age)





class computer:

    def __init__(self):
        self.name = 'surendra'
        self.age = 32


    def compare(self,other):       #self means obj1 and other means obj2
        if self.age == other.age:
            return True
        else:
            return False

obj1 = computer()
obj2 = computer()

obj1.age = 35

if obj1.compare(obj2):
    print("Both are same")
else:
    print("Both are different")