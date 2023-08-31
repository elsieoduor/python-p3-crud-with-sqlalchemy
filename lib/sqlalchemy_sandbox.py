#!/usr/bin/env python3

from datetime import datetime

from sqlalchemy import (create_engine, desc, func,
    CheckConstraint, PrimaryKeyConstraint, UniqueConstraint,
    Index, Column, DateTime, Integer, String)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    __table_args__ = (
        PrimaryKeyConstraint('id', name = 'id_pk'),
        UniqueConstraint('email', name = 'unique_email'),
        CheckConstraint('grade BETWEEN 1 AND 12', name = 'grade_between_1_and_12')
    )
    Index('index_name', 'name')

    id = Column(Integer())
    name = Column(String())
    email = Column(String(55))
    grade = Column(Integer())
    birthday = Column(DateTime())
    enrolled_date = Column(DateTime(), default = datetime.now())

    def __repr__(self):
        return f'Student {self.id}: '\
            +f'{self.name}, '\
            +f'Grade {self.grade}'
if __name__ == '__main__':
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

#For one
    natalie = Student(
        name = "Cypher Natalie",
        email = 'iloveelsie@gmail.com',
        grade = 7,
        birthday = datetime(2003, 11, 24)
    )
    session.add(natalie)
    session.commit()

    #For many
    oduorii = Student(
        name = "Elsie Oduor",
        email = 'ilovecypher@gmail.com',
        grade = 7,
        birthday = datetime(2005, 9, 6)
    )
    sean = Student(
        name = "Sean Omomdi",
        email = 'ilovesonic@gmail.com',
        grade = 1,
        birthday = datetime(2017, 8, 30)
    )
    session.bulk_save_objects([oduorii, sean])
    session.commit()