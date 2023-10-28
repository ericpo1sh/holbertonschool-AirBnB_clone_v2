#!/usr/bin/python3
""" module for DBStorage class """
from os import getenv
from models.city import City
from models.user import User
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

classes = {
    'BaseModel': BaseModel,
    'User': User,
    'Place': Place,
    'State': State,
    'City': City,
    'Amenity': Amenity,
    'Review': Review
}


class DBStorage:
    """This class manages storage of hbnb models into database"""
    __engine = None
    __session = None

    def __init__(self):
        """instantiation of DBStorage engine"""
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                getenv("HBNB_MYSQL_USER"),
                getenv("HBNB_MYSQL_PWD"),
                getenv("HBNB_MYSQL_HOST"),
                getenv("HBNB_MYSQL_DB")
            ),
            pool_pre_ping=True
        )
        Base.metadata.create_all(self.__engine)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query all objects - specific to cls var, if supplied"""
        if cls:
            obj_query = list(self.__session.query(cls).all())
        else:
            obj_list = []
            for key, value in classes.items():
                obj_class = self.__session.query(value).all()
                for obj in obj_class:
                    obj_list.append(obj)
        obj_dict = {}
        for obj in obj_query:
            obj_dict[f'{obj.__class__.__name__}.{obj.id}'] = obj
        return obj_dict

    def new(self, obj):
        """adds object to current database session"""
        self.__session.add(obj)

    def save(self):
        """commit changes to current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes obj from current database session, obj argument supplied"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create tables and database session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine,
            expire_on_commit=False
        )
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """close session"""
        self.__session.remove()
