from ORM import Student,session

s1=Student(1,"jon",30,"MALE")
s2=Student(2,"jane",40,"MALE")
s3=Student(3,"Harry",40,"MALE")

session.add(s1)
session.add(s2)
session.add(s3)
session.commit()
print("Student added succesfully!")
