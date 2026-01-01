# a =4
# b=2
# print(bool(a/b))

# age = int(input("Введите ваш возраст:"))
# if age==14:
#     print('Вы узбек😕...')
# else:
#     print("Ваш возраст:",age)

# num=int(input('Введите число:'))
# if num<5:
#     num-=5
# else:
#     num+=12.5
# print(num)


# my_name=input("Ваше имя:")
# age=2025-int(input("Ваш год рождения:"))
# print(type(my_name),type(age))
# print("Hello my name is:"+my_name,"My age:",age)

print(127%60)

num=int(input('Прошло минут:'))
time1=num//60
time2=num-time1*60
if time1<10 and time2>10:
    print("0"+str(time1)+':'+str(time2))

elif time1<10 and time2<10:
    print("0"+str(time1)+':'+"0"+str(time2))

elif time1>10 and time2>10:
    print(str(time1)+':'+str(time2))
else:
    print(str(time1)+':'+"0"+str(time2))



















