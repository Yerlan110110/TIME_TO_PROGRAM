class A:
    def h(a):
        print(a.__dict__)
b = A()
b.g = 15
b.h()
