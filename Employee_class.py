from abc import ABC


class Employee(ABC):

    def __init__(self, name):
        self.name = name
