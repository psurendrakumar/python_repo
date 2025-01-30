import math

x=2.9
print(math.ceil(x))
print(math.floor(x))


is_hot = True
is_cold = False

if is_hot:
    print("it's a Hot day")
    print("Drink plenty of water")
elif is_cold:
    print("it's a Cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")



is_hot = False
is_cold = True

if is_hot:
    print("it's a Hot day")
    print("Drink plenty of water")
elif is_cold:
    print("it's a Cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")


is_hot = False
is_cold = False

if is_hot:
    print("it's a Hot day")
    print("Drink plenty of water")
elif is_cold:
    print("it's a Cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")


price = 1000000
is_good_credit = True

if is_good_credit:
    down_payment = 0.1*price
else:
    down_payment = 0.2*price
print(f"Down Payment : ${down_payment}")
