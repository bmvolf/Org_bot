import telebot
import config
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    chat_id = message.chat.id
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_start = telebot.types.InlineKeyboardButton(text='🦤 Начать экскурсию!',
                                                     callback_data='menu')
    keyboard.add(button_start)
    bot.send_message(chat_id,
                     'Добро пожаловать в бота экскурсовода по Москве!',
                     reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == 'menu')
def menu(call):
    message = call.message
    chat_id = message.chat.id
    message_id = message.message_id 
    bot.delete_message(chat_id, message_id)
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)
    buttons = []
    for i in range(1, 11):
        button = telebot.types.InlineKeyboardButton(text=config.Names[i-1], callback_data=f'kafe_{i}')
        buttons.append(button)
    for i in range(0, len(buttons), 2):
        if i + 1 < len(buttons):
            keyboard.add(buttons[i], buttons[i+1])
        else:
            keyboard.add(buttons[i])
    bot.send_message(chat_id=chat_id, 
                         text=('Привет! Я бот экскурсовод по самым вкусным, исторически насыщенным и '
                         'интересным местам Москвы, чтобы выбрать место, нажми на кнопку!'), reply_markup=keyboard)
    

@bot.callback_query_handler(func=lambda call: 'kafe' in call.data)
def cafe(call):
    message = call.message
    chat_id = message.chat.id
    message_id = message.message_id
    cafe_id = int(call.data.split('_')[-1])
    cafe_info = config.Descriptions[cafe_id-1]
    cafe_photo = config.Images[cafe_id-1]
    cafe_map = config.MapLinks[cafe_id-1]
    bot.delete_message(chat_id, message_id)
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
    button_back = telebot.types.InlineKeyboardButton(text="↩️ Назад", callback_data='menu')
    button_map = telebot.types.InlineKeyboardButton(text='🗺 На карте', url=cafe_map)
    keyboard.add(button_map, button_back)
    bot.send_photo(chat_id=chat_id, photo = cafe_photo, caption=f'{cafe_info}',reply_markup=keyboard)

if __name__ == '__main__':
    print('Бот запущен!')
    bot.infinity_polling()