from Employee_class import Employee


class Veterinarian(Employee):


    def heal_animal(animal):
        print(f"Животное {animal.get_name} вылечено")