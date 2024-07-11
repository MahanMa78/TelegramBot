
import telebot
from telebot import types,apihelper
from config import API_TOKEN

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,"Please Enter your name: ")
    bot.register_next_step_handler(message,process_name)
    #register_next_step_handler --> baraye inke belafasele bere va handle baadi ro call kone
    
def process_name(message):
    name = message.text
    bot.send_message(message.chat.id,f"Hello {name}! How old are you?")

    bot.register_next_step_handler(message,process_age)

def process_age(message):
    age=message.text
    bot.send_message(message.chat.id,f"You Are {age} years old.\nThank you")

bot.polling()