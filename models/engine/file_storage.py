#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.city import City
from models.user import User
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel

classes = {
    'BaseModel': BaseModel,
    'User': User,
    'Place': Place,
    'State': State,
    'City': City,
    'Amenity': Amenity,
    'Review': Review
}


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls:
            obj_dict = {}
            for key, value in self.__objects.items():
                if cls in classes.values() or cls in classes.keys():
                    if cls == type(value) or classes[cls] == type(value):
                        obj_dict[key] = value
            return obj_dict
        else:
            return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Serialization of __objects to JSON file at __file_path location"""
        obj_dict = {}
        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(self.__file_path, "w") as outfile:
            json.dump(obj_dict, outfile)

    def reload(self):
        """Deserialization to __objects from saved JSON file, if exists"""
        try:
            obj_dict = {}
            with open(FileStorage.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    self.all()[key] = classes[value['__class__']](**value)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes specified object from objects dictionary"""
        if obj:
            for key, value in self.__objects.items():
                if value == obj:
                    del self.__objects[key]
                    return
