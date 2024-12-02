import telebot
from telebot import types

bot = telebot.TeleBot('7729006288:AAHKoiwSNw1GOre8CeMF3Oyfvco_lD4T3ws')

menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
write= types.KeyboardButton("Записать событие")
events = types.KeyboardButton("События")
delete = types.KeyboardButton("Удалить событие")
edit = types.KeyboardButton("Редактировать событие")
menu.add(write,events,delete,edit)
back = types.ReplyKeyboardMarkup(resize_keyboard=True)
back_button = types.KeyboardButton("Назад")
back.add(back_button)

# реакция на команду start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Привет! Salam aleikum", reply_markup = menu)
bot.infinity_polling()