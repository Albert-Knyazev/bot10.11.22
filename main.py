import telebot
from telebot import types

bot = telebot.TeleBot('*****************************************')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name}<u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess,parse_mode='html')


#@bot.message_handler(content_types=['text'])
#def get_user_text(message):
#    if message.text == 'Привет':
#        bot.send_message(message.chat.id, "Hello friend", parse_mode='html')
#    elif message.text == "id":
#        bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id}",parse_mode='html')
#    elif message.text == "photo":
#        photo = open('mult.jpg','rb')
#        bot.send_photo(message.chat.id, photo)
#    else:
#        bot.send_message(message.chat.id, "Неизвестная команда",parse_mode='html')


@bot.message_handler(content_types=['sticker'])
def get_user_sticker(message):
    bot.send_message(message.chat.id, 'Вау, стикер!')


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить веб сайт", url="http://peupeu.ru/"))
    bot.send_message(message.chat.id,'Перейдите на сайт', reply_markup=markup)


@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
    website = types.KeyboardButton('Веб сайт')
    start = types.KeyboardButton('Start')
    markup.add(website,start)
    bot.send_message(message.chat.id,'Перейдите на сайт', reply_markup=markup)


bot.polling(none_stop=True)
    #python body.py
    #ctrl+c ili shift+f2
