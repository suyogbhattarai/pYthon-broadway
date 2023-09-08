#There are some file methods which can be useful in file handling projects.

filename="message.txt"
#read()
with open(filename,"r") as fp:
    data=fp.read(7)
print(data)

#seek()

with open(filename,"r") as fp:
    fp.seek(13)
    data=fp.read()
    fp.seek(0)
    d=fp.read()
print(data)
print(d)

#readline()

with open(filename,"r") as fp:
    data=fp.readline()
    fp.seek(13)
    d=fp.readline()
print(data)
print(d)

#readlines()
with open(filename,"r") as fp:
    data=fp.readlines()
    print(fp.tell()) #tells the current cursor position in the file
print(data) #['Hello World\n', "I'm Learning Python\n", 'Python is a high level language']

data=['Hello World\n', "I'm Learning Python\n", 'Python is a high level language']
with open(filename,"w") as fp:
    fp.writelines(data)



