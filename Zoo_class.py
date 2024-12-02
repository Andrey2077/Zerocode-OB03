from ZooKeeper_class import Zookeeper


class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_employee(self, name, is_zookeper, is_veterinarian):

        if is_zookeper == is_veterinarian:
            print("Ошибка ввода сотрудника")
            return

        if is_zookeper:
            self.employees.append(Zookeeper(name))
        elif is_veterinarian:
            self.employees.append(Zookeeper(name))
        else:
            print("Ошибка ввода")

    def add_animal(self, animal):
        self.animals.append(animal)