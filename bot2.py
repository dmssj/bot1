import telebot

bot = telebot.TeleBot('')

@bot.message_handler(content_types=['voice'])
def voice_handler(message):
    bot.send_message(message.chat.id, "спасибо за гс")

bot.polling()
