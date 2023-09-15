#ORM stands for  object relational  Mapping.
# It is an interface provided by the language to query the database using object rather than a raw query.
#There are different packages in different languages to support ORM.
#FOR python 'sqlalchemy' is a famous tool for ORM (pip install sqlalchemy)
from sqlalchemy import create_engine,Column,String,Integer,CHAR
from sqlalchemy.orm import sessionmaker, declarative_base
Base=declarative_base()


#Here class student is the table modeling

class Student(Base):
    __tablename__="Student"
    id =Column ('id',Integer,primary_key=True)
    name=Column("name",String)
    age=Column('age',Integer)
    gender=Column('gender',CHAR)

    def __init__(self,id,name,age,gender):
        self.id=id
        self.name =name
        self.age = age
        self.gender = gender

    def __str__(self):
        return self.name

engine=create_engine("sqlite:///mydb.db",echo=True)
Base.metadata.create_all(bind=engine)
session=sessionmaker(bind=engine)
session=session()
print("Database created succesfully!")



