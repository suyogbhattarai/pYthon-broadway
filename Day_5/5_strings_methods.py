# capitalize()

message="hello world"
result= message.capitalize()
print(result) # Hello world

#title()
result=message.title()
print(result) # "Hello World"

#upper()
result =message.upper()
print(result) #"HELLO WORLD"

# Lower()
result = message.lower()
print(result) # hello world

# split()

message="hello world"
result = message.split()
print(result)#['hello','world']

message="I,am,learning,python"
result= message.split(',')
print(result) #['I','am','learning','python']

message="hello world"
result= message.split('o')
print(result) #['hell','w,'rld']

# join()
data=["hell",' w','rld']
result="o".join(data)
print(result)#hello world

data=["hello","world"]
result="".join(data)
print(result) #"hello world"

#find()

message="hello world"
result=message.find("w")
print(result) # 6

#   If we give the subset not present in the string then find() returns -1

#replace()

message="hello world"
result = message.replace("hello","HELLO")
print(result) #HELLO world

