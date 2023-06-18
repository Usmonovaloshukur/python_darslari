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


buyurtmalar = ['olma','anjir','uzum','qovun']
mahsulotlar = {
    'olma':20000,
    'shaftoli':25000,
    'tarvuz':18000,
    'uzum':22000
}

while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narx = mahsulotlar[buyurtma]
        print(f"{buyurtma} ning narxi {narx} so'm")
    else:
        print(f"Bizda {buyurtma} yo'q")