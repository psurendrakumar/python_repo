from array import *
vals = array('i',[3,5,-9,10,23])
print(vals)

vals = array('i',[3,5,-9,10,23])
print(vals[0])
print(vals[1])
print(vals[2])

#Using Array Functions
vals = array('i',[3,5,-9,10,23])
print(vals.buffer_info())

vals = array('i',[3,5,-9,10,23])
print(vals.typecode)

vals = array('i',[3,5,-9,10,23])
vals.reverse()
print(vals)

#Using For Loop
vals = array('i',[3,5,-9,10,23])
for i in range(5):
    print(vals[i])


vals = array('i',[3,5,-9,10,23])
for i in range(len(vals)):
    print(vals[i])

vals = array('i',[3,5,-9,10,23])
for e in vals:
    print(e)

#Using While Loop
vals = array('i',[3,5,-9,10,23])
i = 0
while i<len(vals):
    print(vals[i])
    i+=1

#Copy one Array values into another Array(with their square values)
vals = array('i',[3,5,9,7,2])
newArr = array(vals.typecode,[a*a for a in vals])
for e in newArr:
    print(e)

#Factorial of given number
x=int(input("Enter a value : "))
fact=1
for i in range(1,x+1):
    fact=fact*i
print(fact)


#Method - 1 : Print the values of an array in Ascending order using built-in function
vals = array('i',[3,5,9,7,2])
result = sorted(vals)
print(result)


#Method - 2 : Print the values of an array in Ascending order using logic
array_values = [2, 5, 1, 3, 6]
# Implement Bubble Sort
n = len(array_values)
for i in range(n):
    for j in range(0, n - i - 1):
        if array_values[j] > array_values[j + 1]:
            # Swap elements
            array_values[j], array_values[j + 1] = array_values[j + 1], array_values[j]

# Print the sorted array
print(array_values)