# ####################################  dars  -  28   ############################################
#
# class Talaba:
#     def __init__(self, isim, familya, tyil):
#         self.isim = isim
#         self.familya = familya
#         self.tyil = tyil
#     def tanishtir(self):
#         return f"Ismim: {self.isim}, familyam: {self.familya}, tug'ilgan yilim: {self.tyil}"
#
#     def yoshi(self, yil):
#         return yil - self.tyil
#
#
#
# talaba1 = Talaba("Aloshukur", "Usmonov", 1999)
# talaba2 = Talaba("Farruxjon", "Uktamov", 2000)
# talaba3 = Talaba("Azizbek", "Namozov", 2000)
#
# print(talaba1.yoshi(2023))
# print(talaba2.yoshi(2023))
# print(talaba3.yoshi(2023))


# class User:
#     def __init__(self, name, username, email, password):
#         self.name = name
#         self.username = username
#         self.email = email
#         self.password = password
#
#     def get_name(self):
#         return self.name
#     def get_info(self):
#         return f"Ismi: {self.name}, Foydalanuvchi ismi: {self.username}, Email: {self.email}, Parol: {self.password}"
#
# user1 = User("Jahongir", "jahon007", "usmonovjahongir@gmail.com", "12!ja@#h21")
#
# print(user1.get_name())
# print(user1.get_info())



##############################  dars  -  29  #####################################

# class Talaba:
#     def __init__(self, isim, familya, tyil):
#         self.isim = isim
#         self.familya = familya
#         self.tyil = tyil
    #     self.bosqich = 1
    # def get_name(self):
    #     return self.isim
    # def get_familiya(self):
    #     return self.familya
    # def get_fullname(self):
    #     return f"{self.isim} {self.familya}"
    # def get_info(self):
    #     return f"Ismim: {self.isim}, familyam: {self.familya}, bosqichi: {self.bosqich}"

#     def get_age(self, yil):
#         return yil - self.tyil
#
#     def set_bosqich(self, yangi_bosqich):
#         self.bosqich = yangi_bosqich
#     def update_bosqich(self):
#         self.bosqich += 1
#
# class Fan():
    # def __init__(self, nomi):
    #     self.nomi = nomi
    #     self.talabalar_soni = 0
    #     self.talabalar = []
    # def add_student(self, talaba):
    #     """"Fanga talaba qo'shish"""
    #     self.talabalar.append(talaba)
    #     self.talabalar_soni += 1
    # def get_student(self):
    #     return [talaba.get_info() for talaba in self.talabalar]



# matematika = Fan("Oliy Matematika")
# talaba1 = Talaba("Alijon","Valiyev",2000)
# talaba2 = Talaba("Hasan","Alimov",2001)
# talaba3 = Talaba("Akrom","Boriyev",2001)
#
#
# matematika.add_student(talaba1)
# matematika.add_student(talaba2)
# matematika.add_student(talaba3)
#
# print(matematika.get_student())
#
#
# def see_methods(klass):
#     return [method for method in dir(klass) if method.startswith("__") is False]
# # print(see_methods(Talaba))
#
# # print(talaba1.__dict__.values())
#
#
#
# class Avto():
#     def __init__(self, model, rang, karobka, narx):
#         self.model = model
#         self.rang = rang
#         self.karobka = karobka
#         self.narx = narx
#         self.kilometr = 0
#     def get_info(self):
#         return f"Model {self.model}, rangi {self.rang}, karobkasi {self.karobka}, " \
#                f"narxi {self.narx}, probegi {self.kilometr}"
#
#     def update_km(self, km):
#         self.kilometr += km
#
# avto1 = Avto("Malibu", "qora","avtomat", 40000)
# avto2 = Avto("KIA K8", "qora","avtomat", 80000)
# avto3 = Avto("Lacetti", "oq","mexanika", 10000)
# avto1.update_km(25000)
#
# class Avtosalon():
#     def __init__(self, name, location):
#         self.name = name
#         self.location = location
#         self.avtos_for_sale = []
#         self.avto_valume = 0
#     def add_avto(self, avto):
#         self.avtos_for_sale.append(avto)
#         self.avto_valume += 1
#
#     def get_info(self):
#         return [avto.get_info() for avto in self.avtos_for_sale]
#     def get_name(self):
#         return self.name
#     def get_address(self):
#         return self.location
#
# avtosalon1 = Avtosalon("SUPER CARS", "GEORGE AVENU 25")
#
# avtosalon1.add_avto(avto1)
# avtosalon1.add_avto(avto2)
# avtosalon1.add_avto(avto3)
# avto3.update_km(15000)
# print(f"{avtosalon1.get_name()} avtosaloni, manzil {avtosalon1.get_address()}")
# for avtomobile in avtosalon1.get_info():
#     print(avtomobile)
#

# print(see_methods(Avto))