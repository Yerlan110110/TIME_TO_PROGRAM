try:
    with open('uwu.txt','r',encoding='utf-8') as file:
        file.read()
except FileNotFoundError:
    print('Файл не найден')

