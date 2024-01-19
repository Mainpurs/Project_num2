import json
from typing import Any, Dict

import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "6907816424:AAFtptMbHmk8FH4w39qBW7Zy1533IKPiPEM"
bot = telebot.TeleBot(TOKEN)

markup = ReplyKeyboardMarkup(resize_keyboard=True)
markup.add(KeyboardButton('1'))
markup.add(KeyboardButton('2'))

msg = None


filename = "user_data.json"


def load_data():
    try:
        with open(filename, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    return data


def save_data(data):
    with open(filename, "w") as f:
        json.dump(data, f)


@bot.message_handler(commands=['start'])
def welcome(message):
    user_id = message.chat.id
    msg = bot.send_message(message.chat.id, 'Привет! Ты - охотник за приключениями!\n И ты решил, как и все, не много подзаработать. Ну что? Дозиметр на готове?\nТогда пойдем! /start_game')
    data = load_data()
    if str(user_id) not in data:
        data[str(user_id)] = {}
    data[str(user_id)] = {'name': '', 'x': '', 'story1_loc1': '', 'story1_loc2': '', 'story1_loc3': '', 'story1_loc4': '', 'story1_final': '', 'story2_loc1': '', 'story2_loc2': '', 'story2_loc3': '', 'story2_loc4': '', 'story2_final': ''}
    save_data(data)  # я добавил story для развых веток.


@bot.message_handler(commands=['start_game'])
def loc1(message):
    user_id = message.chat.id
    data = load_data()
    msg = bot.send_message(message.chat.id, 'Ты у себя на базе, но пора продумывать план на миллион! Куда пойдешь?\n '
                                            '1)В опасную зону под названием - Радиус.\n 2)В интересную зону - СССР!',
                           reply_markup=markup)
    if message.text == str(1):
        data[str(user_id)]["story1_loc1"] = message.text
        data[str(user_id)]["story2_loc1"] = 0
    elif message.text == str(2):
        data[str(user_id)]["story2_loc1"] = message.text
        data[str(user_id)]["story1_loc1"] = 0
    else:
        data[str(user_id)]["name"] = message.text

    if str(user_id) not in data:
        data[str(user_id)] = {}
    data[str(user_id)] = {'name': '', 'x': '', 'story1_loc1': '', 'story1_loc2': '', 'story1_loc3': '', 'story1_loc4': '', 'story1_final': '', 'story2_loc1': '', 'story2_loc2': '', 'story2_loc3': '', 'story2_loc4': '', 'story2_final': ''}
    save_data(data)
    bot.register_next_step_handler(msg, loc2)


def loc2(message):
    user_id = message.chat.id
    data = load_data()
    msg = None

    if message.text == str(1):
        data[str(user_id)]["story1_loc1"] = message.text
        data[str(user_id)]["story2_loc1"] = '0'
    elif message.text == str(2):
        data[str(user_id)]["story2_loc1"] = message.text
        data[str(user_id)]["story1_loc1"] = '0'
    else:
        data[str(user_id)]["name"] = message.text

    if data[str(user_id)]['story1_loc1'] == '1':
        msg = bot.send_message(message.chat.id,
                               'Ты не заметил, как забрёл в минное поле из аномалий! вот неудача!\n '
                               '1)Идти напролом.\n 2)Сверяться с картой аномалий и идти потихоньку.',
                               reply_markup=markup)
        data[str(user_id)]["story1_loc2"] = message.text
        data[str(user_id)]["story2_loc2"] = '0'
        save_data(data)

    elif data[str(user_id)]["story2_loc1"] == '2':
        msg = bot.send_message(message.chat.id,
                               'Тебе нужно искать артефакты, что-бы заработать денег. Перед тобой 2 здания.\n '
                               '1)Пойти в общaгу.\n 2)Пойти в лечебницу.',
                               reply_markup=markup)
        data[str(user_id)]["story2_loc2"] = message.text
        data[str(user_id)]["story1_loc2"] = '0'
        save_data(data)

    bot.register_next_step_handler(msg, loc3)


def loc3(message):
    user_id = message.chat.id
    data = load_data()
    msg = None

    if message.text == str(1):
        data[str(user_id)]["story1_loc2"] = message.text
        data[str(user_id)]["story2_loc2"] = '0'
    elif message.text == str(2):
        data[str(user_id)]["story2_loc2"] = message.text
        data[str(user_id)]["story1_loc2"] = '0'
    else:
        data[str(user_id)]["name"] = message.text

    if data[str(user_id)]['story1_loc1'] == '1':
        msg = bot.send_message(message.chat.id,
                               'Вот блин... Ты споткнулся! кажется пластерем не обойтись\n '
                               '1)Позвонить в службу охраны и ждать спасения.\n 2)Держась обеями руками за ногу, идти хромая.',
                               reply_markup=markup)
        data[str(user_id)]["story1_loc3"] = message.text
        data[str(user_id)]["story2_loc3"] = '0'
        save_data(data)

    elif data[str(user_id)]["story2_loc1"] == '2':
        msg = bot.send_message(message.chat.id,
                               'Кто это в комнате? Ауууууууу...  класс! Теперь на тебя бежит псих, с битой!\n '
                               '1)Обороняться.\n 2)! Бежать !',
                               reply_markup=markup)
        data[str(user_id)]["story2_loc3"] = message.text
        data[str(user_id)]["story1_loc3"] = '0'
        save_data(data)

    bot.register_next_step_handler(msg, loc4)


def loc4(message):
    user_id = message.chat.id
    data = load_data()
    msg = None

    if message.text == str(1):
        data[str(user_id)]["story1_loc3"] = message.text
        data[str(user_id)]["story2_loc3"] = '0'
    elif message.text == str(2):
        data[str(user_id)]["story2_loc3"] = message.text
        data[str(user_id)]["story1_loc3"] = '0'
    else:
        data[str(user_id)]["name"] = message.text

    if data[str(user_id)]["story1_loc1"] == '1':
        msg = bot.send_message(message.chat.id,
                               'Никого нет, но тебе удалось выбраться и обойти мутантов. И захватить пару артефактов.\n'
                               '1)Хватит этих вылазок.(Отказаться быть сталкером и уйти от дел.)\n2)Тех артифактов надолго не хватит, нужно снова идти на вылазку.',
                               reply_markup=markup)
        data[str(user_id)]["story1_loc4"] = message.text
        data[str(user_id)]["story2_loc4"] = '0'
    elif data[str(user_id)]["story2_loc1"] == '2':
        if data[str(user_id)]["story2_loc3"] == '1':
            msg = bot.send_message(message.chat.id,
                                   'Неудача! Он был сильнее')
            data[str(user_id)]["story2_loc4"] = '1'
            data[str(user_id)]["story1_loc4"] = '0'
            save_data(data)
            final(message)
        elif data[str(user_id)]["story2_loc3"] == '2':
            msg = bot.send_message(message.chat.id,
                                   'Удача! Тебя спас другой сталкер...\n '
                                   'и cдал ментам!\n Неудача')
            data[str(user_id)]["story2_loc4"] = '2'
            data[str(user_id)]["story1_loc4"] = '0'
            save_data(data)
            final(message)

    save_data(data)
    bot.register_next_step_handler(msg, final)


def final(message):
    user_id = message.chat.id
    data = load_data()

    if message.text == str(1):
        data[str(user_id)]["story1_loc4"] = message.text
        data[str(user_id)]["story2_loc4"] = '0'
    elif message.text == str(2):
        data[str(user_id)]["story2_loc4"] = message.text
        data[str(user_id)]["story1_loc4"] = '0'
    else:
        data[str(user_id)]["name"] = message.text

    data[str(user_id)]["story1_loc4"] = '1'
    if data[str(user_id)]["story1_loc4"] == '1':
        bot.send_message(message.chat.id, "")

    save_data(data)


bot.infinity_polling()
