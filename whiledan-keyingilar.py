# ################################  dars - 17  ###############################

# savol = "yaxshi ko'rgan kitobingizni kiriting"
# savol+="(dastur to'xtashi uchun 'stop' deb kiriting)"
#
# while True:
#     qiymat = input(savol)
#     if qiymat =='stop':
#         break
# print("rahmat".title())


# savol = "Yoshingizni kiriting! "
# savol+="('exit' yoki 'quit' deb kiritsangiz dastur to'xtaydi!)"
# qiymat = ''
# while qiymat!='exit' or qiymat!='quit':
#     qiymat = input(savol)
#     if qiymat!='exit' and qiymat!='quit':
#         yosh = qiymat
#         if int(yosh) >65:
#             narx = 0
#         elif int(yosh)>=18:
#             narx = 10000
#         elif int(yosh) >=7:
#             narx = 3000
#         else:
#             narx = 2000
#
#         if narx==0:
#             print("Sizga bepul")
#         else:
#             print(f"Sizga {narx} so'm")
#     else:
#         print("Rahmat!")
#         break


# savol = "Yoshingizni kiriting! "
# savol+="('exit' yoki 'quit' deb kiritsangiz dastur to'xtaydi!)"
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat!='exit' and qiymat!='quit':
#         yosh = qiymat
#         if int(yosh) >65:
#             narx = 0
#         elif int(yosh)>=18:
#             narx = 10000
#         elif int(yosh) >=7:
#             narx = 3000
#         else:
#             narx = 2000
#
#         if narx==0:
#             print("Sizga bepul")
#         else:
#             print(f"Sizga {narx} so'm")
#     else:
#         ishora = False
#         print("Rahmat!")

# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
#
# while True:
#     qiymat = input(savol)
#     if qiymat=='exit':
#         break
#     elif float(qiymat)<0:
#         continue
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")

# ####################################   dars - 18   ###########################

# buyurtmalar = []
# n=1
# while True:
#     buyurtma = input(f"{n}-buyurtmani kiriting: ")
#     buyurtmalar.append(buyurtma)
#     javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     if javob=='ha':
#         n+=1
#     else:
#         break
#
# print("siz kiritgan buyurtmalar:")
# for i in buyurtmalar:
#     print(i.title())

# print("Mahsulot va uning narxi lug'atini shakllantiruvchi dastur.")
#
# mahsulotlar = {}
# ishora = True
# while ishora:
#     mahsulot = input("Mahsulot nomini kiriting: ")
#     narx = input(f"{mahsulot} ning narxini kiriting: ")
#     mahsulotlar[mahsulot] = narx
#
#     javob = input("Yana qo'shasizmi? (ha/yo'q)")
#     if javob =="yo'q":
#         ishora = False
# for i,j in mahsulotlar.items():
#     print(f"{i} ning narxi {j} so'm")

#
# buyurtmalar = ['olma','anjir','uzum','qovun']
# mahsulotlar = {
#     'olma':20000,
#     'shaftoli':25000,
#     'tarvuz':18000,
#     'uzum':22000
# }
#
# while buyurtmalar:
#     buyurtma = buyurtmalar.pop()
#     if buyurtma in mahsulotlar.keys():
#         narx = mahsulotlar[buyurtma]
#         print(f"{buyurtma} ning narxi {narx} so'm")
#     else:
#         print(f"Bizda {buyurtma} yo'q")

# ###########################    dars  - 19  #################################

# def t_yil(ism, yosh):
#     """"ismingizni va yoshingizni kiritsangiz sizga tug'ilgan yilingizni
#     ismingiz bilan birga chiqarib beruvchi funksiya"""
#     print(f"{ism.title()} ning tug'ilgan yili {2023-yosh}")
# t_yil("aloshukur", 24)

# def kv_kub(a):
#     """"Foydalanuvchidan son olib uni kubini va kvadratini topuvchi funksiya"""
#     print(f"{a} ning kvadrati: {a*a} \n{a} ning kubi: {a*a*a}")
# kv_kub(25)

