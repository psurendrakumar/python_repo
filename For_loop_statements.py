x = ['naveen',6,2.5]
for i in x:
    print(i)

y = 'Naveen'
for i in y:
    print(i)

z = range(10)
for i in z:
    print(i)

a = range(11,21,1)
for i in a:
    print(i)

b = range(11,21,3)
for i in b:
    print(i)

c = range(21,10,-1)
for i in c:
    print(i)

d = range(1,21)
for i in d:
    if i % 5 != 0:
      print(i)

#Print all perfect square numbers between 1 to 500
for i in range(1,501):
    if i**2<501:
        print(i**2)