# #  Task 1
# # mes = input('Введите что-то:')
# # with open('data.txt','w+') as f:
# #     f.write(mes)
# #  Task 2
# #     f.seek(0)
# #      print(*f)
# #     lines = f.readlines()
# #      print('Количество строк:', len(lines))
# #     f.seek(0)
# #     content = f.read()
# # with open('copy.txt','w+') as d:
# #     d.write(content)
# with open('numbers.txt','r') as n:
#     content = n.read()
#     num = content.split()
#     l = [i for i in num if int(i) % 2 == 0]
#     with open('even.txt', 'w') as e:
#         e.writelines(' '.join(l))
with open('grades.txt','r',encoding='utf-8') as f:
    def fun(a,*args):
        s = sum(args)/len(args)
        if s < 3.50:
            with open('bad_students.txt','a',encoding='utf-8') as bad:
                bad.write(f"{a} {s:.2f}\n")
                print()
        else:
            with open('good_students.txt','a',encoding='utf-8') as good:
                good.write(f"{a} {s:.2f}\n")
                print()
    l = f.read()
    p = l.split()
    for i in range(0, len(p), 5):
        name = p[i]
        grades = list(map(int, p[i + 1:i + 5]))
        fun(name, *grades)

