#!/usr/bin/python3
"""This module defines a class User"""
from os import getenv
from datetime import datetime
from sqlalchemy import Column, DateTime, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        created_at = Column(
            DateTime,
            default=datetime.utcnow(),
            nullable=False
        )
        updated_at = Column(
            DateTime,
            default=datetime.utcnow(),
            nullable=False
        )
        places = relationship(
            "Place",
            cascade="all, delete",
            backref="user"
        )
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
