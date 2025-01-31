#EX - 1 :

names = ["surendra","raju","praveen","surendra"]
comp = ["Dell","Apple","Hp","Dell"]

zipped = list(zip(names,comp))
zipped1 = set(zip(names,comp))
zipped2 = dict(zip(names,comp))

print(zipped)
print(zipped1)
print(zipped2)



#EX - 2 :

names = ["surendra","raju","praveen"]
comp = ["Dell","Apple","Hp"]

zipped = zip(names,comp)

for (a,b) in zipped:
    print(a,b)