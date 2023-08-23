#Set is a mutable datatype in python.But,the elements of the set must be immutable.
#Unlike list,set is unordered.so,indexing and slicing is not possible .

#Creating an empty set
s=set()
#s={} #This is not an empty set.It is an empty dictionary

#Creating a non-empty set

s={1,1.1,(1,2),True}
print(s)
s1=set([1,2,3,4,1,2,3,4])
print(s1)

s={1,[1,2],3} #This is invalid set because it has list as an element which is mutable
s={1,2,(1,2,[3,4])}#this is also invalid beacause tutle has a mutable element.