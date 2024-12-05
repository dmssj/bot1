import telebot
from telebot import types

bot = telebot.TeleBot('')

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("Сайты по тестированию"))
    keyboard.add(types.KeyboardButton("Сайты по программированию"))
    keyboard.add(types.KeyboardButton("Сайты по дизайну"))
    bot.send_message(message.chat.id, "Выберите категорию:", reply_markup=keyboard)

@bot.message_handler(func=lambda message: True)
def send_links(message):
    if message.text == "Сайты по тестированию":
        bot.send_message(
            message.chat.id,
            "Сайты по тестированию:\n"
            "1. [Test Automation University](https://testautomationu.applitools.com) - курсы по автоматизации тестирования.\n"
            "2. [Software Testing Help](https://www.softwaretestinghelp.com) - статьи и советы для тестировщиков."
        )
    elif message.text == "Сайты по программированию":
        bot.send_message(
            message.chat.id,
            "Сайты по программированию:\n"
            "1. [Stack Overflow](https://stackoverflow.com) - форум для программистов, где можно найти ответы на вопросы.\n"
            "2. [GitHub](https://github.com) - платформа для хранения и совместной работы над проектами."
        )
    elif message.text == "Сайты по дизайну":
        bot.send_message(
            message.chat.id,
            "Сайты по дизайну:\n"
            "1. [Dribbble](https://dribbble.com) - галерея работ дизайнеров.\n"
            "2. [Behance](https://www.behance.net) - портфолио и проекты креативных специалистов."
        )
    else:
        bot.send_message(message.chat.id, "Выберите категорию с клавиатуры.")

bot.polling()
