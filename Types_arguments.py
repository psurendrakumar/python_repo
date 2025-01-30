
#Positional arguments
def person(name,age):
    print(name)
    print(age)


person('surendra',32)


#Keyword arguments
def person(name,age):
    print(name)
    print(age)


person(age = 32,name = 'surendra')


#Default arguments
#Ex - 1 :
def person(name,age = 18):
    print(name)
    print(age)


person('surendra')

#Ex - 2 :
def person1(name,age = 18):
    print(name)
    print(age)


person1('surendra',28)


#Variable length arguments
#Ex - 1 :
def sum(a,b):
    c = a+b
    print(c)


sum(2,6)

#Ex - 2 :
def sum(a,*b):
    c = a
    for i in b:
        c = c+i

    print(c)


sum(2,6,4,1,5)


#Ex -3 :
def sum(*a):
    c = 0
    for i in a:
        c = c+i

    print(c)


sum(1,6,9,3,5)

#Keyworded Variable length arguments
#EX -1 :
def person(name,**data):
    print(name)
    print(data)


person('Surendra',age = 32,city = 'Mumbai',ph_no = 9848032919)

#EX -2 :
def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)


person('Surendra',age = 32,city = 'Mumbai',ph_no = 9848032919)


#EX -3 :
def person(**data):
    for i,j in data.items():
        print(i,j)


person(name = 'Surendra',age = 32,city = 'Mumbai',ph_no = 9848032919)





