import telebot
print ("бот стартовал")
bot = telebot.TeleBot('927989743:AAFGgBj2eCI_hfYes4NArm7OAHmUGtQBzjo')
@bot.message_handler(commands=['start'])
def start_message (message):
	bot.send_message(message.chat.id, 'Боджорно дорогой!')
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Доброго времени суток, как насчет прогуляться по интересным местам нашего города?')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'До скорых встреч)')
    else message.texy.lower() == 'был бы рад узнать подробнее, о том какая прогулка тебе сегодня по душе '

bot.polling()

