#Method over loading : If we pass more or less no. of arguments to a method it will execute without depending on number of arguments
# we have given in that method.

class A:
    def __init__(self,a,b=0,c=0):
        self.a = a
        self.b = b
        self.c = c

    def add(self):
        sum = self.a+self.b+self.c
        print(sum)


a1 = A(1,2,3)
a2 = A(1,2)
a3 = A(1)
a1.add()
a2.add()
a3.add()


#perform method over loading in python in general way
class B:
    def __init__(self,*args):
        self.args = args


    def add(self):
        total = 0
        for i in self.args:
          total+=i
        print(total)


b1 = B(1,2,3,4,5)
b1.add()