# def juftmi(a):
#     """"Juft yoki toqlikka tekshiruvchi funksiya"""
#     if a%2==0:
#         print(f"{a} - juft")
#     else:
#         print(f"{a} - toq")
#
# juftmi(25)

# def taqqosla(a,b):
#     """"foydalanuvchidan ikkita son olib kattasini konsolga chiqaruvchi dastur"""
#     if a>b:
#         print(f"{a} > {b}")
#     elif a<b:
#         print(f"{a} < {b}")
#     else:
#         print(f"{a} = {b}")
# taqqosla(25,55)


# def daraja_hisibla(x, y=2):
#     """"x ning y darajaga ko'taruvchi funksiya"""
#     print(x**y)
# daraja_hisibla(25,3)

# def bulinadimi(a):
#     """"Foydalanuvchidan son olib 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya"""
#     for i in range(2,11):
#         if a%i==0:
#             print(f"{a} soni {i} ga qoldiqsiz bo'linadi")
# bulinadimi(70)

# def info(ism, familya, t_yil, t_joy, email='', tel=''):
#     """"Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email
#     manzili va telefon raqamini qabul qilib, lug'at ko'rinishida qaytaruvchi funksiya"""
#     mijoz ={
#         "ism":ism,
#         "familya":familya,
#         "t_yil":t_yil,
#         "t_joy":t_joy,
#         'email':email,
#         "tel":tel
#     }
#     return  mijoz
#
# print("Mijoz haqida ma'lumotlarni kiriting")
# mijozlar = []
# while True:
#     ism = input("Ismi: ")
#     familya = input("Familyasi: ")
#     t_yil = input("Tug'ilgan yili: ")
#     t_joy = input("Tug'ilgan joyi: ")
#     email = input("Emaili: ")
#     tel = input("Tel raqami: ")
#     mijozlar.append(info(ism, familya, t_yil, t_joy, email, tel))
#     javob = input("Davom etasizmi (yes/no)")
#     if javob!='yes':
#         break
# print("Mijozlar:")
# for mijoz in mijozlar:
#     print(f"{mijoz['ism'].title()} {mijoz['familya'].title()} {mijoz['t_yil']} - yilda {mijoz['t_joy'].title()}da tavallud topgan.\n"
#           f"Tel raqami: {mijoz['tel']}, Emaili kerar bo'lsa: {mijoz['email']}")
#

# def engkatta(a,b,c):
#     """"uchta sondan  eng kattasini chiqarib beruvchi funksiya"""
#     return  max([a,b,c])
# print(engkatta(12,25,5465))

# def info(r):
#         """"Foydalanuvchidan aylaning radiusini qabul qilib olib,
#         uning radiusini, diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya"""
#         aylana={
#             "diametr":2*r,
#             "perimetri":2*3.14*r,
#             "yuzasi":3.14*r*r
#         }
#         return aylana
# print(info(25))

# def tubsonlar(a,b):
#     """"Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya"""
#     sonlar = []
#     for i in range(a,b):
#         f=0
#         for j in range(2,i):
#             if i%j==0:
#                 f=1
#                 break
#         if f==0:
#             sonlar.append(i)
#     return sonlar
# print(tubsonlar(2,25))
#
# print(list(range(2,3)))

# def fibonachi(n):
#     sonlar = []
#     a=0
#     b=1
#     for i in range(2,n):
#         c=a+b
#         a=b
#         b=c
#         sonlar.append(c)
#     return sonlar
#
# print(fibonachi(25))

################################  dars  -  21   ############################

# def bahola(ismlar):
#     baholar = {}
#     for ism in ismlar:
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#         baholar[ism]=baho
#     return baholar
#
# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar)
# print(baholar)

# def katta_harf(ismlar):
#     katta = []
#     for ism in ismlar:
#         katta.append(ism.title())
#     return katta
#
# talabalar = ['ali', 'vali', 'hasan', 'husan']
# print(katta_harf(talabalar))
# print(talabalar)

