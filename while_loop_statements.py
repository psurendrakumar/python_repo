i = 1
while i <= 5:
    print("Telusko",end = "")
    j = 1
    while j <=4:
        print("Rocks", end = "")
        j+=1
    i+=1
    print()

#Print numbers from 1-100 and skip the numbers which are divisible by 3 & 5
i = 1
while i<=100:
    j = i % 3
    k = i % 5
    if j!=0 and k!=0:
        print(i)
    i+=1


#Print output like below
#####
#####
#####
#####

i = 1
while i <= 4:
    print("#",end = "")
    j = 1
    while j <=4:
        print("#", end = "")
        j+=1
    i+=1
    print()