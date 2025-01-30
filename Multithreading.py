
from time import *
from threading import *

class hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

class hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)


t1 = hello()
t2 = hi()


t1.start()
sleep(0.2)
t2.start()

t1.join()
t2.join()

print("Bye")




import time
from threading import *

def calc_square(numbers):
    for i in numbers:
        print("Square of number",i)
        print(i * i)
        sleep(1)


def calc_cube(numbers):
    for i in numbers:
        print("cube of number",i)
        print(i * i * i)
        sleep(1)


initial_time = time.time()

l = [1,2,3,4,5]


t1 = Thread(target = calc_square,args = (l,))
t2 = Thread(target = calc_cube,args = (l,))

t1.start()
sleep(0.2)
t2.start()

t1.join()
t2.join()

print("Time taken : ",time.time()- initial_time)