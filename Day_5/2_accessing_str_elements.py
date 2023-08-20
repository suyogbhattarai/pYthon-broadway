#We can access string elements using indexing and slicing which is similar
# to the list
# Forward indexing starts from 0 and reverse indexing from -1
message="Hello world"

#Indexing
print(message[0])#H
print(message[5])# <space>
print(message[-1])# d
print(message[-8])# l
print(message[20])# Error
print(message[-20])# Error

#Slicing
message="I am learning python"
print(message[:6])#I am l
print(message[0:5])#I am
print(message[3:8])#m lea
print(message[4:])# learning python
print(message[7:2])#''
print(message[-8:-2])#g pyth
print(message[-6:-8])#''
print(message[3:-3])#m learning pyt
print(message[9:-11])#''
print(message[3:8:2])# 'mla'

#Creating the object (empty and non-empty)
#Accesing the elements (Indexing/slicing /accessing elements using key)
#operations
#methods
#built-in functions

# messege="Hello"
# message[2]="L" #It is not possible because string is immutable
# print(message)
#
# del message #del is a keyword that deletes the object



