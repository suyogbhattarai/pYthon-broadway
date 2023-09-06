
# Take two numbers input and divide a number by another number. Handle the possible exceptions.


try:
    num1=int(input("Enter a number"))
    num2=int(input("Enter another number"))
    a=num1 / num2
except (ZeroDivisionError,ValueError):
    print("Please do not divide by zero")

else:
    print(a)





