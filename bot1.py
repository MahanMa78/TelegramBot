import telebot 
from config import API_TOKEN

bot = telebot.TeleBot(API_TOKEN)

user_id = []

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id,'Welcome to microlearn Bot.')
    if message.chat.id not in user_id:
        user_id.append(message.chat.id)


@bot.message_handler(commands=['SUPU2024'])
def send_update(message):
    for id in user_id:
        bot.send_message(id,"The Product is available.")

bot.polling()