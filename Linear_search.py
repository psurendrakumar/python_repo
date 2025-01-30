#Linear search using while loop

pos = 0
def search(list,s):
    i = 0
    while i<len(list):
        if list[i] == s:
            globals()['pos'] = i
            return True
        i+=1
    else:
        return False


list = []
n = int(input("Enter the size of list : "))

for i in range(n):
    e = int(input("Enter the element : "))
    list.append(e)

print(list[0:])

s = int(input("Enter the value to search from the list : "))

if search(list,s):
    print("Founded at position",pos)
else:
    print("Not Found")



#Linear search using for loop

pos = 0
def search(list,s):
    for i in range(len(list)):
        if list[i] == s:
            globals()['pos'] = i
            return True
    else:
        return False


list = []
n = int(input("Enter the size of list : "))

for i in range(n):
    e = int(input("Enter the element : "))
    list.append(e)

print(list[0:])

s = int(input("Enter the value to search from the list : "))

if search(list,s):
    print("Founded at position",pos)
else:
    print("Not Found")