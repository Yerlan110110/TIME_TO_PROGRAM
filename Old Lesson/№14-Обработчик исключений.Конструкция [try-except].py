# x=0
#
# while x==0:
#     try:
#         x = int(input("Введите число:"))
#         x = 5/x
#         print(x)
#     except ZeroDivisionError:
#         print("На ноль делить нельзя!")
#     except ValueError:
#         print("Лучше введите число!")



#Практика 1
result=0
while result==0:
 try:
    num=int(input("Введите первое число:"))
    num1=int(input("Введите второе число:"))

    result=num/num1
    print(f"Результат:{result}")
 except ZeroDivisionError:
    print("Деление на ноль!")
 except ValueError:
    print("Вы ввели строку!")
 finally:
  print("Программа завершена!")