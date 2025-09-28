import pprint
class Person:
    pass
setattr(Person, 'age', 15)
setattr(Person, 'name', 'Yerlan')
print(getattr(Person, 'age'), getattr(Person, 'name'))
delattr(Person, 'age')
delattr(Person, 'name')
pprint.pprint(Person.__dict__)