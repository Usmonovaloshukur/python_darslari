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


class User:
    def __init__(self, name, username, email, password):
        self.name = name
        self.username = username
        self.email = email
        self.password = password

    def get_name(self):
        return self.name
    def get_info(self):
        return f"Ismi: {self.name}, Foydalanuvchi ismi: {self.username}, Email: {self.email}, Parol: {self.password}"

user1 = User("Jahongir", "jahon007", "usmonovjahongir@gmail.com", "12!ja@#h21")

print(user1.get_name())
print(user1.get_info())