class student:

    school = 'Pragati'
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3


    def avg(self):              #Instance method
        return (self.m1+self.m2+self.m3)/3


    @classmethod
    def getschool(cls):
        return cls.school


    @staticmethod
    def info():
        print("This is student class....")


obj1 = student(65,86,92)
obj2 = student(85,90,96)

print(obj1.avg())
print(obj2.avg())

print(student.getschool())
student.info()

