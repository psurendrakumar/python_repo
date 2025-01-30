#Print Febinocci series without using function
n = int(input("Enter how many febinocci numbers you want : "))
a = 0
b = 1
if n<=0:
    print("Number is invalid")
elif n==1:
    print(a)
else:
    print(a)
    print(b)

    for i in range(2,n):
        c = a+b
        a = b
        b = c
        print(c)


#Print Febinocci series using function
def febinocci(x):
    a = 0
    b = 1
    if x<=0:
        print("Number is invalid")
    elif x==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,x):
            c = a+b
            a = b
            b = c
            print(c)

n = int(input("Enter how many febinocci numbers you want : "))
febinocci(n)



#Print Febinocci series using function and print within given input range
def febinocci(x):
    a = 0
    b = 1
    if x<=0:
        print("Number is invalid")
    elif x==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,x):
            c = a+b
            if c <= x:
                a = b
                b = c
                print(c)
            else:
                print("done")
                break

n = int(input("Enter the range of febinocci numbers you want to print : "))
febinocci(n)