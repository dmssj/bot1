import telebot

bot = telebot.TeleBot('***')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "напиши что-нибудь")

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.send_message(message.chat.id, f"ты написал: {message.text}")

bot.polling()
