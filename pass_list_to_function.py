#count number of even and odd numbers
def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i%2 == 0:
            even+=1
        else:
            odd+=1
    return even,odd


lst = [3,4,7,1,8,2,6,10,5]
even,odd = count(lst)
print(f"even : {even} and odd : {odd}")


#count of names which are having more than 5 characters and less than 5 characters
def calculate(x):
    a = 0
    b = 0
    for i in x:
        if len(i)>5:
            a +=1
        else:
            b+=1
    return a,b


lst=[]
for i in range (10):
    x=(input("Enter names : "))
    lst.append(x)
print(lst)
#lst = ['surendra','jhansi','balu','chitti','raju','suresh','kasu','yogi','naresh','madhu']
a,b = calculate(lst)
print(f"names with more than 5 characters : {a} and names with less than 5 characters : {b}")