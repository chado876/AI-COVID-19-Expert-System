from dataclasses import dataclass
from sqlalchemy import create_engine,Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Boolean, Float

Base = declarative_base()

class Diagnosis(Base):
    __tablename__ = "diagnosis"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    temperature = Column(Float)
    age = Column(Integer)
    symptoms = Column(String)
    total_ulhi = Column(Integer)
    total_serious = Column(Integer)
    total_common = Column(Integer)
    total_less_common = Column(Integer)
    current_fever = Column(Boolean)
    result = Column(String)

engine = create_engine('sqlite:///./data/diagnoses.db', echo=True)
Base.metadata.create_all(bind=engine)

