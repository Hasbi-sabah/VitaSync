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
from sqlalchemy import create_engine
from os import getenv
from dotenv import load_dotenv
from sqlalchemy.orm import scoped_session, sessionmaker


load_dotenv()


class DB:
    """
    Interacts with the MySQL database.

    Attributes:
    - __engine: Database engine instance
    - __session: Database session instance
    - classes: List of database classes
    """

    __engine = None
    __session = None
    classes = [
        HCW,
        Drug,
        DrugPrescribed,
        Prescription,
        Patient,
        Vital,
        MedInfo,
        Vaccine,
        Procedure,
        Record,
        User,
        Appointment,
    ]

    def __init__(self):
        """
        Initialize a DB object and set up the database engine.

        Reads environment variables for database connection and initializes
        the database engine. If the environment is set to 'test', drops all
        tables in the database.

        Raises:
        - ValueError: If required environment variables are not set
        """
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
        """
        Retrieve all instances of a class from the database.

        Args:
        - cls: Optional, specific class to retrieve instances for

        Returns:
        - List of instances of the specified class or dictionary of all instances
        """
        res = {}
        for c in self.classes:
            if not cls or cls == c:
                query = self.__session.query(c).filter_by(archived=False).all()
                if cls == c:
                    return query
                res[c.__name__] = query
        return res

    def get_by_id(self, cls=None, objId=None):
        """
        Retrieve an instance by ID from the database.

        Args:
        - cls: Optional, specific class to retrieve instance from
        - objId: ID of the instance to retrieve

        Returns:
        - Instance of the specified class with the given ID
        """
        query = None
        for c in self.classes:
            if not cls or cls == c:
                query = (
                    self.__session.query(c).filter_by(id=objId, archived=False).first()
                )
                if query:
                    break
        return query

    def get_by_username(self, username=None):
        """
        Retrieve a user instance by username from the database.

        Args:
        - username: Username of the user to retrieve

        Returns:
        - User instance with the specified username
        """
        return (
            self.__session.query(User)
            .filter_by(username=username, archived=False)
            .first()
        )

    def search(self, cls=None, **kwargs):
        """
        Search for instances in the database based on given criteria.

        Args:
        - cls: Optional, specific class to search within
        - kwargs: Filtering criteria for the search

        Returns:
        - List of instances matching the search criteria
        """
        return self.__session.query(cls).filter_by(**kwargs, archived=False).all()

    def get_profile(self, profileId):
        """
        Retrieve a profile instance (HCW or Patient) from the database.

        Args:
        - profileId: ID of the profile to retrieve

        Returns:
        - HCW or Patient instance with the specified ID
        """
        hcw = self.__session.query(HCW).filter_by(id=profileId, archived=False).first()
        patient = (
            self.__session.query(Patient)
            .filter_by(id=profileId, archived=False)
            .first()
        )
        return hcw if hcw else patient

    def drug_lookup(self, name):
        """
        Perform a drug lookup based on the drug name.

        Args:
        - name: Name of the drug or a part of the name to search for

        Returns:
        - Query result for drugs matching the search criteria
        """
        return (
            self.__session.query(Drug)
            .filter_by(archived=False)
            .filter(Drug.commercialName.like(f"%{name}%"))
        )

    def appt_lookup(self, start_time, end_time, **id):
        """
        Perform an appointment lookup based on time range and optional ID.

        Args:
        - start_time: Start time of the range (epoch time)
        - end_time: End time of the range (epoch time
        - end_time: End time of the range (epoch time)
        - id: Optional, additional ID filtering criteria

        Returns:
        - Query result for appointments matching the time range and criteria
        """
        start_time = 0 if not start_time else start_time
        end_time = 2147483647 if not end_time else end_time
        if id:
            return (
                self.__session.query(Appointment)
                .filter_by(**id, archived=False)
                .filter(Appointment.time.between(start_time, end_time))
                .all()
            )
        else:
            return (
                self.__session.query(Appointment)
                .filter_by(archived=False)
                .filter(Appointment.time.between(start_time, end_time))
                .all()
            )

    def new(self, obj):
        """
        Add a new object to the current database session.

        Args:
        - obj: Object to be added to the database
        """
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session."""
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
