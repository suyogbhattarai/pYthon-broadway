from estd_connection import estd_connection

cursor= estd_connection()

id=input("Enter student ID")
name=input("student name")
age=int(input("Enter students age"))
address=input("Enter students address")

sql = f"""
INSERT INTO STUDENT(ID,NAME,AGE,ADDRESS) VALUES ('{id}','{name}',{age},'{address}')
"""
cursor.execute(sql)
print("Student added successfully")
