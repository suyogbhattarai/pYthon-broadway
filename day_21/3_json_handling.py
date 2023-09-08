# JSON stands for javascript object Notation
# It is a file format which is mainly used for the communication between two or more entities like:
# communication between web frontend and backend, desktop app and backend etc.
#JSON file has the extension of .json

#Some rules for JSON file

#1.JSON content is the key-value pair




import json

filename="students.json"
students=[
    {"name":"jon","age":30,"address":"KTM"},
    {"name":"jane","age":35,"address":"PKR"}
]

with open(filename,"w") as fp:
    data=json.dumps(students,indent=2)
    fp.write(data)

with open(filename,"r") as fp:
    data=json.loads(fp.read())
    print(data)
print(type(data))

address=data[0]["address"]
print(address)
