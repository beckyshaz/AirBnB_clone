#!/usr/bin/python3
"""class that defines all common attributes/methods for other classes
called basemodel"""


import uuid
from datetime import datetime


class BaseModel:
    """The base class to inherit from """
    def __init__(self, *args, **kwargs):
        """Initializing the instance attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, val in kwargs.items():
                if key == "__class__":
                    del[key]
                elif key == "created_at" or key == "updated_at":
                    datetime_obj = datetime.strptime(
                        val, "%Y-%m-%dT%H:%M:%S.%f"
                    )
                    setattr(self, key, datetime_obj)
                else:
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

            storage.new(self)

    def __str__(self):
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        from models import storage

        self.updated_at = datetime.now()
        storage.save()


    def to_dict(self):
        dict_objct = self.__dict__.copy()
        dict_objct['__class__'] = self.__class__.__name__
        dict_objct['created_at'] = self.created_at.isoformat()
        dict_objct['updated_at'] = self.updated_at.isoformat()
        return dict_objct
