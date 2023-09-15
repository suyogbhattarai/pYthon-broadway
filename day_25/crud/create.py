

from estd_connection import estd_connection

cursor=estd_connection()

def create_student():

    id=int(input("Enter student id"))
    name=input("Enter student name")
    age=int(input("Enter student age"))
    address=input("Enter student address")

    sql=f"INSERT INTO STUDENT(ID,NAME,AGE,ADDRESS) VALUES({id},'{name}',{age},'{address}')"
    cursor.execute(sql)
    print("Created succesfull with !")






