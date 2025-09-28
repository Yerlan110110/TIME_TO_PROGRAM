from pprint import pprint
result = []

class Car:
    engine = 1.6
    color = 'black'
    
    
with open("data.txt", "r") as file:
    for i in file:
        if str(Car.engine) in i.split() and Car.color in i.split():
            result.append(i)
pprint(result)    
    
    