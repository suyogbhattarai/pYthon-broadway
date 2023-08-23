a=1
print(type(a)) #int
a=(1)
print(type(a))#int
a=(1,)
print(type(a))#tuple

a=1,
print(type(a))#tuple.And this is a tuple packing

a=1,2,3
print(a)#(1,2,3)
a,b,c=1,2,3
print(a) #1
print(b) #2
print(c) #3

a,b,c=(1,2,3)
print(a) #1
print(b) #2
print(c) #3

#POSSIBLE ERRORS IN TUPLE PACKING AND UNPACKING

a,b=1,2,3 #too many value to unpack.
a,b,c=1,2 #not enough values to unpack.




