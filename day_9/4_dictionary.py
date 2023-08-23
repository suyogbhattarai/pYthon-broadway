#Dictionary are the mutable datatypes in Python.
#They are the key-value pairs enclosed within curly braces.

# creating an empty dictionary.
a={}
print(a)
a=dict()
print(a)

#Creating non-empty dictionary
student={"name":"jane","age":30,"address":"KTM"}
print(student)
student=dict(name="jane",age=30,address="KTM")
print(student)

#Accessing elements of a dictionary
#Dictionary elements are accessed using keys
student={"name":"jane","age":30,"address":"KTM"}
name=student["name"]
print(name)

age=student["age"]
print(age) #30

address=student["address"]
print(address)#Ktm

# print(student["roll_no"]) #It raises key error

#Accessing dictionary elements using .get() method

student={"name":"jane","age":30,"address":"KTM"}
name=student.get("name")
print(name)#Jane

roll_no=student.get("roll_no")
print(roll_no)#None




