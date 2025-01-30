x = 5
y = 4
z = x+y
print(z)

#Swaping of two strings
a = 5
b = 6
print(a)
print(b)

#Method-1(Using third variable)
a = 5
b = 6

temp = a
a = b
b = temp
print(a)
print(b)

#Method-2(Using '+'&'-')
a = 5
b = 6

a = a+b
b = a-b
a = a-b
print(a)
print(b)

#Method-3(Using XOR)
a = 5
b = 6

a = a^b
b = a^b
a = a^b
print(a)
print(b)

#Method-4(Using special operation)
a = 5
b = 6

a,b = b,a

print(a)
print(b)

#Enter a character as input
ch = input("Enter a character : ")
print(ch)

ch1 = input("Enter a character : ")
print(ch1[0])

ch2 = input("Enter a character : ")[0]
print(ch2)

#Enter an expression as input
result = eval(input("Enter expression : "))
print(result)