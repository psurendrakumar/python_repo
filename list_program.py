names = ["surendra","jhansi","sirisha","madhu"]
print(names[1])
print(names[-2])
print(names[1:])
print(names[:])


names = ["surendra","jhansi","sirisha","madhu"]
names[1] = "jhanu"
print(names)


numbers = [3,6,2,8,10,14]
max = numbers[0]
for number in numbers:
    if number>max:
        max=number
print(max)