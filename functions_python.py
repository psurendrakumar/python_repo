def greet():
    print("Hello")
    print("Good Morning")

def add(x,y):
    c = x+y
    print(c)

def add_rtn(x,y):
    c = x+y
    return c

def add_sub(x,y):
    c = x+y
    d = x-y
    return c,d

greet()
add(5,4)
result = add_rtn(5,3)
print(result)
result1,result2 = add_sub(9,5)
print(result1,result2)






