#  file=open("data/text.txt",'r')
#
#  #print(file.read())
#
#  for line in file:
#     print(line,end='')
#
#  file.close()
#
#
#
# #Практика 1
# file= open("data.txt",'w')
# print('qw','er','ty','ui','op',sep='\n',file=file)
#
#
# file.close()
#
# file=open('data.txt','a')
# file.write('[]')
# file.close()
#
# with open('data.txt','r',encoding='utf-8') as file:
#  print(file.read())
#
# #Практика 2
# user=input('Введите число: ')
# with open('../data/practic2.txt', 'w', encoding='utf-8') as num:
#  num.write(user)
# with open('../data/practic2.txt', 'r', encoding='utf-8') as num:
#   numbers=list(map(int,num.read().split()))
# average=sum(numbers) / len(numbers)
# average1=max(numbers)
# average2=min(numbers)
# with open('../data/result2.txt', 'w', encoding='utf-8') as num:
#  num.write(f"Числа:{numbers}\n")
#  num.write(f"Среднее число:{average}\n")
#  num.write(f"Максимальное число:{average1}\n")
#  num.write(f"Минимальное число:{average2}")