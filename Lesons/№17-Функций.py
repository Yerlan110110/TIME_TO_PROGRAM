# st  = int(input('Введите радиус:'))
# def fun(a):
#     return 3.14 * a**2
# print(fun(st))


# st  = int(input('Введите число:'))
# def fun(a):
#     even = [int(i) for i in str(a) if int(i) % 2 == 0]
#     print('Чётных цифр в числе:',len(even))
#     print('Сумма чётных цифр:',sum(even))
# fun(st)

st = int(input('Введите число:'))
def fun(a):
     num = 1
     for i in range(1, a+1):
         num *= i
     print(num)
fun(st)