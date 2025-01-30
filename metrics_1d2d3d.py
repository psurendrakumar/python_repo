#1D Array: Single sequence of elements.
#2D Array: A grid of elements with rows and columns.
#3D Array: A stack of 2D arrays, often visualized as layers.

from numpy import *
array_1d = array([1, 2, 3, 4, 5])
print(f"1-Dimensional Array : {array_1d}")
print(array_1d.dtype)
print(array_1d.ndim)
print(array_1d.shape)
print(array_1d.size)

array_2d = array( [ [1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9] ]
                 )
print("2-Dimensional Array : ")
print(array_2d)
print(array_2d.dtype)
print(array_2d.ndim)
print(array_2d.shape)
print(array_2d.size)

array_3d = array( [[[1, 2],
                   [3, 4]],
                  [[5, 6],
                   [7, 8]],
                  [[9, 10],
                   [11, 12]] ]
                 )
print("3-Dimensional Array : ")
print(array_3d)
print(array_3d.dtype)
print(array_3d.ndim)
print(array_3d.shape)
print(array_3d.size)



arr1 = array( [ [1, 2, 3, 4, 5, 6],
                [7, 8, 9, 10, 11, 12] ]
            )
arr2 = arr1.flatten()       #Converting into 1-Dimensional Array
arr3 = arr1.reshape(4,3)    #Converting into 2-Dimensional Array
arr4 = arr1.reshape(2,2,3)  #Converting into 3-Dimensional Array
print(arr2)
print(arr3)
print(arr4)

#matrix in python
m = matrix('1 2 3;4 5 6;7 8 9')
print(m)
print(diagonal(m))
print(m.min())
print(m.max())


#Operations with matrix
m1 = matrix('1 2 3;4 5 6;7 8 9')
m2 = matrix('3 5 1;2 3 4;3 1 6')
m3 = m1 + m2
m4 = m1 * m2
print(m3)
print(m4)