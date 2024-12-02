from Animal_class import Animal
from Animal_interface import Soundable


class Reptile(Animal, Soundable):

    def __init__(self, name, age, type_of_sound):
        super().__init__(name, age, type_of_sound)

    def make_sound(self):
        print(f"Рептилия: {self.get_name()} {self.type_of_sound}")
