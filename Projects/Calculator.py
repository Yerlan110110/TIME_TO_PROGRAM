try:
    n = int(input('Введите первое число:'))
    nm = int(input('Введите второе  число:'))
    zn = int(input('Выберите что хотите сделать:\n1.Сложить\t2.Вычтить\t3.умножить\t4.раздеелить\nНапишите что сделаете(Например:1):'))
except ValueError:
    print('Еблан число жаз🖕')
match zn:
    case 1:
        print('Результат:',n +nm)
    case 2:
        print('Результат:',n - nm)
    case 3:
        print('Результат:',n * nm)
    case 4:
        print('Результат:',n / nm)



