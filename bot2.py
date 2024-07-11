import telebot 
from config import API_TOKEN
from telebot.types import InlineKeyboardButton,InlineKeyboardMarkup

bot = telebot.TeleBot(API_TOKEN)

button1 = InlineKeyboardButton(text="Button1",callback_data="btn1")
button2 = InlineKeyboardButton(text="Button2",url="https://bing.com")
inline_keyboard = InlineKeyboardMarkup(row_width=2)
inline_keyboard.add(button1,button2)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id,"Welcome dear user",reply_markup=inline_keyboard)


@bot.callback_query_handler(func=lambda call:True)
def check_button(call):
    if call.data == "btn1":
        bot.answer_callback_query(call.id,"btn1 is tapped ",show_alert=True)



bot.polling()