import sqlite3
from models.diagnosis import Diagnosis
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# create a default path to connect to and create (if necessary) a database
# called 'database.sqlite3' in the same directory as this script
Base = declarative_base()

def add_diagnosis(diagnosis: Diagnosis):
    engine = create_engine('sqlite:///./data/diagnoses.db', echo=True)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(diagnosis)
    session.commit()
    get_diagnoses()



def get_diagnoses():
    engine = create_engine('sqlite:///./data/diagnoses.db', echo=True)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    diagnoses = session.query(Diagnosis).all()

    for diagnosis in diagnoses:
        print("Diagnosis with id-%s" %diagnosis.id + " and first name - " + diagnosis.first_name + " and result - " + diagnosis.result)
        session.expunge(diagnosis)

    session.commit()
    session.close()
    return diagnoses

def get_column_names():
    col_names = Diagnosis.metadata.tables['diagnosis'].columns.keys()
    print(col_names)
    return col_names


def count_total_diagnoses():
    engine = create_engine('sqlite:///./data/diagnoses.db', echo=True)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    rows = session.query(Diagnosis).count()
    session.commit()
    print("TOTAL DIAGNOSES:: %s" % rows)
    return rows


def drop_diagnoses():
    engine = create_engine('sqlite:///./data/diagnoses.db', echo=True)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Diagnosis).delete()
    session.commit()

def query_db(res):
    engine = create_engine('sqlite:///./data/diagnoses.db', echo=True)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(Diagnosis).filter(Diagnosis.result==res).all()
    for result in results:
        print("QUERY: Diagnosis with id-%s" %result.id + " first name - " + result.first_name + " and result - " + result.result)
        session.expunge(result)
    return results
    

# query_db("Very High Risk")
# drop_diagnoses()
# get_diagnoses()
# count_total_diagnoses()
# engine = create_engine('sqlite:///./data/diagnoses.db', echo=True)
# Base.metadata.create_all(bind=engine)

# get_column_names()






			