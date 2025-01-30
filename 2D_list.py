metrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
metrix[0][2] = 30
print(metrix[0][0])
print(metrix[0][1])
print(metrix[0][2])
print(metrix[1][0])
print(metrix[1][1])
print(metrix[1][2])
print(metrix[2][0])
print(metrix[2][1])
print(metrix[2][2])

for row in metrix:
    for item in row:
        print(item)