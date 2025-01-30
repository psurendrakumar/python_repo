#Ways of creating array using Numpy
from numpy import *

#using array()
arr1 = array([1,3,5,2,4,6])
arr2 = array([1,3,5,2,4.2,6])
arr3 = array([1,3,5,2,4,6],int)
arr4 = array([1,3,5,2,4,6],float)
print(arr1)
print(arr2)
print(arr3)
print(arr3.dtype)
print(arr4)
print(arr4.dtype)

#using zeros()
arr1 = zeros(5)
arr2 = zeros(5,int)
print(arr1)
print(arr2)

#using ones()
arr1 = ones(5)
arr2 = ones(5,int)
print(arr1)
print(arr2)

#using linspace()
arr1 = linspace(0,15,16)
arr2 = linspace(0,15,20)
arr3 = linspace(0,15)
print(arr1)
print(arr2)
print(arr3)


#using arange()(i.e : same like range())
arr = arange(0,15,2)
print(arr)

#using logspace()
arr = logspace(1,40,5)
print(arr)
print('%.2f' %arr[0])
print('%.2f' %arr[4])

