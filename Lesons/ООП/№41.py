class A:
    def __init__(self, y):
        self.x = 1
        self.y = y


b = A(3)
print(b.__dict__)
