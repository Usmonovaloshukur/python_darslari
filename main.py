
# dars - 1

# print(""""Dexia", "Tiko", 'Damas' ko'rganlar qilar havas""")

# print(5**4)
# print(22%4)

# dars - 3

# tomonlari 25 ga teng teng bo'lgan perimetri va yuzi

# print("Yuzasi:", 125**2)
# print("Perimetri:", 4*125)

# Diametri 12 ga teng bo'lgan doiraning yuzini toping  (pi=3.14 deb oling)

# print("Doiraning yuzasi:", 3.14*10**2/4)

# Katetlari 6 va 7 bo'lgan to'g'ri burchakli uchburchakning gipotenuzasini toping
# (Pifagor teoremasidan foydalaning)///


# a=6
# b=7
# c=(a**2+b**2)**(1/2)
# print("Gepotenuza:", c)

# dars - 4

# a= "hello world"
# print(a)

# xabar = "xabar deb nomlangan o'zgaruvchiga biror matn yuklang va konsolga chiqaring," \
#         " keyin esa o'zgaruvchiga yangi qiymat berib uni ham konsolga chiqaring."
#
# xabar = "javohir yaxshi bola emas deb aytsa bu gap to'g'ri bo'lmaydi"
# print(xabar)

# class = "azizbek"
# print(class)

# radus = 5
# pi = 3.14159
# aylana_yuzi = (radus**2)*pi
# print("Radusi", radus, "ga teng aylananing yuzi=", aylana_yuzi)

# dars - 5

# kocha = input("Ko'cha\n")
# mahalla = input("Mahalla\n")
# tuman = input("Tuman\n")
# viloyat = input("Viloyat\n")
# manzil = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
# print(manzil.capitalize())

# dars - 6

# a = int(input("Istalgan son kiriting \n>>>"))
#
# print(f"{a} ning kvadrati {a*a} \n{a} ning kubi esa {a*a*a} ga teng")

# yosh = int(input("Yoshingizni kiriting \n>>>"))
# t_yil = 2023 - yosh
# print(f"siz {t_yil} da tug'ilgansiz")

# son1 = int(input("Birinchi sonni kiirting\n>>>"))
# son2 = int(input("Ikkinchi sonni kiirting\n>>>"))
#
# print(f"{son1} + {son2} = {son1 + son2} \n"
#       f"{son1} - {son2}  = {son1-son2} \n"
#       f"{son1} * {son2} = {son1 * son2} \n"
#       f"{son1} / {son2} = {son1/son2}")

# dars - 7

# ismlar = ["Farrux", 'Javohir', "Azizbek", "Ro'zimurod"]
#
# print(f"Salom {ismlar[0]} oshga boramizmi Kamolonga? \n"
#       f"Salom {ismlar[1]} kechga nima yeymiz? \n"
#       f"Salom {ismlar[2]} tayoq yeysizmi? \n"
#       f"Salom {ismlar[3]} qannoq yaxshimi?")
#
# print(ismlar)

# sonlar = [12, 25.12, -28.125, 32.18, -123]
#
# sonlar.insert(1, 1546)
# print(sonlar)

# t_shaxslar = ["Abu Bakr r.a", "Umar r.a", "Usmon r.a"]
# z_shaxlar = ["Anvar aka", "Elon Mask"]
#
# print(f"Men tarixiy shaxslardan {t_shaxslar.pop(1)} \n"
#       f"Zamonaviy shaxslardan esa {z_shaxlar.pop(0)} bilan suhbat qurgan bo'lar edim")


# friends = []
# friends.append('farrux')
# friends.append('azizbek')
# friends.append('javohir')
# friends.append("ro'zimurod")
# print(friends)
#
# friends.remove('farrux')
# friends.remove("azizbek")
# friends.append("muhammad aka")
# friends.insert(1, "abdulmo'min")
#
# print(friends)
#
# mehmonlar = []
#
# mehmon1 = friends.pop(0)
# mehmonlar.append(mehmon1)
#
# mehmon2 = friends.pop(-1)
# mehmonlar.append(mehmon2)
# print(mehmonlar)


