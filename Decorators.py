#EX - 1 :
def decorator_1(func):
    def inner(x,y):
        if x<y:
            x,y = y,x
        func(x,y)
    return inner


@decorator_1
def div(a,b):
    print(a/b)


div(2,6)


#EX - 2
def decorator_2(func):
    def inner(x,y):
        if x%2 == 0 and y%2 ==0:
            func(x,y)
        else:
            print("Please enter even numbers only")
    return inner



@decorator_2
def sum(a,b):
    print(a+b)


sum(4,8)