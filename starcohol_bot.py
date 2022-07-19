import telebot
from telebot import types
bot = telebot.TeleBot('5385998740:AAGTl4Jv7YeLmZhPcMuhX02vyHHpt7jyqIE')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет ✌️ ')

@bot.message_handler(commands=['button'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_yes = types.KeyboardButton("VK")
    button_git = types.KeyboardButton("Git")
    markup.add(button_yes, button_git)
    bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)

@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == "VK":
        bot.send_message(message.chat.id, "https://vk.com/id113935641")
    if message.text == "Git":
        bot.send_message(message.chat.id, "https://github.com/Igoryha")

bot.polling()
