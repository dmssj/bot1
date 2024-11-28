import telebot
import requests

bot = telebot.TeleBot('***')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Напиши 'запрос', чтобы получить данные.")

@bot.message_handler(func=lambda message: message.text == "запрос")
def get_api_data(message):
    # Новый сайт для запроса
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    if response.status_code == 200:
        data = response.json()
        email = data['email']  # Извлечение почты пользователя
        bot.send_message(message.chat.id, f"Email пользователя: {email}")
    else:
        bot.send_message(message.chat.id, "Ошибка при запросе данных.")

bot.polling()