#############################  dars -  22  ####################################

# def summa(*sonlar):
#     """"Kiritilgan sonlar yig'indisini hisoblovchi funksiya"""
#     yigindi = 0
#     for son in sonlar:
#         yigindi +=son
#     return yigindi
# print(summa(12,25,36))

# def summa(*sonlar):
#     """Kiritilgan sonlar yig'indisini hisoblovchi funksiya"""
#     return sum(sonlar)
#
# print(summa(12,25,36))


# def summa(x,y, *sonlar):
#     return  x+y+sum(sonlar)
# print(summa(25,15,14,25,14,48,78))

# def avto_info(kompaniya, model, **malumotlar):
#     """Avto haqidagi ma'lumotlarni lug'at ko'rinishdia qaytaruvchi funksiya"""
#     malumotlar['kompaniya'] = kompaniya
#     malumotlar['model'] = model
#     return malumotlar
# avto1 = avto_info("GM", "Lacetti", narx =5000, rang="qizil")
# print(avto1)

# def kopaytma(*sonlar):
#     """"Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya"""
#     multiple = 1
#     for son in sonlar:
#         multiple*=son
#     return multiple
# print(kopaytma(22,15,21)

# def info(ism,familya, **malumotlar):
#     """"Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya"""
#     malumotlar["ism"] = ism
#     malumotlar["familya"] = familya
#     return malumotlar
#
# talaba1 = info("Farruxjon", "Uktamov", t_yil=2000, millati = "o'zbek", malumoti = 'oliy')
# print(talaba1)


###############################  dars - 24  #######################################

# import math
#
# yuza = lambda r: math.pi*r*r
# a=yuza(12)
# print(a)

# yigindi = lambda x,y:x+y
# print(yigindi(12,25))

# darja = lambda a,b:a**b
# print(darja(25,2))

# def daraja(n):
#     return lambda x : x**n
# kvadrat = daraja(2)
# kub = daraja(3)
#
# a=kvadrat(2)
# print(a)

# map funksiyasi

# from math import sqrt
#
# sonlar = list(range(1,11))
# ildizlar = list(map(sqrt, sonlar))
# print(ildizlar)

# sonlar = list(range(1,11))

# def daraja2(x):
#     """"berilgan sonni kvadratini qaytaruvchi dastur"""
#     return x*x
# kvadratlar = list(map(daraja2, sonlar))
#
# print(kvadratlar)

# kvadrat = list(map(lambda x:x*x,sonlar))
# print(kvadrat)

# a=[12,25,15]
# b=[1,2,3]
# a_plus_b = list(map(lambda x,y:x+y, a,b))
#
# print(a_plus_b)

# ismlar = ["anvar", "sobir", "alisher", "jasur"]
# katta = list(map(lambda ism: ism.title(), ismlar))
# print(katta)


# filter funksiyasi

# import random as r
#
# sonlar = r.sample(range(100),10)
#
# def juftmi(x):
#     """"Juft bo'lsa True, Toq bo'lsa False qaytaruvchi dastur"""
#     return x%2==0
#
# juft_sonlar = list(filter(juftmi, sonlar))
# print(juft_sonlar)

# import random as r
# sonlar = r.sample(range(100),10)
#
# juft_sonlar = list(filter(lambda son: son%2==0, sonlar))
# print(f"{sonlar}\n"
#       f"{juft_sonlar}")

mevalar = ["olma", "shaftoli", "o'rik", "uzum", "nok","pomidor", "olcha", "gilos", "tarvuz", "qovun"]
mevalar_o = list(filter(lambda meva:meva.startswith("o"), mevalar))
print(mevalar_o)

mevalar5= list(filter(lambda i:len(i)<=5, mevalar))
print(mevalar5)

mevalar_a = list(filter(lambda x:x.endswith("a"), mevalar))
print(mevalar_a)