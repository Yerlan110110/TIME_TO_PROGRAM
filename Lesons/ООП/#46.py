class Product:
    def __init__(self, name, price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_info(self):
        return self.name, self.price

    def buy(self, quantity):
        try:
            if self.quantity >= quantity:
                self.quantity -= quantity
                return self.quantity
            else:
                raise ValueError("don't have a product ")
        except ValueError:
            print('Вы заказали больше чем есть')


class Electronic(Product):
    def __init__(self, name, price, quantity, guaranty):
        Product.__init__(self, name, price, quantity)
        self.guaranty = guaranty

    def get_info(self):
        return self.name, self.price, self.quantity, self.guaranty

class Smartphone(Electronic):
    def __init__(self, name, price, quantity, guarantee,ram, storage):
        Electronic.__init__(self, name, price, quantity, guarantee)
        self.ram = ram
        self.storage = storage
    def get_info(self):
        return self.name, self.price, self.quantity, self.guaranty, self.ram, self.storage


class Laptop(Electronic):
    def __init__(self, name, price, quantity, guarantee, gpu):
        Electronic.__init__(self, name, price, quantity, guarantee)
        self.gpu = gpu
    def get_info(self):
        return self.name, self.price, self.quantity, self.guaranty, self.gpu



s = Smartphone('Android',25_000,5,2,16,128)
a = Laptop('Asus',200_000,12,5,4)
d = Smartphone('Iphone',25_000,12,5,4,128)

l = [a,s,d]
for i in l:
    print(i.get_info())









        


