from abc import ABC


class Animal(ABC):

    def __init__(self, name, age, type_of_sound):
        self.__name = name
        self.age = age
        self.type_of_sound = type_of_sound

    def get_name(self):
        return self.__name
