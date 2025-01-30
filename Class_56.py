#if class A only has init method if we call the constructor of "B" it will show "init method" of A

class A:

    def __init__(self):
        print("is A init")

    def feature1(self):
        print("Feature-1 is working")

    def feature2(self):
        print("Feature-2 is working")

class B(A):

    def feature3(self):
        print("Feature-3 is working")

    def feature4(self):
        print("Feature-4 is working")


a1 = B()



#if class A & B both has init methods if we call the constructor of "B" and use super method then it will show "init methods" of
#both A and B

class A:

    def __init__(self):
        print("is A init")

    def feature1(self):
        print("Feature-1 is working")

    def feature2(self):
        print("Feature-2 is working")

class B(A):

    def __init__(self):
        super().__init__()
        print("is B init")

    def feature3(self):
        print("Feature-3 is working")

    def feature4(self):
        print("Feature-4 is working")


a1 = B()



#MRO(Method Resolution Order) in this the preference is always on the left side class(i.e class A) :
class A:

    def __init__(self):
        print("is A init")

    def feature1(self):
        print("Feature1-A is working")

    def feature2(self):
        print("Feature-2 is working")

class B:

    def __init__(self):
        print("is B init")

    def feature1(self):
        print("Feature1-B is working")

    def feature4(self):
        print("Feature-4 is working")

class C(A,B):

    def __init__(self):
        super().__init__()
        print("is C init")

    def feat(self):
        super().feature2()


a1 = C()
a1.feature1()
a1.feat()



#Call both super classes A & B constructors in class C by without using super() method :

class A:

    def __init__(self):
        print("is A init")

    def feature1(self):
        print("Feature1-A is working")

    def feature2(self):
        print("Feature-2 is working")

class B:

    def __init__(self):
        print("is B init")

    def feature1(self):
        print("Feature1-B is working")

    def feature4(self):
        print("Feature-4 is working")

class C(A,B):

    def __init__(self):
        A.__init__(self)  # Explicitly call A's constructor
        B.__init__(self)  # Explicitly call B's constructor
        print("is C init")

    def feat(self):
        super().feature2()


a1 = C()
a1.feature1()
a1.feat()