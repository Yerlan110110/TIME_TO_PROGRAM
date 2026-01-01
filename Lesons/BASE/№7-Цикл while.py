# num=int(input())
# i=-1
# while i<num:
#     i+=1
#     print(i)

# num = int(input("Введите число:"))
# i=0
# c=0
# while num:
#     i=num%10
#     num//=10
#     if i%2==0:
#        c+=1
# print(c)

x = int(input("Введите X:"))
r = int(input("Введите R:"))
i=x
c=0
while i<=r:
    print(i)
    i+=1
    c+=1
print(f"В промежутке от X до R {c} числа")