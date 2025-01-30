#EX - 1 :
a = 10  #Global Variable

def something():
    a = 15  #Local Variable
    print("'a' value inside the function ",a)


something()
print("'a' value outside the function ",a)


#EX - 2 :
a = 10  #Global Variable

def something():
    global a   #Global Variable
    a = 15
    print("'a' value inside the function ",a)


something()
print("'a' value outside the function ",a)


#EX - 3 :
a = 10  #Global Variable
print(id(a))

def something():
    a = 9                 #Local Variable
    x = globals() ['a']   #Global Variable
    print(id(x))
    globals()['a'] = 15   #Update the Global Variable
    print("'a' value inside the function ",a)


something()
print("'a' value outside the function ",a)