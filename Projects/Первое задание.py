from operator import index

x=['erl','arman','er','marat','qw','ed','rf','g','yh','uj','dk',
   'gh','ng','th','af','h','hy','hg','Array','ahfghgh']
fount=False
for i in x:
    if x.index(i) % 18 == 0:
        for q in i:
            i.title()
            if q == "A" :
                print(f"Восемьнадцатый элемент который начинается на букву А:{i}")
                fount =True
            else:
                break
if fount==0:
 print("Не одного элемента кратный к 18 и начинающего на букву А " )


