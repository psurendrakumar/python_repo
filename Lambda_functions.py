
#lambda functions
f = lambda a : a * a

result = f(5)
print(result)


f = lambda a,b : a + b

result = f(5,6)
print(result)



#Explanation using lambda functions filter(),map(),reduce()

from functools import reduce

lst = [5,2,6,7,3,4,9,8,1]

evens = list(filter(lambda a : a%2 ==0,lst))
print(evens)

doubles = list(map(lambda a : a*2,evens))
print(doubles)

sum = reduce(lambda a,b : a+b,doubles)
print(sum)


#Explanation without using lambda functions filter(),map(),reduce()

from functools import reduce
lst = [5,2,6,7,3,4,9,8,1]

def is_even(n):
    return n%2 == 0  #lambda a : a%2 ==0


evens = list(filter(is_even,lst))
print(evens)


def update(n):
    return n*2       #lambda a : a*2


doubles = list(map(update,evens))
print(doubles)



def add_all(m,n):
    return m+n      #lambda a,b : a+b


sum = reduce(add_all,doubles)
print(sum)



#Findout Factorial of a number using lambda function
from functools import reduce
n = int(input("Enter a number: "))
lst = []
for i in range(1, n+1):
    lst.append(i)
print(lst)
factorial = reduce(lambda a, b: a * b,lst)
print(factorial)