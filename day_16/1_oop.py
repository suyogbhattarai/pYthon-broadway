# What will we study in oop?
# Class Attribute and Instance Attribute
# Pillars of OOP
# => Inheritance, Polymorphism, Encapsulation, Abstraction
# Types of Inheritance
# Function / Method Overloading, Operator Overloading, Method Overriding
# Private, Public and Protected Members
# Abstract Classes
# Magic-Methods

#OOP is an approach of programming  in which programs are modelled in the real world problems
#oop stands for object-oriented programming
#class is the blueprint of an object .It has its own attributes known as properties  and methods
#objects are the instance of a class.

#There are four major  pillars of oop :-

#1.inheritance
#2.Encapsulatio
#3.Polymorphism
#4.Abstraction

#Making a class using "class" keyword
class VehicleInformation:
    engine_type="petrol" #class attributes


    #__init__() function inside a class is called when the object of the class is created.so,this
    #function is also called as a constructor.
    def __init__(self,number_of_doors,color):
        self.number_of_doors=number_of_doors # instance attribute
        self.color=color #instance attribute

v1=VehicleInformation(4,"green") #Creating an object/ instantiating an object
print(v1.engine_type) #objects can access the property and methods of the class using dot(.)
print(v1.color)
print(v1.number_of_doors)
print(VehicleInformation.color) #it raises attribute error because color is not a class attribute it is an
#instance attribute

#We can also access the class attribute using the class.
print(VehicleInformation.engine_type) #petrol.THIS IS TERMED AS "GETTING"


v1.engine_type="diesel"#THIS IS TERMED AS "SETTING"
print(VehicleInformation.engine_type) #PETROL
print(v1.engine_type)#diesel



