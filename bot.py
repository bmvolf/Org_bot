import telebot
from telebot import types
from enum import Enum

bot = telebot.TeleBot('8403510554:AAElPR25rtD1lE8WRhanOrXEfsN231DPYVc')
class ExcursionType(Enum):
    Empty = 0
    RedSquare = 1
    Chistie = 2
    Strogino = 3
excursion = ExcursionType.Empty
excursionText = [['0RS','1RS','2rs','3rs','4rs','5rs','6rs','7rs'],\
    ['0ch','1ch','2ch','3ch','4ch','5ch','6ch','7ch'],\
        ['0st','1st','2st','3st','4st','5st','6st','7st']]
cnt = 0
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🦤 Начать экскурсию!")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-экскурсовод!", reply_markup=markup)
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global cnt, excursion
    if message.text == '🦤 Начать экскурсию!':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('🇷🇺 Красная площадь')
        btn2 = types.KeyboardButton('🦆 Чистые пруды')
        btn3 = types.KeyboardButton('⛵️ Строгино')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, 'Выберите маршрут:', reply_markup=markup) #ответ бота
    elif message.text == '🇷🇺 Красная площадь':
        excursion = ExcursionType.RedSquare
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('⬅️')
        btn2 = types.KeyboardButton('⏏️')
        btn3 = types.KeyboardButton('➡️')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, excursionText[excursion.value-1][cnt], reply_markup=markup)
    elif message.text == '🦆 Чистые пруды':
        excursion = ExcursionType.Chistie
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('⬅️')
        btn2 = types.KeyboardButton('⏏️')
        btn3 = types.KeyboardButton('➡️')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, excursionText[excursion.value-1][cnt], reply_markup=markup)
    elif message.text == '⛵️ Строгино':
        excursion = ExcursionType.Strogino
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('⬅️')
        btn2 = types.KeyboardButton('⏏️')
        btn3 = types.KeyboardButton('➡️')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, excursionText[excursion.value-1][cnt], reply_markup=markup)
    elif message.text == '➡️':
        if cnt == 7:
            bot.send_message(message.from_user.id, 'Вы прошли экскурсию')
        elif cnt < 7:
            cnt += 1
            bot.send_message(message.from_user.id, excursionText[excursion.value-1][cnt])
    elif message.text == '⬅️':
        if cnt == 0:
            bot.send_message(message.from_user.id, 'Вы только в начале экскурсию')
        elif cnt >= 1:
            cnt -= 1
            bot.send_message(message.from_user.id, excursionText[excursion.value-1][cnt])
    elif message.text == '⏏️':
        excursion = ExcursionType.Empty
        cnt = 0
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🇷🇺 Красная площадь')
        btn2 = types.KeyboardButton('🦆 Чистые пруды')
        btn3 = types.KeyboardButton('⛵️ Строгино')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, 'Выберите маршрут:', reply_markup=markup)
        

bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть