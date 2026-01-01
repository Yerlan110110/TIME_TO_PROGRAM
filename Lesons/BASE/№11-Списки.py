# s=int(input("Введите строку:"))
# t=[d**2 for d in range(2,s+1,2) if d%5==0]
# print(t)


s=int(input("Введите строку:"))
s_str=str(s).zfill(6)

num=[int(d) for d in s_str]
if num[0]+num[1]+num[2]==num[3]+num[4]+num[5]:
    print('Билет счасливый')
else:
    print('Билет не счасливый')