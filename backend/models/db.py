from models.base import Base, BM
from models.hcw import HCW
from models.drug import Drug
from models.drug_prescribed import DrugPrescribed
from models.prescription import Prescription
from models.patient import Patient
from models.vital import Vital
from models.med_info import MedInfo
from models.vaccine import Vaccine
from models.procedure import Procedure
from models.record import Record
from models.appointment import Appointment
from models.user import User
from sqlalchemy import create_engine, or_
from os import getenv
from dotenv import load_dotenv
from sqlalchemy.orm import scoped_session, sessionmaker


load_dotenv()


class DB:
    """interaacts with the MySQL database"""

    __engine = None
    __session = None
    classes = [HCW, Drug, DrugPrescribed, Prescription, Patient, Vital, MedInfo,
               Vaccine, Procedure, Record, User, Appointment]

    def __init__(self):
        """Instantiate a DBStorage object"""
        MYSQL_USER = getenv("MYSQL_USER")
        MYSQL_PWD = getenv("MYSQL_PWD")
        MYSQL_HOST = getenv("MYSQL_HOST")
        MYSQL_DB = getenv("MYSQL_DB")
        ENV = getenv("ENV")
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                MYSQL_USER, MYSQL_PWD, MYSQL_HOST, MYSQL_DB
            )
        )
        if ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def get_all(self, cls=None):
        res = {}
        for c in self.classes:
            if not cls or cls == c:
                query = self.__session.query(c).filter_by(archived=False).all()
                if cls == c:
                    return query
                res[c.__name__] = query
        return res
    
    def get_by_id(self, cls=None, objId=None):
        query = None
        for c in self.classes:
            if not cls or cls == c:
                query = self.__session.query(c).filter_by(id=objId, archived=False).first()
                if query:
                    break
        return query
    
    def get_by_username(self, username=None):
        return self.__session.query(User).filter_by(username=username, archived=False).first()
    
    def search(self, cls=None, **kwargs):
        return self.__session.query(cls).filter_by(**kwargs, archived=False).all()
    
    def get_profile(self, profileId):
        hcw = self.__session.query(HCW).filter_by(id=profileId, archived=False).first()
        patient = self.__session.query(Patient).filter_by(id=profileId, archived=False).first()
        return hcw if hcw else patient
        
    def drug_lookup(self, name):
        return self.__session.query(Drug).filter_by(archived=False).filter(Drug.commercialName.like(f'%{name}%'))
    
    def appt_lookup(self, start_time, end_time, patientId=None):
        start_time = 0 if not start_time else start_time
        end_time = 2147483647 if not end_time else end_time
        if patientId:
            return self.__session.query(Appointment).filter_by(patientId=str(patientId), archived=False).filter(Appointment.time.between(start_time, end_time)).all()
        else:
            return self.__session.query(Appointment).filter_by(archived=False).filter(Appointment.time.between(start_time, end_time)).all()
    
    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)
        self.save()

    def close(self):
        """call remove() method on the private session attribute"""
        Base.metadata.drop_all(self.__engine)
        self.__session.remove()