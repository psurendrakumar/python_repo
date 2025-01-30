#Copy an image from one file to another file

f1 = open('Surendra_photo.jpg','rb')

f2 = open('my_pic.jpg','wb')

for data in f1:
    f2.write(data)