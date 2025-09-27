import pprint
class A:
    x = 12
a = A()
a.y = 10
pprint.pprint(A.__dict__)
setattr(A,'x',5)
print(A.x)