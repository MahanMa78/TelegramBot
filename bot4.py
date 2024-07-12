import sqlite3
from telebot import TeleBot
from config import API_TOKEN
from telebot.types import KeyboardButton,ReplyKeyboardMarkup

bot = TeleBot(token=API_TOKEN)

keyboard = ReplyKeyboardMarkup(resize_keyboard=True,row_width=1) #khodesh miad shomare ro migire
button = KeyboardButton(text="send my info",request_contact=True)
keyboard.add(button)


#create database
with sqlite3.connect('user.db') as connection:
    cursor = connection.cursor()
    create_table_query = """
    CREATE TABLE IF NOT EXISTS user(
        id integer primary key,
        first_name text,
        last_name text,
        phone_number text
    );
"""
    cursor.execute(create_table_query)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,"Welcome to microlearn bot",reply_markup=keyboard)

@bot.message_handler(content_types=['contact'])
def contact(message):
    # bot.send_message(message.chat.id,text = f"{message.contact} ")
    with sqlite3.connect('user.db') as connection:
        cursor = connection.cursor()
        insert_data_query = """
            INSERT INTO user(id,first_name,last_name,phone_number)
            VALUES (?,?,?,?)
        """
        data = (
            message.contact.user_id,
            f'{message.contact.first_name}',
            f"{message.contact.last_name}",
            f"{message.contact.phone_number}"
        )
        cursor.execute(insert_data_query,data)

bot.polling()