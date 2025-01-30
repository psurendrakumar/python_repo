#Check whether the given number is positive or negative
x = int(input("Enter a number : "))

if x>=0:
    print("It is a positive number")
else:
    print("It is a negative number")
print("program completed")

#Biggest among 3 numbers
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))

if a > b and a > c:
    print("first number is big number")
elif b > c:
    print("second number is big number")
else:
    print("Third number is big number")
print("program completed")