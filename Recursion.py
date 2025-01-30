#Findout factorial of a number using recursion
def fact(x):
    if x == 0:
        return 1
    return x * fact(x-1)


n = int(input("Enter a value : "))
result = fact(n)
print(result)



import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
i = 1
def greet():
    global i
    print("Hello",i)
    i += 1
    greet()


greet()




