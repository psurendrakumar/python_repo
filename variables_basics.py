a = 5
print(type(a))

b = 3.5
print(type(b))

c = 5+6j
print(type(c))

name = "surendra"
print(type(name))

#Even a single character in python should be a string data type
user = "s"
print(type(user))

k = a>b
print(k)
print(type(k))

s = a<b
print(s)
print(type(s))


a = 5.9 #Converting float to int
b = int(a)
print(b)
print(type(b))

c = float(b) #Converting int to float
print(c)
print(type(c))

m = 7
n = 8
r = complex(m,n)
print(r)
print(type(r))


lst = [10,25,46,71,85]
print(type(lst))

st = {24,14,65,36,25,44}
print(type(st))

tup = (14,29,54,67,93)
print(type(tup))

p = {'rahul' : 'apple','mahesh' : 'samsung','rajesh' : 'oneplus','krishna' : 'nothing'}
print(type(p))
print(p.keys())
print(p.values())
print(p['rajesh'])
print(p.get('rajesh'))


print(range(10))

print(type(range(10)))

print(list(range(0,10)))

print(list(range(2,10,2)))

