

# import datetime as dt
# import math
# import re

# hozir = dt.datetime.now()
# print(hozir)
# print(hozir.date())
# print(hozir.time())
# print(hozir.hour)
# print(hozir.minute)
# print(hozir.second)
#
# bugun = dt.date.today()
# print(bugun)
#
# ertaga = dt.date(2023,6,28)
# print(ertaga)

# bugun = dt.datetime.now()
# hayit = dt.datetime(2023,6,28,5,30,00)
#
# farq = hayit - bugun
# sekundlar = farq.seconds
# minutlar = int(sekundlar/60)
# soatlar = int(minutlar/60)
#
#
# # print(f"Hayitga {farq.days} kun {soatlar} soat qoldi")
#
# vaqt = bugun.strftime("%H:%M:%S")
# print(f"Hozir vaqt {vaqt}")
#
# sana = bugun.strftime("%d-%m-%Y")
# print(sana)
# hozir = bugun.strftime("%d %m %Y, %H:%M")
# print(hozir)

# hozir = dt.date.today()
# workdate = dt.date(2023, 9, 5)
#
# farq = workdate - hozir
# # print(round(farq.days/30), " months")
#
# datebirth = dt.date(1999, 12, 6)
# umr = hozir - datebirth
# days = umr.days

# print(f"{days}")


# andoza = "^\+[1-9]\d{1,14}$"
#
# telnum1 = input("telefon raqam kiriting: ")
# # telnum2 = "8932268258"
#
# if re.match(andoza,telnum1):
#     print("Raqamingiuz tasdiqlandi")
# else:
#     print("Telefon raqam kiriting!")

# matn = "Assalom alaykum hurmatli do'stlar. Navbatdagi darsimiz YouTubega yuklandi:"
# matn += " https://youtu.be/vsxJPRLXpgI Ushbu darsimizda unittest moduli yordamida klasslarning xususiyatlar va"
# matn += " metodlarini tekshiruvchi dastur yozishni o'rganamiz. Bugungi dars manzili: https://python.sariq.dev/testing/37-klass-test"
#
# andoza = "https?:\/\/[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}/\/b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)"
#
# print(re.findall(andoza, matn))

