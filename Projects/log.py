import math
num = int(input('1.десятичный логарифм\t'
                '2.двоичный логарифм\t'
                '3.логарифм по произвольному основанию\n'
                'Выберите действие:'))
match num:
    case 1 :
     print(math.log10(int(input('Десятичный логарифм числа:'))))
    case 2 :
     print(math.log2(int(input('Двойчный логарифм числа:'))))
    case 3 :
     print(math.log(int(input('Введите число:')),int(input('По основанию:'))))