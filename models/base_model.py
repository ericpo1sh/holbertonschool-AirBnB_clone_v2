#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import models
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

    def __str__(self):
        """string representation of BaseModel object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def delete(self):
        """delete current instance from FileStorage"""
        models.storage.delete(self)

    def save(self):
        """updates updated_at attribute with current datetime"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """returns __dict__ keys & values of BaseModel instance"""
        inst_dict = self.__dict__.copy()
        inst_dict.update({
            'created_at': datetime.isoformat(self.created_at),
            'updated_at': datetime.isoformat(self.updated_at),
            '__class__': self.__class__.__name__
        })
        if '_sa_instance_state' in inst_dict:
            del inst_dict['_sa_instance_state']
        return inst_dict
