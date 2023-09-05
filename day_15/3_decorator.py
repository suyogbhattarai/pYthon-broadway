# Decorators are the functions in Python which add extra functionality in the existing function
# It is created on the basis of closure concept


def extra_message(func):
    def inner_fxn(a,b):
        print("The sum of the numbers is:")
        return func(a,b)
    return inner_fxn
@extra_message

def addition(a,b):
    print(a+b)

addition(2,3)
def extra_message2(func):
     def inner_fxn():
         print("I am learning python")
         return func()
     return inner_fxn

@extra_message2
def message():
    print("Helllo World!")
message()

