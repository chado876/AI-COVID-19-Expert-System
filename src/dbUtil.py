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
    # diagnosis = Diagnosis()
    # diagnosis.gender = "male"

    diagnoses = session.query(Diagnosis).all()
    for diagnosis in diagnoses:
        print("Diagnosis with id-%s" %diagnosis.id + " and first name - " + diagnosis.first_name)

    session.commit()
    session.close()


# diagnosis = Diagnosis()
# diagnosis.first_name = "Mason"
# diagnosis.last_name = 'Mount'

# add_diagnosis(diagnosis)
# get_diagnoses()

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

# drop_diagnoses()
# get_diagnoses()
# count_total_diagnoses()
# engine = create_engine('sqlite:///./data/diagnoses.db', echo=True)
# Base.metadata.create_all(bind=engine)






			