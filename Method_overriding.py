#EX - 1 :
class parent:
    def method(self):
        print("This is parent method")

class child(parent):
    def method(self):
        print("This is child method")

c1 = child()
c1.method()



#EX - 2 :
class grandparent:
    def method(self):
        print("This is grandparent method")

class parent(grandparent):
    def method(self):
        print("This is parent method")

class child(parent):
    def method(self):
        print("This is child method")

c1 = child()
p1 = parent()

p1.method()
c1.method()



#EX - 3 :
class parent1:
    def method(self):
        print("This is parent1 method")

class parent2:
    def method(self):
        print("This is parent2 method")

class child(parent1,parent2):
    def method(self):
        print("This is child method")

c1 = child()

c1.method()



#EX - 4 :
class parent1:
    def method(self):
        print("This is parent1 method")

class parent2:
    def method(self):
        print("This is parent2 method")

class child(parent1,parent2):
    pass

c1 = child()

c1.method()



#EX - 5 :
class parent:
    def method(self):
        print("This is parent method")

class child(parent):
    def method(self):
        parent.method(self)
        print("This is child method")

c1 = child()
c1.method()