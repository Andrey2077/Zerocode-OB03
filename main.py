from Bird_class import Bird
from Mammal_class import Mammal
from Reptile_class import Reptile
from Zoo_class import Zoo


def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

bird_pigeon = Bird("Голубь Вася", 1, "курлычет")
bird_parrot = Bird("Попугай Попка", 2, "пугает")
mammal_goat = Mammal("Коза Нюрка", 5, "пыхтит")
reptile_crocodile = Reptile("Крокодил Гена", 20, "хрумчит")

list_of_animals = [bird_pigeon, bird_parrot, mammal_goat, reptile_crocodile]
animal_sound(list_of_animals)

zoo = Zoo()
zoo.add_animal(bird_pigeon)
zoo.add_animal(bird_parrot)
zoo.add_animal(mammal_goat)
zoo.add_animal(reptile_crocodile)
zoo.add_employee("Смотритель Ваня", True, False)
zoo.add_employee("Ветеринар Федя", False, True)
print(zoo.employees)

