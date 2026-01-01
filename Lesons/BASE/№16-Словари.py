# sl = {
#     'машина':'car',
#     'Телефон': 'Phone',
#      'Ручка': 'pen',
#      'Платье': 'dress',
#      'Сильный': 'great',
#      'но': 'but',
#      'Сколько': 'how',
#      'Под': 'under',
#      'При': 'by',
#      'Заец': 'rabit',
# }
# for i in sl.keys():
#     if len(i) > 5:
#         print(sl[i])
l = input('Введите слово:')
sl ={}

for i in l:
    if i in sl:
     sl[i] += 1
    else:
     sl[i] = 1
print(sl)













# i = 0
# while i < 5:
#     word = input('Введите слово: ')
#     translation = input('Введите перевод: ')
#     sl[word] = translation
#     i +=1
# print(sl)