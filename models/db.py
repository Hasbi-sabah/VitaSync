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
from models.user import User
from sqlalchemy import create_engine
from os import getenv
from dotenv import load_dotenv
from sqlalchemy.orm import scoped_session, sessionmaker


load_dotenv()


class DB:
    """interaacts with the MySQL database"""

    __engine = None
    __session = None
    classes = [HCW, Drug, DrugPrescribed, Prescription, Patient, Vital, MedInfo,
               Vaccine, Procedure, Record, User]

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
                query = self.__session.query(c).all()
                if cls == c:
                    return query
                res[c.__name__] = query
        return res
    
    def get_by_id(self, cls=None, objId=None):
        for c in self.classes:
            if not cls or cls == c:
                query = self.__session.query(c).filter_by(id=objId).first()
                if query:
                    break
        return query
    
    def search(self, cls=None, **kwargs):
        return self.__session.query(cls).filter_by(**kwargs).all()
        
    def drug_lookup(self, name):
        return self.__session.query(Drug).filter(Drug.commercialName.like(f'%{name}%'))
    
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
