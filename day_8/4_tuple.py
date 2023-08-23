#Tuple is an immutable datatype in Python
#Tuple can take different datatypes  regardless they are mutable or immutable

#Indexing and slicing in tuple is same as that of List
#Tuple elements are enclosed with parenthesis. i.e.()


#Creating an empty tuple

t=tuple()
t=()

#Creating non-empty tuple
t=(1,1.1,[1,2,3])
print(t) #(1,1.1,[1,2,3])

#####Accesing tuple Elements #####3
# Tuple elements are accessed using indexing and slicing

vowels=("a","e","i","o","u")
print(vowels[0]) #"a"
print(vowels[4])#"u"
print(vowels[-1])#"u"
print(vowels[-3] )#"i"
print(vowels[20])#"Index error"
data=("a","b","c","d","e","f","g","h","i","j","k","l")
print(data[0:7]) #("a","b","c","d","e","f","g")
print(data[:5])#("a","b","c","d","e")
print(data[:5])
print(data[6:])
print(data[3:8])
print(data[6:2])
print(data[6:-2])
print(data[-8:-3])
print(data[-9:8])
print(data[-3:-7])
print(data[2:8:2])
print(data[-9:-2:])





