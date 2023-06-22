# import avto_info_mod as aim
#
# avto1 = aim.avto_info("GM", "Malibu", "qora", "avtomat",2020,40000)
#
# aim.info_print(avto1)

# from avto_info_mod import info_print, avto_info
#
# avto1 = avto_info("GM", "Malibu", "qora", "avtomat",2020,40000)
# info_print(avto1)

# from avto_info_mod import avto_info as ainfo, info_print as iprint
#
# avto1 = ainfo("GM", "Malibu", "qora", "avtomat",2020,40000)
# iprint(avto1)

# modul ichidagi barcha funksiyalarni ko'chirib olish

# from avto_info_mod import *
#
# avto1 = avto_info("GM", "Malibu", "qora", "avtomat",2020,40000)
# info_print(avto1)

# math moduli

# from math import sqrt,pow,pi,log2, log10
# x=400
# print(sqrt(x))
# print(pow(25,2))
# print(pi)
# print(log2(16))
# print(log10(1000))

import random as r
son = r.randint(25,250)
print(son)

ismlar = ["hasan", "husan", "farrux", "javohir", "abdulmo'min", "azizbek"]
ism = r.choice(ismlar)
print(ism)
print(r.choice(ism))

r.shuffle(ismlar)
print(ismlar)