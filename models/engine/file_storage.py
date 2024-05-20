#!/usr/bin/python3
"""class that serializes instances to a JSON file and
deserializes JSON file to instances"""


import json


class FileStorage:
    """Defining storage class"""
    classes = {"BaseModel": "BaseModel"}
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        keys = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[keys] = obj

    def save(self):

        dict_obj = {}

        for key, value in self.__objects.items():
            dict_obj[key] = value.to_dict()
            with open("file.json", "w", encoding="utf-8") as jsonFile:
                json.dump(dict_obj, jsonFile)

    def reload(self):
        try:
            with open("jsonFile", "r", encoding="utf-8") as jsonload:
                deserialize = json.load(jsonload)
                for key, value in deserialize.items():
                    class_name = v['__class__']
                    if class_name in self.classes:
                        instance = self.classes[class_name](**value)
                        self.__objects[key] = instance
        except FileNotFoundError:
            pass
