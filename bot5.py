import telebot
import random

bot = telebot.TeleBot('')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Напиши 'картинка', и я отправлю тебе случайное изображение.")

@bot.message_handler(func=lambda message: message.text.lower() == "картинка")
def send_random_image(message):
    image_url = f"https://picsum.photos/seed/{random.randint(1, 10000)}/200/300"
    bot.send_photo(message.chat.id, image_url, caption="Вот случайная картинка для тебя!")

bot.polling()
