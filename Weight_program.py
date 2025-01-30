weight = int(input("Please Enter your Weight : "))
units = input("(L)bs or (K)g ? ")
if units.upper()=="L":
    converted = weight * 0.45
    print(f"Your weight is {converted} kilos")
else:
    converted = weight / 0.45
    print(f"Your weight is {converted} pounds")