# ####################  dars - 8  ##########################
#
# countries = ["Uzbekistan", "Tadjikistan", "Khazakhistan", "Russia", "Ukraina", "Saudi Arabia"]
# countries.reverse()
#
# print(countries)

# royxat = list(range(120, 1201, 2))
# sum1 = sum(royxat)
# ayirma = max(royxat) - min(royxat)
# print(len(royxat))
# print(sum1)
# print(ayirma)
#
# print(royxat[:20])
# print(royxat[-20:])
# print(royxat[260:281])

# taomlar = ["manti", "kabob", "osh", "jiz", "sho'rva"]
#
# nonushta = taomlar[:]
# nonushta.remove("manti")
# nonushta.remove("kabob")
# nonushta.remove("jiz")
# print(nonushta)

# ############################  dars - 9  #######################

# ismlar = ['farrux', 'javohir', 'azizbek', 'muhammad', 'abdulloh']
#
# for ism in ismlar:
#     print(f"Assalomu alaykum {ism.title()}")
#
# print(f"kod {len(ismlar)} marta takrorlandi")

# sonlar = list(range(11,100,2))
#
# for son in sonlar:
#     print(son**3)
# print(sonlar)

# kinolar = []
# for i in range(5):
#     kinolar.append(input(f"{i+1}- kinoni kiriting \n>>>").title())
#
# print("sizning yoqtirgan kinolaringiz")
# for kino in kinolar:
#     print(kino)


# n = int(input("bugun nechta odam bilan suhbat qurdingiz?\n>>>"))
#
# odamlar = []
#
# for i in range(n):
#     odamlar.append(input(f"{i+1} odamni kiriting\n>>>"))
# print(odamlar)

# #########################  dars  - 10   #############################
# cars = ["toyota", "mazda", "hyundai", "gm", "kia"]
# for car in cars:
#     if (car != "gm"):
#         print(car.title())
#     else:
#         print(car.upper())

# ism = input("Ismingizni kiriting?\n>>>")
# admin = "Farruxjon"
# if ism == "Farruxjon":
#     print(f"Xush kelibsiz admin {admin} \n"
#           f"Foydalanuvchilar ro'yxatini ko'rishni xohlaysizmi?")
# else:
#     print(f"Xush kelibsiz hurmatli {ism} aka")

# a = int(input("birinchi son kiriting\n>>>"))
# b = int(input("ikkinchi son kiriting\n>>>"))

# if a == b:
#     print("kiritgan sonlaringiz teng")
# elif a > b:
#     print("birinchi son ikkinchi sondan katta")
# else:
#     print("birinchi son ikkinchi sondan kichik")

# a = int(input("ixtiyoriy son kiriting\n>>>"))
# if a > 0:
#     print("musbat")
# else:
#     print("manfiy")

# a = int(input("Son kiriting?\n>>>"))

# if a>0:
#     print(a**(1/2))
# else:
#     print("musbat son kiriting")

# ###############################  dars - 11  #################################3

# a = int(input("juft son kiriting?\n>>>"))
#
# if a%2==0:
#     print("rahmat")
# else:
#     print("bu juft son emas")

# yosh = int(input("Yoshingiz nechada?\n>>>"))
#
# if yosh<4 or yosh>60:
#     print("Sizga kirish bepul")
# elif yosh >18:
#     print("Sizga 20000 so'm")
# else:
#     print("Sizga 10000 so'm")

# a = int(input("Birinchi sonni kiriting\n>>>"))
# b = int(input("ikkinchi sonni kiriting\n>>>"))
#
# if a>b:
#     print(f"{a}>{b}")
# elif a<b:
#     print(f"{a}<{b}")
# else:
#     print(f"{a}={b}")

# mahsulotlar = ['uzum', 'anor', 'shaftoli', 'olcha', 'flash', 'pepsi', 'cola', 'fanta', 'nok', 'behi']
#
# savat = []
# bor_mahsulotlar =[]
# yoq_mahsulotlar =[]
#
# for i in range(5):
#     savat.append(input(f"Savatga {i+1}-mahsulotni qo'shing\n>>>"))
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         yoq_mahsulotlar.append(mahsulot)
#
# if len(yoq_mahsulotlar)==0:
#     print("Do'konimizda hamma mahsulot mavjud")
# else:
#     print("Do'konimizda quyidagi mahsulotlar mavjud emas!")
#     for m in yoq_mahsulotlar:
#         print(m)

