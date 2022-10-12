#!/usr/bin/python3
"""
File Storage
"""
from json import json
from models.base_model import BaseModel


class FileStorage(BaseModel):
    """
    File storage WIP
    """
    def __init__(self):
        """"
        Init File Storage
        """
        __file_path = "engine/file.json"
        __objects = {}
    
    def all(self):
        return self.__objects #IDK

    def new(self, obj):
        dic = {}
        k = f"{self.obj.__class__.__name__}.{obj.id}"
        obj_dict = obj.to_dict()
        self.__objects[k] = obj_dict
        

    def save(self):
        """
        Function that writes an object to text file,
        using a JSON representation.
        """
        with open(self.__file_path, 'w') as f:
            json.dump(self.__objects, f)

    def reload(self):
        """Reloading"""
        try:
            with open(self.__file_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            pass
