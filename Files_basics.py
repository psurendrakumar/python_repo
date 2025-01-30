#Create a new file then Insert and Append the data into a file

f = open('my_data','w')        #Creating a new file

f.write("Hi\n")                #Inserting the data into a file
f.write("This is surendra kumar\n")
f.write("Working as a Python Developer\n")



f = open('my_data','a')        #Appending the data into a file
f.write("At Accenture india pvt.ltd\n")
f.write("currently looking for a better opportunity\n")






