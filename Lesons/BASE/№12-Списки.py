# stp=['qsqsqs','Qsqsqsqs']
# stp.pop(0)
# print(stp)
#Практика_1
# List=[]
# stp=input("Введите строку:")
# for i in stp:
#      if i not in('a',"e","u"):
#          List.append(i)

# print(List)
#Практика_2
# List=[(int(input(f"Введите {i} цифру:"))) for i in range(1,10)]
# List=[i for i in List if i>5]
# print(List)
#Практика_3
List =[int(input(f"Введите {i}-ую цифру:"))for i in range(1,11)]
List.sort(reverse=True,key=abs)
num = 1
found = False
for i in range(0,10,2):
    if List[i] % 3 == 0:
        num *= List[i]

        found = True

if found:
    print("Произведение элементов, кратных 3 и с чётным индексом:",num)
else:
    print("Нет элементов, кратных 3 и стоящих на чётных индексах.")





