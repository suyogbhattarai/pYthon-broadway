#If a function takes another functions as a parameter then it is called as
#higher order function.
# Examples are sort() method of list ,map(),reduce(),filter(),decorators etc.

#map() = It is a builtin function which takes two parameters.First parameters is a function and second
#parameter should be an iterable.

# It maps every element of the iterable to a new form.
# The count of the elements in the  iterable and final result is same in map()

nums=[1,2,3,4,5]
def add_15_to_each(element):
    return element +15

result=map(add_15_to_each,nums) # map() returns a map object which is an iterator. But to see the
#actual data,we need to convert in to some other datatypes.
print(list(result))

def raise_power_2_to_each(element):
    return element**2
result=map(raise_power_2_to_each,nums)
print(list(result))


#filter()=  It is a built-in function which takes two parameters.First parameters is a function and second
#parameter should be an iterable.

#It filters out certain elements of the iterable and retuns a new result.
#The count of the elements in  iterable and final result might not be same in filter().

nums=[1,2,3,4,5,6,7,8,9,10]

def pick_evens(element):
    if element % 2==0:
        return True

    return False

result=list(filter(pick_evens,nums))
print(result)

# reduce() = It is a built-in functions which takes two parameters.First parameter is a function and second
#parameter is an iterable

#It reduces the overall elements to a single value.
from functools import reduce

nums=[1,2,3,4,5,6,7,8,9,10]

def add_all_elements(x,y):
    return x+y

result=reduce(add_all_elements,nums)
print("The sum is:",result)



