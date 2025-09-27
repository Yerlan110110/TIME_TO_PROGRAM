# class Car:
#     wheel = 4
#     def __init__(self, color, mark, speed):
#         self.color = color
#         self.mark = mark
#         self.speed = speed
#
#     def drive(self,place):
#         print(f'Машина цвета: {self.color}, марки: {self.mark}, '
#               f'едет со скоростью {self.speed} в {place}')
# class Firetruck(Car):
#     def __init__(self,color, mark, speed,blinker):
#         self.blinker = blinker
#         super().__init__(color, mark, speed)
#     def pour_water(self):
#         print('Поливаю водой')
#
# ___________________________________
# car1 = Car('cиний','Toyota',300)
# car1.drive('Moskow')
#
# car2 = Firetruck('красный','ЗИЛ',100,True)
# car2.drive('Место вызова')
#___________________________________
# class Cat:
#     breed = 'Sybir'
#     age = 5
# print(getattr(Cat,'breed'),getattr(Cat,'age'))
# special_cat = Cat()
# getattr(special_cat,'paws',4)
#
# class Car:
#     speed : int = 250
#     color : str = 'blue'
# print(Car.speed,Car.color)
# del Car.color
#
# class Black:
#     pass
# print(Black.__dict__)
# black_man = Black
# black_man.x = 'нет'
# delattr(black_man,'x')
# print(black_man.__dict__)
#
# class A:
#     pass
# class B:
#     pass
# a = A
# b = B
# print(isinstance(type(a),type(b)))

# class No:
#     pass
# No.state = 'example'
# print(No.__dict__)
# no = No()


