class car:

    wheels = 4
    def __init__(self):
        self.com = "BMW"
        self.mil = 10


obj1 = car()
obj2 = car()

obj1.mil = 8
car.wheels = 5

print(obj1.com,obj1.mil,obj1.wheels)
print(obj2.com,obj2.mil,obj2.wheels)