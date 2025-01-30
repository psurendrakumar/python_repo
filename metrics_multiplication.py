from numpy import *
arr1 = zeros((2, 3),int)
arr2 = zeros((3, 2),int)
result = zeros((2, 2),int)

print('Enter values in first matrix : ')
for i in range(2):
    for j in range(3):
        arr1[i][j] = int(input(f"Enter value for arr1[{i}][{j}]: "))

print('Enter values in second matrix : ')
for i in range(3):
    for j in range(2):
        arr2[i][j] = int(input(f"Enter value for arr2[{i}][{j}]: "))

# Perform matrix multiplication manually
for i in range(2):
    for j in range(2):
        for t in range(3):
            result[i][j] += arr1[i][t] * arr2[t][j]

# Print the result
print("Resultant Matrix : ")
print(result)
