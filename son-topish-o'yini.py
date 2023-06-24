import random as r
print("Keling o'ylagan sonni topish o'ynaymiz!")

def son_top(n=10):
    sonlar = list(range(1,n+1))
    x=r.choice(sonlar)
    y = int(input(f"1 dan {n} gacha son o'yladim. Topa olasizmi?\n>>>"))
    urinish_soni = 0
    while True:
        urinish_soni+=1
        if y>x:
            y=int(input("Xato, men o'ylagan son bundan kichikroq. Yana harakat qiling:\n>>>"))
        elif y<x:
            y=int(input("Xato, men o'ylagan son bundan kattaroq. Yana harakat qiling:\n>>>"))
        else:
            y=f"Topdingiz {y} sonini o'ylagan edim. {urinish_soni} ta taxmin bilan topdingiz. Tabriklayman!"
            break
    print(y)
    return urinish_soni

def son_top_pc(n=10):
    input(f"1 dan {n} gacha son o'ylang. Men topishga harakat qilaman. O'ylagan bo'lsangiz istalgan tugmani bosing ")
    quyi = 1
    yuqori = n
    urinish_soni=0
    while True:
        urinish_soni+=1
        if quyi!=yuqori:
            taxmin = r.randint(quyi,yuqori)
        else:
            taxmin = quyi
        javob = input(f"Siz {taxmin} sonini o'yladingiz: to'g'ri(t), katta(+), kichik(-)".lower())

        if javob == '-':
            yuqori = taxmin - 1
        elif javob == '+':
            quyi = taxmin + 1
        else:
            break
    print(f"Men {urinish_soni} ta taxmin bilan topdim!")
    return urinish_soni

def play(n=10):
    taxminlar = son_top(n)
    taxminlar_pc = son_top_pc(n)
    while True:
        if taxminlar>taxminlar_pc:
            print("Yutqazdingiz! Men yutdim")
        elif taxminlar<taxminlar_pc:
            print("Siz yutdingiz!")
        else:
            print("Durrang!")
        yana = int(input("Yana o'ynaysizmi ha(1), yo'q(0)"))
        if yana == 0:
            break
play()








