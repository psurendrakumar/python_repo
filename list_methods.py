numbers = [5,2,1,7,4]
numbers.append(10)
print(numbers)

numbers = [5,2,1,7,4]
numbers.insert(0,20)
print(numbers)

numbers = [5,2,1,7,4]
numbers.remove(5)
print(numbers)

numbers = [5,2,1,7,4]
numbers.clear()
print(numbers)

numbers = [5,2,1,7,4]
numbers.pop()
print(numbers)

numbers = [5,2,1,7,4]
numbers.pop(3)
print(numbers)

numbers = [5,2,1,7,4]
numbers.sort()
print(numbers)

numbers = [5,2,1,7,4]
numbers.reverse()
print(numbers)

numbers = [5,2,1,7,4]
numbers.sort()
numbers.reverse()
print(numbers)

numbers = [5,2,1,7,4]
print(max(numbers))
print(min(numbers))
print(sum(numbers))

numbers = [5,2,1,7,4]
numbers.extend([8,3,9])
print(numbers)

numbers = [5,2,1,7,4]
del numbers[2:]
print(numbers)

numbers = [5,2,1,7,4]
print(numbers.index(5))

numbers = [5,2,1,7,4]
print(50 in numbers)

numbers = [5,2,1,5,7,4]
print(numbers.count(5))

numbers = [5,2,1,7,4]
numbers2 = numbers.copy()
numbers.append(10)
print(numbers2)
print(numbers)



numbers = [5,2,1,5,3,7,4,2,3]
uniques = []
for number in numbers:
    if number not in uniques:
       uniques.append(number)
print(uniques)


#print two different lists together
names = ['surendra','naveen','raju','vasudev']
mail = [numbers,names]

print(mail)