import telebot

bot = telebot.TeleBot('')

user_data = {}

@bot.message_handler(commands=['start'])
def start(message):
    user_data[message.chat.id] = {'step': 1}
    bot.send_message(message.chat.id, "Привет! Как тебя зовут?")

@bot.message_handler(func=lambda message: True)
def conversation(message):
    chat_id = message.chat.id

    if chat_id not in user_data:
        user_data[chat_id] = {'step': 1}

    step = user_data[chat_id]['step']

    if step == 1:
        user_data[chat_id]['name'] = message.text
        bot.send_message(chat_id, f"Тебя зовут {message.text}. Сколько тебе лет?")
        user_data[chat_id]['step'] = 2

    elif step == 2:
        if message.text.isdigit():
            user_data[chat_id]['age'] = message.text
            bot.send_message(chat_id, f"Тебе {message.text} лет. Чем ты увлекаешься?")
            user_data[chat_id]['step'] = 3
        else:
            bot.send_message(chat_id, "Пожалуйста, напиши возраст числом.")

    elif step == 3:
        user_data[chat_id]['hobby'] = message.text
        bot.send_message(chat_id, f"Здорово! Ты увлекаешься {message.text}. Было приятно познакомиться!")
        del user_data[chat_id]

bot.polling()
