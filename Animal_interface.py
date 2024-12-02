from abc import ABC, abstractmethod


class Soundable(ABC):

    @abstractmethod
    def make_sound(self):
        pass
