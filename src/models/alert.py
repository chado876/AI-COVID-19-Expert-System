from dataclasses import dataclass
from sqlalchemy import create_engine,Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Boolean, Float

Base = declarative_base()

class Alert(Base):
    __tablename__ = "alerts"
    id = Column(Integer, primary_key=True)
    alert_type = Column(String)
    value = Column(Integer)

engine = create_engine('sqlite:///./data/diagnoses.db', echo=True)
Base.metadata.create_all(bind=engine)

