from uuid import uuid4

class Avto:
    __num_avto = 0
    pi = 3.14159
    def __init__(self, make, model, color, year, price, km = 0):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.price = price
        self.__km = km
        self.__id = uuid4()
        Avto.__num_avto += 1

    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto

    def get_km(self):
        return self.__km

    def get_id(self):
        return self.__id

    def add_km(self, km):
        if km > 0:
            self.__km += km
        else:
            print("Moshinani kilometrini kamaytirib bo'lmaydi")


avto1 = Avto("GM", "Malibu", "Qora", "2023", 40000, 1000)


class Shaxs:
    """"Shaxslar haqida ma'lumotlar"""

    def __init__(self, ism, familya, passport, tyil):
        self.ism = ism
        self.familya = familya
        self.passport = passport
        self.tyil = tyil
        self.__telnum = 998932268258

    def get_telnum(self):
        return self.__telnum

    def get_info(self):
        """"Shaxs haqida ma'lunotlar"""
        info = f"{self.ism} {self.familya}. Passport: {self.passport}, {self.tyil}-yilda tug'ilgan"
        return info
    def get_age(self):
        """"Shaxsning yoshini qaytaruvchi metod"""
        return 2023 - self.tyil


class Talaba(Shaxs):
    """Talaba klassi"""
    __talabalar_soni = 0

    def __init__(self, ism, familya, passport, tyil, idraqam):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        Talaba.__talabalar_soni += 1
    @classmethod
    def get_talabalar_soni(cls):
        return cls.__talabalar_soni

    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam

    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich

    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info
    def fanga_yozil(self, fanlar):
        self.fanlar.append(fanlar)

    def remove_fan(self, fan):
        if fan in self.fanlar:
            self.fanlar.remove(fan)
        else:
            return "Siz bu fanga yozilmagansiz"


talaba1 = Talaba("Aloshukur", "Usmonov", "AB4961314", 1999, "login1254564")
talaba2 = Talaba("Aloshukur", "Usmonov", "AB4961314", 1999, "login1254564")
talaba3 = Talaba("Aloshukur", "Usmonov", "AB4961314", 1999, "login1254564")
print(Talaba.get_talabalar_soni())