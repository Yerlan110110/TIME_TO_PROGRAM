class Person:
    age = 15
p = Person()
p.name = 'Yerlan'
print(getattr(p, 'name'))
print()
