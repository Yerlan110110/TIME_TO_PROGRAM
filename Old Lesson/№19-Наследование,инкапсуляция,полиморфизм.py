class Bulding:
    year=None
    city=None

    def __init__(self,year,city):
        self.year=year
        self.city=city

    def get_info(self):
        print("Year:",self.year,"City:",self.city)

#Наследование
class School(Bulding):
     pupils=0

     def __init__(self,pupils,year,city):
         super(School,self).__init__(year,city)
         self.pupils=pupils
     #Полиморфизм
     def get_info(self):
         super().get_info()
         print("Pupils:",self.pupils)

class House(Bulding):
     pass

class Shop(Bulding):
     pass
school=School(100,2000,"Moscow")
#Инкапсуляция?,не неслышал
school.year=5
school.get_info()
house=House(2000,"Moscow")
shop=Shop(2000,"Moscow")
