av = 8
x = int(input("Enter how many candies you want : "))
i = 1
while i<=x:
    if i > av:
        print("Out of stock")
        break
    print("candy")
    i+=1
print("Exit")


for i in range(1,101):
    if i % 3 == 0:
        continue
    print(i)
print("Exit")


for i in range(1,101):
    if i % 3 == 0 or i % 5 == 0:
        continue
    print(i)
print("Exit")


for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        continue
    print(i)
print("Exit")


for i in range(1,101):
    if i % 2 != 0:
        pass
    else:
        print(i)
print("Exit")



#Print fibonacci numbers below 50
x=0
y=1
print('The Fibonacci Series will be:\n')
print(x)
print(y)
i=1
while i<=48:
    z=x+y
    if z > 50:  # Stop printing if the Fibonacci number exceeds 50
        break
    print(z)
    x=y
    y=z
    i+=1


for i in range(5):
    if i==3:
        continue
    print("Hello ",i)


for i in range(5):
    if i==3:
        break
    print("Hello ",i)

