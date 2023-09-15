from ORM import session,Student

session.query(Student).filter(Student.id==3).update({"name":"ken","age":12}) #ORM
session.query(Student).filter(Student.name=="jon").update({"name":"Gita","age":12}) #ORM
session.commit()
print("Student Uploaded Succesfully!")
