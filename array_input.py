#create an empty array and provide input values then Print index of searching element of array without using in-built function
from array import *
arr = array('i',[])
n = int(input("Enter the size of array : "))
for i in range(n):
    x = int(input("Enter the element : "))
    arr.append(x)
print(arr)

s = int(input("Enter the value for search : "))
k = 0
for e in arr:
    if e==s:
        print(k)
        break
    k+=1

#using in-built function
print(arr.index(s))


#write a code to reverse an array without using in-built function
c = array('i',[5,2,4,3,7])
n = len(c)
i=1
while i<=n:
    print(c[-i],end = " ")
    i=i+1
print()


#Create an array with 5 values & delete a value from array without using in-built function
arr = array("i",[])
n = int(input("Enter the length of array : "))
for i in range(n):
    x=int(input("Enter the value : "))
    arr.append(x)
print(arr)

h = int(input("Enter the value to be deleted : "))
for e in arr:
    if e==h:
        arr.remove(e)
        break
print(arr)


#Create an array with 5 values & delete a value from array based on index no without using in-built function
arr = array("i",[])
n = int(input("Enter the length of array : "))
for i in range(n):
    x=int(input("Enter the value : "))
    arr.append(x)
print(arr)

ind = int(input("Enter the index value to delete : "))
for e in range(n):
    if e==ind:
        arr.pop(e)
        break
print(arr)