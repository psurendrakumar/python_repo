a = 4
b = 2

try :
    print("Resource open")
    print(a/b)
    k = int(input("Enter a number : "))
    print(k)

except ZeroDivisionError as e:
    print("Hey,You cannot divide a number by zero",e)

except ValueError as e:
    print("Invalid input")

except Exception as e:
    print("Something went wrong........")

finally:
    print("Resource closed")