# Lamda functions are the elegant way of creating one linear functions in python.
#This function doesnot have name.So,it is also called as Anonymous functions.
#We do not use lamda functions in the places where the functions should be called .
#We use it when we need a reference of the function.For example as a parameter in higher
#order functions like map reduce and filter.

def addition(x,y):
    return x+y
print(addition(2,3))#5

add=lambda x,y:x+y
print(add(2,3))#5

#maps()

nums=[1,2,3,4,5]
# def add_15_to_each(element):
#     return element +15

result=map(lambda element:element+15,nums) # map() returns a map object which is an iterator. But to see the
#actual data,we need to convert in to some other datatypes.
print(list(result))

from functools import reduce

result=map(lambda element:element**2,nums)
print(list(result))

result=filter(lambda element:element % 2==0,nums)
print(list(result))

result=reduce(lambda x,y:x+y,nums)
print(result)




