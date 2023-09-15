# “Python + is + an + awesome + language”. Split the given string to get a list and join to
# get another string “Python is an awesome language”

string1='''Python + is + an + awesome + language'''
stringlist=string1.split('+')
print(stringlist)
print("".join(stringlist))
# string2=f"{string1[0] + string1[1] +string1[2] + string1[3] + string1[4]}"
# print(string2)