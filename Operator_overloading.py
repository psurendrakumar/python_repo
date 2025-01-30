class maths:

    def __init__(self,a,b):
        self.a = a
        self.b = b


    def __add__(self, other):
        return self.a+other.a , self.b+other.b


p1 = maths(2,5)
p2 = maths(3,4)

print(p1+p2)




class maths:

    def __init__(self,length,breadth,width):
        self.length = length
        self.breadth = breadth
        self.width = width


    def volume(self):
        return self.length*self.breadth*self.width


    def __gt__(self, other):

        if self.volume() > other.volume():
            return True
        else:
            return False


p1 = maths(2,8,7)
p2 = maths(3,4,9)

print("Volume of p1:", p1.volume())
print("Volume of p2:", p2.volume())

# Compare volumes
if p1 > p2:
    print("p1 is bigger")
else:
    print("p2 is bigger")





