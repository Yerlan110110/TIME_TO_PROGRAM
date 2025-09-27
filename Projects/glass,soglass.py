word = input("Введите строку: ")

glass = "АЕЁИОУЫЭЮЯаеёиоуыэюя"
go = 0
so = 0
el=' '
for i in word:
    if i in glass:  # Проверяем, есть ли буква в списке гласных
        go += 1
    elif i in el:
        so-=0

    else:
        so += 1

print("Гласных:",go,"\nСогласных:", so)
