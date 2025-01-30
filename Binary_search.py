#Binary search

pos = 0
def search(list,s):
    lower = 0
    higher = len(list)-1

    while lower<=higher:
        mid = (lower + higher) // 2
        if list[mid] == s:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < s:
                lower = mid+1
            else:
                higher = mid - 1
    return False


list = []
n = int(input("Enter the size of list : "))

for i in range(n):
    e = int(input("Enter the element : "))
    list.append(e)

list.sort()
print(list[0:])

s = int(input("Enter the value to search from the list : "))


if search(list,s):
    print("Founded at position",pos)
else:
    print("Not Found")