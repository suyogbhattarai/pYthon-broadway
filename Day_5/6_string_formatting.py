#String formatting in python can be done with three methods.

#1.f-strings
#2.format specifier
#3. .format() method

#f-strings

name="jon"
message=f"Hello i'm {name}"
print(message) #Hello i'm jon

#.format() method

name="Jane"
language="Python"
message="Hello i'm {}.I'm learning {}".format(name,language)
print(message)

#format specifier

name="jane"
language="python"
age=21
message="Hello i'm %s.I'm learning %s.I'm %d year old" %(name,language,age)
print(message)