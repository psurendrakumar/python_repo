def cube():
    n = 1
    while n<=10:
        result = n ** 3
        n+=1
        yield (result)


c1 = cube()

for i in c1:
    print(i)