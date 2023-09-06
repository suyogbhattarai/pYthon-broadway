#Take two numbers as input and add those numbers. Handle the possible exceptions.
try:
    num1=int(input("Enter your 1st number"))
    num2=int(input("Enter your 2nd number"))
except ValueError:
    print("Input a number, not character")
else:
    print(num1)
    print(num2)
    print(num1+num2)
