import telebot
import config
import random
from telebot import types


bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcomeMessage(message):
    sti = open('giphy.mp4', 'rb')
    bot.send_animation(message.chat.id, sti)  # отправить стикер
    bot.send_message(message.chat.id, "Дарова")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('1')
    item2 = types.KeyboardButton('2')
    markup.add(item1, item2)
    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот /"
                     "созданный чтобы быть подопытным кроликом.".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def replyMessage(message):
    if message.chat.type == 'private':
        if message.text == '1':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('11')
            item2 = types.KeyboardButton('12')
            markup.add(item1, item2)
            bot.send_message(message.chat.id,
                             'Ты выбрал 1'.format(
                                 message.from_user, bot.get_me()),
                             parse_mode='html', reply_markup=markup)
        if message.text == '11':
            markup = types.ReplyKeyboardRemove()
            bot.send_message(message.chat.id,
                             '11'.format(
                                 message.from_user, bot.get_me()),
                             parse_mode='html', reply_markup=markup)
        if message.text == '2':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('21')
            item2 = types.KeyboardButton('22')
            markup.add(item1, item2)
            bot.send_message(message.chat.id,
                             'Ты выбрал 2'.format(
                                 message.from_user, bot.get_me()),
                             parse_mode='html', reply_markup=markup)
        if message.text == '11':
            markup = types.ReplyKeyboardRemove()
            bot.send_message(message.chat.id,
                             '11'.format(
                                 message.from_user, bot.get_me()),
                             parse_mode='html', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Я не знаю че ты написал')



bot.polling(none_stop=True)