#You can create object of inner class inside the outer class (or)
#You can create object of inner class outside the outer class provided you use outer class name to call it.


#EX-1 : You can create object of inner class inside the outer class
class student:

    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no
        self.lapA = self.laptop('HP','i5',8)          #constructor of inner class laptop
        self.lapB = self.laptop('Dell','i9',16)


    def show(self):
        print(self.name,self.roll_no)


    class laptop:

        def __init__(self,brand,cpu,ram):
            self.brand = brand
            self.cpu = cpu
            self.ram = ram


        def config(self):
            print(self.brand,self.cpu,self.ram)




s1 = student('surendra',230)
s2 = student('jhansi',240)

s1.show()
s1.lapA.config()
s2.show()
s2.lapB.config()




#EX-2 : You can create object of inner class outside the outer class
class student:

    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no


    def show(self):
        print(self.name,self.roll_no)


    class laptop:

        def __init__(self,brand,cpu,ram):
            self.brand = brand
            self.cpu = cpu
            self.ram = ram


        def config(self):
            print(self.brand,self.cpu,self.ram)




s1 = student('surendra',230)
s2 = student('jhansi',240)

lapA = student.laptop('HP','i5',8)       #constructor of inner class laptop
lapB = student.laptop('Dell','i9',16)

s1.show()
lapA.config()
s2.show()
lapB.config()




#EX-3 :
class geometry:

    def __init__(self):
        self.r1 = self.rectangle()
        self.t1 = self.triangle()


    class rectangle:

        def __init__(self):
            self.length = int(input("Enter the length : "))
            self.breadth = int(input("Enter the breadth : "))


        def show(self):
             self.area = self.length * self.breadth
             print("Area of the rectangle ",self.area)


    class triangle:

        def __init__(self):
                     self.height = int(input("Enter the height : "))
                     self.base = int(input("Enter the base : "))


        def show(self):
                     self.area = 0.5 * self.height * self.base
                     print("Area of the triangle ", self.area)


g1 = geometry()

g1.r1.show()
g1.t1.show()