# foydalanuvchilar = ["farrux", 'azizbek', 'javohir', 'shukur', 'jahon']
#
# login = input("Yangi login kiriting: ")
# if login in foydalanuvchilar:
#     print("login band, boshqa login tanlang")
# else:
#     print('Xush kelibsiz foydalanuvchi')

# son = int(input("Istalgan butun son kiriting: "))
#
# for i in range(2,11):
#     if son%i==0:
#         print(f"{son} soni {i} soniga qoldiqsiz bo'linadi")


# ##################################  dars - 14  ##########################

# otam = {"ism": "islom", "familya":"oriqov", "tyil": 1972, "vil":"samarqand"}
#
# print(f"Menign otam {otam['ism'].title()} {otam['familya'].title()}, {otam['tyil']} da {otam['vil']} viloyatida tug'ilgan")

# sevimli_taomlar = {"Farrux":"palov", "Azizbek":"shashlik", "Ro'zimurod":"ko'za sho'rva"}
#
# traom = sevimli_taomlar['Farrux']
# print(f"Farruxning sevimli taomi {traom}")

# python_lugat = {
#     "if":"shartli operator",
#     "upper()":"metodi string turidagi matndagi barcha harflarni katta harfga o'tkazadi",
#     "lower()":"metodi string turidagi matndagi barcha harflarni kichik harfga o;tkazadi",
#     "print()":"funksiyasi kodimizni natijasini konsolga chiqarishda ishlatiladi",
#     "range(i,j,k)":"funksiya i dan j gacha bo'gan sonlarni k interval bilan chiqarib beradi",
#     "list()":"list yasash uchun ishlatiladigan funksiya",
#     "title()":"metodi matndagi so'zlarni birinchi harfini katta harfga o'zgartiradi",
#     "capitalize()":"matndagi birinchi kelgan so'zni birinchi harfini bosh harfga aylantiradi",
#     "for":"siklik operator",
#     "and":"mantiqiy ko'paytirish operatori",
#     "len()":"funksiyasi list elementlari sonini chiqarib beradi"
# }
#
# kaliit_soz = input("Kalit so'z kiriting: ")
#
# if kaliit_soz in python_lugat.keys():
#     print(python_lugat[kaliit_soz])
# else:
#     print("bunday terminni ma'nosini bilmayman")

# ##################################   dars - 15  #################################

# python_lugat = {
#     "if":"shartli operator",
#     "upper()":"metodi string turidagi matndagi barcha harflarni katta harfga o'tkazadi",
#     "lower()":"metodi string turidagi matndagi barcha harflarni kichik harfga o;tkazadi",
#     "print()":"funksiyasi kodimizni natijasini konsolga chiqarishda ishlatiladi",
#     "range(i,j,k)":"funksiya i dan j gacha bo'gan sonlarni k interval bilan chiqarib beradi",
#     "list()":"list yasash uchun ishlatiladigan funksiya",
#     "title()":"metodi matndagi so'zlarni birinchi harfini katta harfga o'zgartiradi",
#     "capitalize()":"matndagi birinchi kelgan so'zni birinchi harfini bosh harfga aylantiradi",
#     "for":"siklik operator",
#     "and":"mantiqiy ko'paytirish operatori",
#     "len()":"funksiyasi list elementlari sonini chiqarib beradi"
# }
#
# for kalit, qiymat in sorted(python_lugat.items()):
#     print(f"{kalit}, -  {qiymat}")
#

# davlatlar = {
#     "aqsh": "washington d.c",
#     "rossiya": "moskva",
#     "xitoy":"piken",
#     "qozog'iston":"astana",
#     "malayziya": "kuala-lumpur",
#     "tojikiston":"dushanbe",
#     "italiya":"rim",
#     "ispaniya":"madrid",
#     "angiliya":"london"
# }
#
# print("Dunyo davlatlari:")
# for davlat in sorted(davlatlar):
#     print(f"{davlat.upper()}")
#
# print("Poytaxtlar:")
# for poytaxt in sorted(davlatlar.values()):
#     print(poytaxt.title())
#
# davlat = input("Siz qaysi davlatni poytaxtini bilishni xohlaysiz?  ").lower()
# poytaxt = davlatlar.get(davlat)
#
# if poytaxt ==None:
#     print("Kechirasiz bu davlat haqida bizda ma'lumot yo'q")
# else:
#     print(davlatlar[davlat].title())

