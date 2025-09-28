from pprint import pprint
class A:
    def pl():
        print(1 + 5)
A.pl()
b = A
b.pl()
pprint(A.pl)
pprint(b.pl)
