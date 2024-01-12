import json
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "6907816424:AAFtptMbHmk8FH4w39qBW7Zy1533IKPiPEM"
bot = telebot.TeleBot(TOKEN)

markup = ReplyKeyboardMarkup(resize_keyboard=True)
markup.add(KeyboardButton('1'))
markup.add(KeyboardButton('2'))


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
    msg = bot.send_message(message.chat.id, 'Привет! Ты - охотник за приключениями!\n И ты решил, как и все, не много подзаработать. Ну что? Дозиметр на готове?\nТогда пойдем!')
    bot.send_message(message.chat.id, 'Напиши имя персонажа:')
    data = load_data()
    if str(user_id) not in data:
        data[str(user_id)] = {}
    data[str(user_id)] = {'loc1': '', 'loc2': '', 'loc3': '', 'final': ''}
    save_data(data)
    bot.register_next_step_handler(msg, loc1)


def loc1(message):
    user_id = message.chat.id
    msg = bot.send_message(message.chat.id, 'Ты у себя на базе, но пора продумывать план на миллион! Куда пойдешь?\n '
                                            '1)В опасную зону под названием - Радиус.\n 2)В интересную зону - СССР!',
                           reply_markup=markup)
    data = load_data()
    data[str(user_id)]["loc1"] = message.text
    save_data(data)
    bot.register_next_step_handler(msg, loc2)


def loc2(message):
    user_id = message.chat.id
    data = load_data()
    if data[str(user_id)]["loc1"] == '1':
        msg = bot.send_message(message.chat.id,
                               'Кажись ты забрёл в минное поле из аномалий!\n '
                               '1)Бежать напролом!\n 2)Сверяться с картой аномалий и идти потихоньку.',
                               reply_markup=markup)
    elif data[str(user_id)]["loc1"] == '2':
        msg = bot.send_message(message.chat.id,
                               'Тебе нужно искать артефакты. Перед тобой 2 здания.\n '
                               '1)Пойти в общaгу.\n 2)Пойти в лечебницу.',
                               reply_markup=markup)
    data[str(user_id)]["loc2"] = message.text
    save_data(data)
    bot.register_next_step_handler(msg, loc3)


def loc3(message):
    user_id = message.chat.id
    msg = bot.send_message(message.chat.id, 'Ты у себя на базе, но пора продумывать план на миллион! Куда пойдешь?\n '
                                            '1)В опасную зону под названием - Радиус.\n 2)В интересную зону - СССР!',
                           reply_markup=markup)
    data = load_data()
    data[str(user_id)]["loc3"] = message.text
    save_data(data)
    bot.register_next_step_handler(msg, final)


def final(message):
    user_id = message.chat.id
    msg = bot.send_message(message.chat.id, 'Ты у себя на базе, но пора продумывать план на миллион! Куда пойдешь?\n '
                                            '1)В опасную зону под названием - Радиус.\n 2)В интересную зону - СССР!',
                           reply_markup=markup)
    data = load_data()
    data[str(user_id)]["final"] = message.text
    save_data(data)
    bot.register_next_step_handler(msg, loc1)


if __name__ == "__main__":
    bot.polling(none_stop=True)
