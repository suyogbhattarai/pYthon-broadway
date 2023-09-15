#We can create a file,update and delete the content of the file using Pyhton language.
#File can be opened in following modes in Python.

#r=read mode
#w=write mode
#a=append mode
#r+ =read and write mode
#w+ =write and read mode
# x= exclusive write mode

filename="message.txt"
fp=open(filename,"w")
fp.write("Hello World")
fp.close()



fp=open(filename,'a')
try:
    fp.write("\nI'm Learning Python")
finally:
    fp.close()

fp=open(filename,"r")
data=fp.read()
print(data)
fp.close()

#Opening the file with the above method can be problematic sometime as we may forget
# to close the file
#so, it is better to open your file using context manager

with open(filename,'r') as fp: #Context manager
    data=fp.read()
print(data)

with open (filename,"r+") as fp:
    data=fp.read()
    fp.write("\nPython is a high level language")
print(data)

with open (filename,"r") as fp:
    data=fp.read()

print(data)

# with open(filename,"w+") as fp:
#     fp.write("I'm Learning python")
#     data=fp.read()
# print(data)






