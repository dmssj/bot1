import telebot
from telebot import types

bot = telebot.TeleBot('***')

@bot.message_handler(commands=['start'])
def start(message):
    # Создание клавиатуры
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.add(types.KeyboardButton("напиши 'Закрыть' в сообщении бота"))
    bot.send_message(message.chat.id, "напиши 'Закрыть', чтобы убрать клавиатуру.", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == "Закрыть")
def close_keyboard(message):
    bot.send_message(message.chat.id, "клавиатура убрана", reply_markup=types.ReplyKeyboardRemove())

bot.polling()
