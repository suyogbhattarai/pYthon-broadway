#We have diffrent methods to add and remove items ina aset

#add()
s={1,2,3}
result=s.add(4) #None
print(result)#{1,2,3,4}

#update()
s.update([4,5,6])
print(s)#{1,2,4,3,6,5}

#discard()
s.discard(4) #discard() takes element as an argument
print(s) #{1,2,3,6,5}

#remove()
s.remove(5)
print(s) #{1,2,3,6}
s.remove(10) #It raises error
