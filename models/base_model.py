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
        if kwargs and len(kwargs) > 0:
            if 'id' not in kwargs.keys():
                self.id = str(uuid4())
            if '__class__' in kwargs.keys():
                del kwargs['__class__']
            if "created_at" in kwargs.keys() and "updated_at" in kwargs.keys():
                kwargs['created_at'] = datetime.strptime(
                    kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f'
                )
                kwargs['updated_at'] = datetime.strptime(
                    kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f'
                )
            else:
                self.created_at = datetime.now()
                self.updated_at = self.created_at
            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
        # for key, value in kwargs.items():
        #     if not hasattr(self, key):
        #         setattr(self, key, value)

    def __str__(self):
        """string representation of BaseModel object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def delete(self):
        """delete current instance from FileStorage"""
        from models.__init__ import storage
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
