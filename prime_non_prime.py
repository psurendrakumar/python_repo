#Check whether the given number is Prime or Not

#Method - 1 :
num = int(input("Enter the number : "))
if num < 2:
    print("Not a prime number")
else:
    for i in range(2,num):
        if num % i == 0:
            print("It is not a Prime number")
            break
    else:
        print("It is a Prime number")


#Method - 2 :
from math import *
x = int(input("Enter the number: "))
if x < 2:
    print("Not a prime number")
elif x == 2:  # Special case for 2
    print("Prime number")
else:
    for i in range(2, ceil(sqrt(x)) + 1):  # Check divisors from 2 to sqrt(x)
        if x % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")


#Print fibonacci numbers below 50
# Initializing the first two Fibonacci numbers
a, b = 0, 1

# Loop to print Fibonacci numbers less than 50
while a < 50:
    print(a)
    a, b = b, a + b  # Update a and b