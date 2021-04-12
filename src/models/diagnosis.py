from dataclasses import dataclass
from sqlalchemy import create_engine,Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Float

Base = declarative_base()

class Diagnosis(Base):
    __tablename__ = "diagnosis"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    temperature = Column(Float)
    age = Column(Integer)
    gender = Column(String)
    symptoms = Column(String)

