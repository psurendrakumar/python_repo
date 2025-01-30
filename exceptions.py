try:
    age = int(input("Enter age : "))
    income = 20000
    risk = income/age
    print(risk)
except ValueError:
    print("Invalid value")
except ZeroDivisionError:
    print("age cannot be 0.")