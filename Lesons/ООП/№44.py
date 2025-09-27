class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age >= 0:
            self.__age = age

    def info(self):
        print(f"Имя: {self.__name}, Возраст: {self.__age}")

    def make_sound(self):
        return "..."


class Lion(Animal):
    def make_sound(self):
        return "Rrrr"


class Elephant(Animal):
    def make_sound(self):
        return "Tuuu"


class Monkey(Animal):
    def make_sound(self):
        return "Ua-Ua"




