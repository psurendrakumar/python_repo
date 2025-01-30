for item in "Python":
    print(item)

for item in [10,20,30,40]:
    print(item)

for item in ["surendra","jhansi","chitti","madhu"]:
    print(item)

for item in range(10):
    print(item)

for item in range(5,10):
    print(item)

for item in range(5,10,2):
    print(item)


prices =[10,20,30,40]
total = 0
for price in prices:
    total+=price
print(f"Total sum : {total}")


numbers = [5,2,5,2,2]
for x_count in numbers:
    print("x"*x_count)

numbers = [5,2,5,2,2]
for x_count in numbers:
    output = ""
    for x_count in range(x_count):
        output +='x'
    print(output)

