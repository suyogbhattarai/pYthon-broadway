#Like any other language python also has its set of keywords.There are around 35 keywords in python.

# Keywords are the reserved words of the language which cannot be used as variables or any identifiers

help("keywords")

#Rules for naming identifiers

#1.  Identifiers are case sensitive i.e A=1 and a=1 ,"A" and "a" are two different identiers
#2.  Identifiers can not be the keywords
#3.  Identifiers can't start with numbers.
#4.  Identifiers can include from A-Z,a-z ,0-9 (but cant start with nums)and underscore(-)
#5.  Cant include special cahracters like (@,!,$ etc.)


####### Python statement #########
#Each line in a program is a python statement
# But sometimes multiple statement can be  written in a same line and also one statement can occur in multiple lines

m1="hello";m2="world"#two statements in one line

print(m1 + m2)
message="hello I'm learning Python." \
    "Python is a great language"#Single statements in two lines
print(message)

########### Indentations in 'python ############

#Indentations in python are very important. They are the part of syntax
#Indentations help to define a block of code in python

a=1
if a<2:
    print("Hello World")

###### Comments in python ########

# hash (#) in python is used as a single line comment
# triple-quote string ("""   """)in python can be used as a multi-line comment.




