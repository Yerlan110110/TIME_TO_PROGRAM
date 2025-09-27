#Практика_1
num1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
num2=[]
for i in num1:
  num2.append(i ** 2)
print(tuple(sorted(num2,reverse=True)))
#Практика_2
letters = (['a','b'],['c','d'],['e','f'],['g','h'])
for i in range(4):
    letters[i].insert(0,"!")
print(letters)
#Практика_3
num1=tuple(sorted(map(int,input(f"Введите число:").split(","))))
print(num1+tuple(reversed(num1)))