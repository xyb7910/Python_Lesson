from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from SqlAlchemy.LinkDB.main import engine

Base = declarative_base()


# 定义 Student 表
class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer)

    def __repr__(self):
        return "<Student(name='%s', age='%s')>" % (self.name, self.age)


# 定义 Lesson 表
class Lesson(Base):
    __tablename__ = 'lesson'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(100), nullable=False)
    student_id = Column(Integer, ForeignKey('student.id', ondelete='CASCADE'), nullable=False)

    def __repr__(self):
        return "<Lesson(name='%s', description='%s')>" % (self.name, self.description)


# Base.metadata.create_all(engine)
Base.metadata.drop_all(engine)

# 创建 session 实例
session = sessionmaker(bind=engine)()

# 测试插入数据

# Student 数据
stu1 = Student(name='zmz', age=10)
stu2 = Student(name='ypb', age=18)
stu3 = Student(name='gll', age=20)

# session.add_all([stu1, stu2, stu3])
# session.commit()

# Lesson 数据
l1 = Lesson(name='java', description='this is java', student_id=stu1.id)
l2 = Lesson(name='java', description='this is java', student_id=stu2.id)
l3 = Lesson(name='python', description='this is python', student_id=stu1.id)
# session.add_all([l1, l2, l3])
# session.commit()
