class computer:           #class

    def config(self):     #method
        print("i5, 16gb RAM, 1TB ROM")


obj = computer()          #obj means Object  #Total line is called constractor

computer.config(obj)
obj.config()



class computer:

    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram


    def config(self):
        print("Configuration is ",self.cpu,self.ram )


obj1 = computer('i5',16)
obj2 = computer('Razon 3',8)


obj1.config()
obj2.config()