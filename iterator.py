#EX - 1 : Create Iteration using built-in functions

lst = [2,3.6,8,5,"surendra"]

x = iter(lst)

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))


#EX - 2 : Create Iteration using built-in functions

lst = [2,3.6,8,5,"surendra"]

x = lst.__iter__()

print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())



#EX - 1 : Creating our own iterators

class number:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return (self)

    def __next__(self):
        if self.num<=20:
            result = self.num
            self.num += 1
            return result
        else:
            raise StopIteration


x = number()       #x is Iterable object(because we used 'iter' and 'next' methods in the class)

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))


#EX - 2 : Creating our own iterators

class number:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return (self)

    def __next__(self):
        if self.num<=20:
            result = self.num
            self.num += 1
            return result
        else:
            raise StopIteration


x = number()            #x is Iterable object(because we used 'iter' and 'next' methods in the class)

for i in x:
    print(i)


