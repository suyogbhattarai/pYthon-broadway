#True and false are the booleaan  types
#True and false are also the keywords in python

#Operations that give booelean types
a=5
b=10
c=15

#relational operations

print ( b > a) #True
print(b!=a) #True
print(b<a) #False
print(a == c) #False

#Logical Oprerators

print(b>a and a==c)#false
print(b>a or a==c)#true
print(not True)#false
print(not False)#true
print(not a)#False

#Membership Operation

print(2 in [1,2,3])#TRUE
print(3 not in [1,2,3])#False

#Identity operation
a=1
b=1

print (a==b)#TRUE
print(a is b)#TRUE

# IDENTITY
a=1245776888888888888888888888888888888766666666666666666666666666666666666666666666666666662252722572252577527
b=1245776888888888888888888888888888888766666666666666666666666666666666666666666666666666662252722572252577527
print(a is b)

#Concept of truthy and falsy
# Truthy

# all non-empty datatypes and non-zero numbers are trythy values

a=12
b=5.7
c=[1,2]
d=(4,5)
e={1,2}
f={"name":"jon"}
g=True

# All these datatypes are truthy datatypes
# We can check the truthiness of the data using bool function

print(bool(b))  # True


# Falsy
# All empty datatypes and zero are falsy values
a = 0
b = 0.0
c = []
d = ()
e = {}
f = set()
g = False
h = None
print(not a)
print(bool(b))

#PYTHON BOOLEANS ARE THE SUBCLASS OF THE INTEGER CLASS. THAT MEANS TRUE IS 1 AND FALSE IS 0

a=True
b=3
print(a+b)#4
print(70 * False)#0
print(True + True)#2