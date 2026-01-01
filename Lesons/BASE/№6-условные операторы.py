# num1=int(input("Введие первое число:"))
# num2=int(input("Введие второе число:"))
# num3=int(input("Введие третья число:"))
# if num1<num2<num3:
#     print(num3+num2)
# elif num1<num2>num3:
#     print(num3+num2)
# elif num1>num2<num3:
#     print(num3+num1)
# else:
#     print(num1+num2)
# n=int(input("Текущий год:"))
# v="Вискосный" if n % 4 == 0 and n%100!=0 or n%400==0 else "Не вискосный"
# print(v)

try:
    month=int(input('В каком месяце вы родились?\nОтвет:'))

    match month:
        case 12|1|2:
            print("Вы родились зимой ")
        case 3 | 4 | 5:
            print("Вы родились весной")
        case 6 | 7 | 8:
            print("Вы родились летом")
        case 9 | 10 | 11:
            print("Вы родились осеню")

except ValueError:
     print("Вы родились долбоёбом...")
