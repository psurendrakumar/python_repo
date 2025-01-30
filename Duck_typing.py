#Duck typing
#Method-1 :
class duck:
    def sound(self):
        print("Qwack Qwack!")


class dog:
    def sound(self):
        print("Bow Bow!")


class cat:
    def sound(self):
        print("Meow Meow!")


def all_sounds(obj):
    obj.sound()


x = dog()
all_sounds(x)




#Duck typing
#Method-2 :
class duck:
    def sound(self):
        print("Qwack Qwack!")


class dog:
    def sound(self):
        print("Bow Bow!")


class cat:
    def sound(self):
        print("Meow Meow!")


class main_code:
    def all_sounds(self,obj):
        obj.sound()


x = duck()
y = main_code()
y.all_sounds(x)
