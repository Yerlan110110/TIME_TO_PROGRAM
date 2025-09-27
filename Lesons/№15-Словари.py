# Практика_1
#sl = {
#     'кот': 'cat',
#     'машина': 'car',
#     'жить': 'live',
#     'ручка': 'pen',
#     'мышь': 'mouse',
#     'чашка': 'cup',
#     'горячий': 'hot',
#     'блокнот': 'notes',
#     'телефон': 'phone',
#     'железо': 'iron',
# }
#
# word = input("Введите слово: ").lower()
# try:
#     print(f'Слово {word} переводится как:',sl[word])
# except KeyError:
#     print(f'Слова "{word}" нет в словаре')
# Практика_2
from random import randint

i = 1
sl = {}

while i < 10:
    key = randint(0, 999)

    if key in sl:
        continue  # если ключ уже есть, пропускаем и пробуем снова

    name = input(f'{i}. Введите имя_фамилия: ')
    sl[key] = name
    i += 1

print(sl)



