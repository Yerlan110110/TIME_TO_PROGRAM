# k = input('Введи: ')
# print(list(filter(lambda x: x.isdigit(), k)))
nums = list(map(int, input("Введите 10 чисел через пробел: ").split()))

# Проверка: если пользователь ввел не 10 чисел
if len(nums) != 10:
    print("Ошибка: нужно ввести ровно 10 чисел.")
else:
    result = list(map(lambda x: x * 2 if x % 2 == 0 else x * 3, nums))
    print("Первоначальный список:", nums)
    print("Получившийся список:", result)

