#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), nullable=False, primary_key=True, unique=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instantiation of BaseModel object"""
        self.id = kwargs.get('id', str(uuid4()))
        self.created_at = kwargs.get('created_at', datetime.now())
        self.updated_at = kwargs.get('updated_at', self.created_at)
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    self.__dict__[key] = datetime.strptime(
                        value,
                        "%Y-%m-%dT%H:%M:%S.%f"
                    )
                elif key != '__class__':
                    self.__dict__[key] = value

    def __str__(self):
        """string representation of BaseModel object"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def delete(self):
        """delete current instance from FileStorage"""
        from models import storage
        storage.delete(self)

    def save(self):
        """updates updated_at attribute with current datetime"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """returns __dict__ keys & values of BaseModel instance"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({
            '__class__': (str(type(self)).split('.')[-1]).split('\'')[0]
        })
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in dictionary.keys():
            dictionary.pop('_sa_instance_state')
        return dictionary
