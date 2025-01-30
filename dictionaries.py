customer_data = {
    "name" : "surendra",
    "email" : "surendra.pechetti@gmail.com",
    "age" : 32,
    "is_mature" : True
}
print(customer_data["name"])
print(customer_data["email"])
print(customer_data["age"])
print(customer_data["is_mature"])


customer_data = {
    "name" : "surendra",
    "email" : "surendra.pechetti@gmail.com",
    "age" : 32,
    "is_mature" : True
}
customer_data["name"] = "basheer"
customer_data["dob"] = "29 july 1992"
print(customer_data["name"])
print(customer_data["email"])
print(customer_data["age"])
print(customer_data["is_mature"])
print(customer_data["dob"])



customer_data = {
    "name" : "surendra",
    "email" : "surendra.pechetti@gmail.com",
    "age" : 32,
    "is_mature" : True
}
print(customer_data["name"])
print(customer_data["email"])
print(customer_data["age"])
print(customer_data["is_mature"])
print(customer_data.get("doj","16 november 2023"))



phone_num = input("Enter phone number : ")
numbers_words = {
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four"
}

output = ""
for num in phone_num:
    #method-1 : output += numbers_words[num]+" "
    output += numbers_words.get(num) + " "
print(output)


phone_num = input("Enter phone number : ")
numbers_words = {
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four"
}

output = ""
for num in phone_num:
    output+=numbers_words.get(num,"!")+" "
print(output)


