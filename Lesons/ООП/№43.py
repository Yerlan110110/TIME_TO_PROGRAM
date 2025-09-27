class Person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def info(self):
        print(self.__name, self.__age)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,age):
        if age >= 0:
            self.__age=age


class Student(Person):
    def __init__(self,name, age, grade):
        super().__init__(name,age)
        self.__grade = grade
    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self,grade):
        if grade >= 0:
            self.__grade=grade
        else:
            print('Число меньше нуля')

    def info(self):
        super().info()
        print('Оценка:',self.__grade)

p = Person('Yerlan',15)
s = Student('Yerlan', 15, 5)
p.age = -5
s.grade = -5
s.info()




