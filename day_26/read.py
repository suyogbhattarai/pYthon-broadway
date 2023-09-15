from ORM import session,Student

#READING ALL DATA AT ONCE
results=session.query(Student).all() #orm
print(results)
s2=results[1]
print(s2.name)

for student in results:
    print(student.name)
    print(student.age)

filtered_student =session.query(Student).filter(Student.id==3) #[obj3]
for student in filtered_student:
    print(student.name)