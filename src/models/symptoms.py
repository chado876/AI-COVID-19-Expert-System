from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Symptom(Base):
    _tablename_ = "symptom"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    severity = Column(String)
   
