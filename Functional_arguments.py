#Immutable object as argument - Integer
def update(x):
    print('Value of x ',x)
    print("Memory Address of 'x' before update",id(x))
    x=8
    print('Value of x after update',x)
    print("Memory Address of 'x' after update",id(x))

a=10
print('Value of a ',a)
print("Memory Address of 'a' before update",id(a))
update(a)
print('Value of a ',a)
print("Memory Address of 'a' after update",id(a))


#Mutable object as argument - List
def update(x):
    print('inside function, before update',spam)
    print('Memory address of list inside function, before update',id(spam))
    spam[1]=-3
    print('inside function, after update',spam)
    print('Memory address of list inside function, after update',id(spam))


spam=[1,2,3]
print('Items in list',spam)
print('Memory address of list',id(spam))
update(spam)
print('Items in updated list',spam)
print('Memory Address of updated list',id(spam))