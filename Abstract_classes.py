from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        pass

    def method2(self):
        print("This is concrete method")

    @abstractmethod
    def method3(self):
        pass

    @abstractmethod
    def method4(self):
        pass


class B(A):
    def method1(self):
        print("method1 is implemented in sub-class")

    def method3(self):
        print("method3 is implemented in sub-class")

    def method4(self):
        print("method4 is implemented in sub-class")

obj = B()
obj.method1()
obj.method2()
obj.method3()
obj.method4()



from abc import ABC,abstractmethod
from math import sqrt

class polygon(ABC):
    @abstractmethod
    def sides(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def figure(self):
        return "It is a 2-dimensional plane figure"


class Rectangle(polygon):
    def sides(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2*(self.length + self.breadth)

    def extramethod(self):
        return "reactangle has 4 sides"


class Triangle(polygon):
    def sides(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = self.perimeter()
        return sqrt(s*(s-self.a) * (s-self.b) * (s-self.c))

    def perimeter(self):
        return (self.a+self.b+self.c)/2

    def extramethod(self):
        return "triangle has 3 sides"


class Square(polygon):
    def sides(self,side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side

    def extramethod(self):
        return "square has 4 sides"


rect = Rectangle()
rect.sides(10,20)
tri = Triangle()
tri.sides(10,20,30)
sqr = Square()
sqr.sides(10)

for i in [rect,tri,sqr]:
    print(i.area())
    print(i.perimeter())
    print(i.extramethod())
    print(i.figure())





