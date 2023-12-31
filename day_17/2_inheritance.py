#Inheritance is one of the features of OOP.
#Using inheritance we can access the properties and methods of a parent class from
# its children classes

class A:
    pass

class B(A): #Inheriting class "A" in a child class "B"
    pass

#Types of inheritance:

#1. Single Inheritance
#2. Multilevel Inherintance
#3. Multiple Inheritance
#4. Hierarchial Inheritance
#5. Hybrid Inheritance.


# Single Inheritance
# In this inheritance a single Child class inherits the properties of a single Parent class.

class A:
    category ="message"

class B(A):
    pass
b=B()
print(b.category) #Message

#Multilevel Inheritance
#In this inheritance, a child class inherits a parent class and this child class is again inherited to
#another child class

class A:
    message ="hello world"

class B(A):
    message = "i'm learning Python"

class C(B):
    pass

c=C()
print(c.message) #i'm learning Python

#Multiple Inheritance

class A:
    message ="Hello World "

class B:
    message="I'm Learning Python"

class C(A,B): # priority to top-most left to right
    pass
c=C()
print(c.message) #hello world

#Hierarchial Inheritance

class A:
    message="Hello World"

class B(A):
    pass

class C(A):
    pass

b=B()
print(b.message) #HELLO WORLD
C=C()
print(c.message) #Hello world


# Hybrid Inheritance

#This Inheritance is the combination of hierarchial and multiple inheritance

class A:
    message ="Hello World"
class B(A):
    message = "Python is a high level language"
class C(A):
    message = "Im learning python"
class D(B,C):
    pass
class E(D):
    pass

e=E()
print(e.message) # Python is a high level language.

#MRO (Method Resolution Order) defines where to search for the attribute in an inheritance.
print(E.mro())
#If the attribute is not found in any of the classes then it raises "AttributeError"