# taomlar = {
#     "osh":32000,
#     "kabob":30000,
#     "non":6000,
#     "salat":12000,
#     "pepsi":15000,
#     "limonchoy":6000,
#     "baliqkabob":30000,
#     "jiz":60000,
#     "tovuqkabob":15000,
#     "lag'mon":25000,
#     "norin":20000
# }

# b_taomlar= []
# print("3 ta taom buyurtma bering! ")
# for i in range(3):
#     b_taomlar.append(input(f"{i+1} - taom: "))
#
# for b_taom in b_taomlar:
#     if b_taom in taomlar:
#         print(f"{b_taom.title()} - {taomlar[b_taom]} so'm")
#     else:
#         print("Bunday taom bizda mavjud emas!")
#

# ###############################  dars - 16  ######################################

# data = [
#     {
#         "ism":"Abu Abdulloh Muhammad ibn Ismoil",
#         "t_joy":"Buxoro",
#         "t_yil":810,
#         "umri":60,
#         "asarlari":["Al-jome' as-sahih", "Al-adab al-mufrat", "At-tarix al-kabir", "At-tarix as-sag'ir"]
#     },
#     {
#         "ism":"Abdulla Qodiriy",
#         "t_joy":"Toshkent",
#         "t_yil":1894,
#         "umri":44,
#         "asarlari":["O'tgan kunlar", "Mehrobdan chayon", "Obid ketmon"]
#     },
#     {
#         "ism":"Erkin Vohidov",
#         "t_joy":"Farg'ona",
#         "t_yil":1936,
#         "umri":80,
#         "asarlari":["Tong nafasi", "Qo'shiqlarim sizga", "O'zbegim"]
#     },
#     {
#         "ism":"Alisher Navoiy",
#         "t_joy":"Hirot",
#         "t_yil":1441,
#         "umri":60,
#         "asarlari":["Xamsa", "Lison ut-tayr","Mahbub al-qulub"]
#     }
# ]
#
# for i in data:
#     print(f"\n{i['ism']}ning mashhur asarlari:")
#     for asar in i['asarlari']:
#         print(asar)

# kinolar = {
#     "Ali":["Terminator", "Rambo", "Titanik"],
#     "Vali":["Tenet", "Insepshin", "Interstellar"],
#     "Husan":["Abdullajon", "Bomba", "Shaytanat"],
#     "Hasan":["Mahallada duv-duv gap","John Wick"]
# }
#
# for ism in kinolar:
#     print(f"\n{ism}ning sevimli kinolari:")
#     for kinos in kinolar[ism]:
#         print(kinos)

# davlatlar = {
#     "O'zbekiston":{"poytaxt":"Toshkent", "hudud":448978, "Aholisi":33000000, "pulbirligi":"so'm"},
#     "Rossiya":{"poytaxt":"Moskva", "hudud":17098246, "Aholisi":144000000, "pulbirligi":"rubl"},
#     "AQSH":{"poytaxt":"Vashington", "hudud":9631418, "Aholisi":327000000, "pulbirligi":"dollar"},
#     "Malayziya":{"poytaxt":"Kuala-Lumpur", "hudud":329750, "Aholisi":25000000, "pulbirligi":"rinngit"}
# }
# davlat = input("Davlat nomini kiriting: ")
# if davlat in davlatlar:
#     print(f"\n{davlat}ning poytaxti {davlatlar[davlat]['poytaxt']}")
#     print(f"Hududi: {davlatlar[davlat]['hudud']} kv.m\n"
#           f"Pul birlig: {davlatlar[davlat]['pulbirligi']}\n"
#           f"Aholisi: {davlatlar[davlat]['Aholisi']}")
# else:
#     print("Bizda bu davlat haqida ma'lumot mavjud emas")















