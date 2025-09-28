class A:
    def __init__(self, age, name):
        self.age = age
        self.name = name
    def add(self,x, y):
        return x + y
a = A(15, 'Yerlan')
print(A.add(a, 1, 3))
print(a.add(1, 3))

    
