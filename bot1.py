import telebot
from telebot import types

bot = telebot.TeleBot('***')

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.add(types.KeyboardButton("Сайты по тестированию"))
    keyboard.add(types.KeyboardButton("Сайты по программированию"))
    keyboard.add(types.KeyboardButton("Сайты по дизайну"))
    bot.send_message(message.chat.id, "Выберите категорию:", reply_markup=keyboard)

@bot.message_handler(func=lambda message: True)
def send_links(message):
    if message.text == "Сайты по тестированию":
        bot.send_message(message.chat.id, "1. https://testautomationu.applitools.com\n2. https://www.softwaretestinghelp.com")
    elif message.text == "Сайты по программированию":
        bot.send_message(message.chat.id, "1. https://stackoverflow.com\n2. https://github.com")
    elif message.text == "Сайты по дизайну":
        bot.send_message(message.chat.id, "1. https://dribbble.com\n2. https://www.behance.net")

bot.polling()
