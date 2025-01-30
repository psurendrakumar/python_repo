for i in range(4):
    for j in range(4):
        print("# ",end = "")
    print()


for i in range(4):
    for j in range(i+1):
        print("# ",end = "")
    print()


for i in range(4):
    for j in range(4-i):
        print("# ",end = "")
    print()


#Method - 1
for i in range(4):
    for j in range(4-i):
        x = i + 1
        print(x,end = "")
        i+=1
    print()

#Method - 2
for i in range(1,5):
      for j in range(i,5):
        print(j,end = "")
      print()


x='ABCD'
y='PQR'
for i in range(1,5):
    print(x[:i]+y[i-1:])


