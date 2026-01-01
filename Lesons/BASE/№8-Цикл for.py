# num=int(input())
# n=0
# for i in range(0,num+1,2):
#     n+=i
# print(n)


# num=int(input())
# for i in range(1,num):
#     if i==7:
#         continue
#     elif i==13:
#         continue
#     elif i==21:
#         continue
#     elif i==29:
#         continue
#     print(i)


num=int(input("Введите число:"))
for i in range(1,num+1):
    if i%2==0:
        i**=2
    else:
        i**=3
    print(i)

