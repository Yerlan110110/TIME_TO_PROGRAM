class Animal:
    def __init__(self, name, age , health):
        self.__name = name
        self.__age = age
        self.__health = health

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age > 0:
            self.__age = age
        else:
            raise ValueError('age must be positive')

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, health):
        if 100 > health > 0:
            self.__health = health
        else:
            print('Не пизди')

    def info(self):
        print('Name:', self.__name)
        print('Age:', self.__age)
        print('Health:', self.__health)


class Feedable:
    def eat(self, food):
        print('I eat ' + food)

    def make_sound(self):
        pass


class Lion(Animal,Feedable):
    def __init__(self, name, age , health):
        super().__init__(name, age , health)

    def make_sound(self):
        print('Rrrrr')

    def hunt(self):
        print('Atack')

    def eat(self, food):
        if food == 'meat':
            super().eat(food)
        else:
            raise ValueError('I don"t eat this food')


class Elephant(Animal):
    def __init__(self, name, age , health):
        super().__init__(name, age , health)

    def make_sound(self):
        print('Uuuuu')

    def spray_water(self):
        print('Water')

    def eat(self, food):
        if food == 'grass':
            print("I eat grass")
        else:
            raise ValueError('I don"t eat this food')




class Parrot(Animal):
    def __init__(self, name, age , health):
        super().__init__(name, age , health)

    def make_sound(self):
        print('khrkhr')

    def talk(self):
        print('I can talk')

    def eat(self, food):
        if food == 'seeds':
            print("I eat meat")
        else:
            raise ValueError('I don"t eat this food')


class Employee:
    def __init__(self, name, position):
        self.__name = name
        self.__position = position

    @property
    def name(self):
        return self.__name

    @property
    def position(self):
        return self.__position

    def work(self):
        pass

class Zookeeper(Employee):
    def work(self):
        print(f"{self.name} кормит животных.")

class Veterinarian(Employee):
    def work(self):
        print(f"{self.name} лечит животных и повышает их здоровье.")

class Guide(Employee):
    def work(self):
        print(f"{self.name} проводит экскурсию по зоопарку.")


class Zoo:
    def __init__(self):
        self.__animals = []
        self.__employees = []

    @property
    def animals(self):
        return self.__animals

    @animals.setter
    def animals(self, animals):
        if isinstance(animals, list):
            self.__animals = animals
        else:
            raise ValueError("animals должно быть списком")

    @property
    def employees(self):
        return self.__employees

    @employees.setter
    def employees(self, employees):
        if isinstance(employees, list):
            self.__employees = employees
        else:
            raise ValueError("employees должно быть списком")
    def add_animal(self, animal):
        self.animals.append(animal)

    def add_employee(self, employee):
        self.employees.append(employee)

    def daily_routine(self):
        for animal in self.animals:
            animal.make_sound()
            try:
                animal.eat('meat')
            except ValueError as v:
                print('Неподходящий корм')

        for employee in self.employees:
            employee.work()

    @staticmethod
    def rules():
        print("Правила для посетителей зоопарка:")
        print("1. Не кормить животных!")
        print("2. Не кричать и не стучать по клеткам!")
        print("3. Беречь природу и соблюдать чистоту!")
    def save_to_file(self):
        with open('animals.txt','w',encoding='utf-8') as f:
            a = []
            for animal in self.animals:
                f.write(f"{animal.__class__.__name__},{animal.name},{animal.age},{animal.health}\n")
    def load_from_file(self):
        self.animals = []
        with open("animals.txt", "r", encoding="utf-8") as f:
            for line in f:
                cls_name, name, age, health = line.strip().split(",")
                age = int(age)
                health = int(health)

                # создаём объект по имени класса
                cls = globals().get(cls_name)  # достаём класс по имени
                if cls:  # если класс найден
                    self.add_animal(cls(name, age, health))  # создаём объект





l = Lion('a', 2, 3)
l.eat('meat')
print(Zoo.animals)
Zoo.animals = 12
print(Zoo.animals)
print(isinstance(12, list))













