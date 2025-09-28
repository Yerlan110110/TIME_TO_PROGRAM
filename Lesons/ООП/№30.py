#class Person:
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age
#a = Person('Jon',350)
#b = Person('Lololowka',1e6)
#print(a.__dict__)
#print(b.__dict__)

class Tringle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def isosceles(self):
        if self.a ==self.b or self.a ==self.c or self.b == self.c:
            print('равнобедренные')
        else:
            print('не равнобедренные')
t = Tringle(3,2,1)
t.isosceles()
            

