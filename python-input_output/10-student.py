#!/usr/bin/python3


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if not attrs:
            return self.__dict__
        result = {}
        for key in self.__dict__:
            if key in attrs:
                result[key] = self.__dict__[key]
        return result
