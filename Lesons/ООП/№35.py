from math import pi
from pprint import pprint
class Computer:
    age = 1
    price = 3e5
    size : str = 'big'
getattr(Computer, 'sdf', pi)
pprint(Computer.__dict__)
del Computer.age
delattr(Computer, 'price')
