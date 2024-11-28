import telebot

bot = telebot.TeleBot('8101859131:AAHsM5oqmiSeyuXpvn-J52wQQNd67OLNY6U')

@bot.message_handler(content_types=['voice'])
def voice_handler(message):
    bot.send_message(message.chat.id, "спасибо за гс")

bot.polling()
