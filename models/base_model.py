#!/usr/bin/python3
"""BaseModel module for AirBnB Clone project.
This model is used to define the superclass base model
"""

from uuid import uuid4
from datetime import datetime


class BaseModel:

    """BaseModel class for AirBnB Clone
    id: string - assign with an when an instance is created
    created_at: original datetime
    updated_at: last modification datetime
    save(self): updates updated_at with the current datetime
    to_dict(self): returns a dictionary containing all keys/values of __dict__
    __str__: should print: [<class name>] (<self.id>) <self.__dict__>
    """
    def __init__(self, *args, **kwargs):

        if kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            for key, v in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == '__class__':
                    v = self.__class__
                else:
                    setattr(self, key, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):

        nt = self.__dict__.copy()
        nt['created_at'] = self.created_at.isoformat()
        nt['updated_at'] = self.updated_at.isoformat()
        nt['__class__'] = self.__class__.__name__

        return nt
