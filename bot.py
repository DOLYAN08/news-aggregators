# Агрегатор новостей, телеграм бот  @News_by_bot
import telebot
import config
import ParserNews
from telebot import types


bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Новости belta.by')
    item2 = types.KeyboardButton('Новости tut.by')
    item3 = types.KeyboardButton('Новости yandex.by')
    item4 = types.KeyboardButton('Последние новости.')
    keyboard.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id,
                     'Привет! \n Выбери новостной ресурс для отоброжения актуальных новостей'
                     .format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def handler(message):
    if message.chat.type == 'private':
        if message.text == 'Последние новости.':
            class_name = 'news'
        elif message.text == 'Новости tut.by':
            class_name = 'tut_by'
        elif message.text == 'Новости yandex.by':
            class_name = 'yandex_by'
        elif message.text == 'Новости belta.by':
            class_name = 'belta_by'
        else:
            pass
        for i in range(len(ParserNews.create_class(class_name))):
            bot.send_message(message.chat.id,
                             (ParserNews.create_class(class_name))[i],
                             parse_mode='html')


bot.polling(none_stop=True)
