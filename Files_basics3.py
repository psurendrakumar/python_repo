#Copying data from one file to another file

f1 = open('my_data','r')

f2 = open('abc','w')

for data in f1:
    f2.write(data)