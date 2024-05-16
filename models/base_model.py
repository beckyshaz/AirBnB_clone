#!/usr/bin/python3
"""class that defines all common attributes/methods for other classes
called basemodel"""


import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dict_objct = self.__dict__.copy()
        dict_objct['__class__'] = self.__class__.__name__
        dict_objct['created_at'] = self.created_at.isoformat()
        dict_objct['updated_at'] = self.updated_at.isoformat()
        return dict_objct
