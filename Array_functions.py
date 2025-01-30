from numpy import *

arr = array([1,2,3,4,5])
print(arr)

#Add 5 to an array
arr = arr+5
print(arr)

#Adding two arrays
arr1 = array([1,2,3,4,5])
arr2 = array([6,1,8,2,9])
arr3 = arr1+arr2
print(arr3)

#Concatenate two arrays
arr1 = array([1,2,3,4,5])
arr2 = array([6,1,8,2,9])
print(concatenate([arr1,arr2]))

arr = array([1,2,3,4,5])
print(sum(arr))
print(min(arr))
print(max(arr))
print(log(arr))
print(sin(arr))
print(cos(arr))
print(sqrt(arr))

#Method-1 : Using Alias(But in this method another array will not create in memory and addresses of arr1 & arr2 are same)
arr1 = array([1,2,3,4,5])
arr2 = arr1
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))

#Method-2 : Using Shallow copy
arr1 = array([1,2,3,4,5])
arr2 = arr1.view()
arr1[1] = 7  #if any value changed in arr1 it will automatically reflects in arr2
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))


#Method-3 : Using Deep copy
arr1 = array([1,2,3,4,5])
arr2 = arr1.copy()
arr1[1] = 7  #if any value changed in arr1 it will not reflects in arr2
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))

#Add 2 arrays using forloop(i.e : without using in-built function)
arr1 = array([1,5,3,4,5])
arr2 = array([6,1,3,2,4])
arr3 = zeros([len(arr1)],int)
for i in range(5):
    arr3[i] = arr1[i] + arr2[i]
print(arr3)


#Findout the maximum number from an array using forloop(i.e : without using in-built function)
arr = array([2,7,3,9,6])
temp = 0
for i in range(5):
    if temp < arr[i]:
        temp = arr[i]
print(temp)
