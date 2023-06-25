################################   dars - 32  #######################################
from uuid import uuid4
#
#
# class Avto:
#     __num_avto = 0
#     pi = 3.14159
#     def __init__(self, make, model, color, year, price, km = 0):
#         self.make = make
#         self.model = model
#         self.color = color
#         self.year = year
#         self.price = price
#         self.__km = km
#         self.__id = uuid4()
#         Avto.__num_avto += 1
#
#     def __repr__(self):
#         """"Obekt haqida ma'lumot"""
#         return f"{self.color} rangli {self.model}, narxi {self.price}$"
#     def __lt__(self, other):
#         """"Kichik"""
#         return self.price < other.price
#     def __le__(self, other):
#         """"Kichik yoki teng"""
#         return self.price <= other.price
#     def __eq__(self, other):
#         return self.price == other.price
#
# class Avtosalon:
#     def __init__(self, name):
#         self.name = name
#         self.avtolar = []
#     def __len__(self):
#         return len(self.avtolar)
#     def __repr__(self):
#         return f"{self.name} avtosaloni"
#     def add_avto(self, *avtolar):
#         for avto in avtolar:
#             if isinstance(avto, Avto):
#                 self.avtolar.append(avto)
#             else:
#                 print("Avto obyektini kiriting!")
#     def __getitem__(self, item):
#         return self.avtolar[item]
#     def __setitem__(self, key, value):
#         if isinstance(value, Avto):
#             self.avtolar[key] = value
#     def __add__(self, other):
#         if isinstance(other, Avtosalon):
#             yangi_salon = Avtosalon(f"{self.name} {other.name}")
#             yangi_salon.avtolar = self.avtolar + other.avtolar
#             return yangi_salon
#         elif isinstance(other, Avto):
#             self.add_avto(other)
#         else:
#             print(f"Avtosalonga {type(other)} ni qo'shib bo'lmaydi")
#     def __call__(self, *param):
#         if param:
#             for avto in param:
#                 self.add_avto(avto)
#         else:
#             return [avto for avto in self.avtolar]
#
#
#
#
#
#
#
# avto1 = Avto("GM", "Malibu", "Qora", 2020, 40000)
# avto2 = Avto("GM","Lacetti","Oq",2020,7000)
# avto3 = Avto("Toyota",'Carolla',"Silver",2018, 45000)
# avto4 = Avto("Mazda", "Mazda 6", "Qizil", 2015, 35000)
# avto5 = Avto("Volkswagen","Polo",'Qora',2015,30000)
# avto6 = Avto("Honda","Accord","Oq",2017,42000)
#
# avtosalon1 = Avtosalon("MaxAvto")
# avtosalon2 = Avtosalon("Super Cars")
# avtosalon1.add_avto(avto1,avto2,avto3)
# avtosalon2.add_avto(avto4,avto5,avto6)
#
#
# avto7 = Avto("BMW", 'X7','Qora',2015,75000)
# avtosalon1 + avto7
# avto_new = Avto("Mercedes-Benz", 'E200','Silver',2015,80000)
# avtosalon1(avto_new)
# print(avtosalon1[:])
# #
# # x,y = 10, 2
# # # print(x*5)
#
# t1 = "hello"
# t2 = " world"
# # print(t1+t2)
# # print(t1*3)
#
# l1 = [1,2,3]
# l2 = [4,5,6]
# # print(l1*2+l2*2)

# ###########  Amaliyot ######################

class Talaba:
    def __init__(self, name, familyname, yosh):
        self.name = name
        self.familyname = familyname
        self.yosh = yosh
        self.id = uuid4()
    def __repr__(self):
        return f"{self.name} {self.familyname}"

    def __lt__(self, other):
        return self.yosh < other.yosh
    def __ge__(self, other):
        return self.yosh >= other.yosh

class Fan:
    def __init__(self, name):
        self.name = name
        self.talabalar = []

    def __repr__(self):
        return f"{self.name} fani"

    def add_student(self, *talabalar):
        for talaba in talabalar:
            if isinstance(talaba, Talaba):
                self.talabalar.append(talaba)
            else:
                print("Talaba kiriting")

    def __len__(self):
        return len(self.talabalar)
    def __getitem__(self, item):
        return self.talabalar[item]

    def __setitem__(self, key, value):
        if isinstance(value, Talaba):
            self.talabalar[key] = value
    def __add__(self, other):
        if isinstance(other, Fan):
            yangi_fan = f"{self.name} {other.name}"
            yangi_fan.talabalar = self.talabalar + other.talabalar
            return yangi_fan
        elif isinstance(other,Talaba):
            self.add_student(other)
        else:
            print(f"Avtosalonga {type(other)} qo'shib bo'lmaydi")
    def __call__(self, *parm):
        if parm:
            for talaba in parm:
                self.add_student(talaba)
        else:
            return [talaba for talaba in self.talabalar]

fan1 = Fan("Kvant Elektrodinamikasi")
fan2 = Fan("Klassik Elektrodinamika")

talaba1 = Talaba("Aloshukur", "Usmonov", 1999)
talaba2 = Talaba("Javohir", "Toshqo'rg'onov", 2001)
talaba3 = Talaba("Farrux", "Uktamov", 2000)

fan1.add_student(talaba1, talaba2)

fan1(talaba3)
print(fan1())

