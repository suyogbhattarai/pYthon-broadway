import math

radius=float(input("Enter the radius"))
area=math.pi*radius*2
print(area)#task 1

# task 2
n=int(input("Enter a solid number to check its frequency"))
list=[5,2,3,5,3,2,3,3,1,4]
result=list.count(n)
print(f"The number given is repeated {result} times")
