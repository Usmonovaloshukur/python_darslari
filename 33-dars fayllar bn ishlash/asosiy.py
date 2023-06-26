
import pickle


# with open("things.txt") as fayl:
#     info = fayl.read()
#
# print(info)

with open("pi_million_digits.txt") as jild:
    pi = jild.read()
pi = pi.rstrip()
pi = pi.replace("\n", "")
pi = pi.replace(" ", "")
# print(pi)
datebirth = "06121999"
# print(datebirth in pi)

pi = float(pi)
# print(type(pi))

with open("pi.pkl", "wb") as fayl:
    pickle.dump(pi, fayl)

with open("pi.pkl", "rb") as son:
    pisoni = pickle.load(son)
# print(pisoni)

while True:
    book = input("Yaxshi ko'rgan kitoblaringizni kiriting, to'xtatmoqchi bo'lsangiz enter tugmasini bosing \n>>>")
    if not book: break
    with open("books.txt", "a") as file:
        file.write(book + "\n")

