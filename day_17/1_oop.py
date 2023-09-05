#Basic Introduction--

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
    def __init__(self,number_of_doors,color): # constructor.Constructor cannot be more than 1 in a class
        self.number_of_doors=number_of_doors # instance attribute
        self.color=color #instance attribute


#A method is a function defined inside the class.Methods are called with the class object.
# They cant be called independently.Here "description" is a method (function defined inside the class)


    def description(self): # a method .Method can be of any numbers in a class.
        return f"The vehicle has {self.number_of_doors} doors and is {self.color} color. It's engine type is"\
                f"self.engine_type"

v1=VehicleInformation(4,"green") #Creating an object/ instantiating an object

print(v1.engine_type) #objects can access the property and methods of the class using dot(.)
print(v1.color)
print(v1.number_of_doors)
print(v1.description())
# print(VehicleInformation.color) #it raises attribute error because color is not a class attribute it is an
#instance attribute

#We can also access the class attribute using the class.
print(VehicleInformation.engine_type) #petrol.THIS IS TERMED AS "GETTING"


v1.engine_type="diesel"#THIS IS TERMED AS "SETTING"
print(VehicleInformation.engine_type) #PETROL
print(v1.engine_type)#diesel


class BikeInformation:
    engine_type="petrol" #class attribute

    def __init__(self,no_of_tyres,color):
        self.no_of_tyres =no_of_tyres #instance attribute
        self.color = color #instance attribute

v2=BikeInformation(2,"black") #Creating an object /intantiating an object
print(v2.engine_type)
print(v2.color)
print(v2.no_of_tyres)

print(BikeInformation.engine_type) #This is known as getting

v2.engine_type="diesel" #This is termed as setting
print(v2.engine_type)
print(BikeInformation.engine_type)



