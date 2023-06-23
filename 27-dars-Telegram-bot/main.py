from transliterate import to_latin, to_cyrillic
import telebot

token = "5531356659:AAHYKNJO0z4I1wFoV9zyCY_eR04bCo7cMiU"
bot = telebot.TeleBot(token, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = "Assalomu Alekum. Xush kelibsiz"
    javob += "\nMatn kiriting!"
    bot.reply_to(message, javob)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    javob = lambda msge: to_cyrillic(msge) if msg.isascii() else to_latin(msge)
    bot.reply_to(message, javob(msg))

bot.polling()

# matn = input("Matn kiriting: ")
# if matn.isascii():
#     print(to_cyrillic(matn))
# else:
#     print(to_latin(matn))