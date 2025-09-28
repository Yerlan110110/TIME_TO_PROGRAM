class A:
    def func():
        pass
A.age = 5
b = A()
print(b.__dict__)
print(A.func())
