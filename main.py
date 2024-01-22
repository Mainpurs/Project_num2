import json
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import random as r

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
    msg = (bot.send_message(message.chat.id,
                            'Привет! Ты - охотник за приключениями!\n И ты решил, как и все, не много подзаработать. Ну что? Дозиметр на готове?\nТогда пойдем!'))
    bot.send_message(user_id, 'Ты у себя на базе, но пора продумывать план на миллион! Куда пойдешь?\n '
                              '1)В ОПАСНУЮ зону под названием - Радиус.\n 2)В ИНТЕРЕСНУЮ зону - СССР!',
                     reply_markup=markup)
    data = load_data()
    if str(user_id) not in data:
        data[str(user_id)] = {}
    data[str(user_id)] = {'name': '', 'choice': '', 'choice2': '', 'loc1': '0', 'loc2': '0', 'loc3': '0', 'loc4': '0',
                          'final': '0'}
    save_data(data)  # я добавил story для развых веток.
    bot.register_next_step_handler(msg, loc1)


def loc1(message):
    user_id = message.chat.id
    data = load_data()
    msg = None

    if message.text == str(1):
        data[str(user_id)]["choice"] = '1'
    elif message.text == str(2):
        data[str(user_id)]["choice"] = '2'
    else:
        data[str(user_id)]["x"] = message.text
    save_data(data)

    if data[str(user_id)]["choice"] == '1':
        photo = open('pic/radius.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        msg = bot.send_message(user_id, 'Ты не заметил, как забрёл в минное поле из аномалий! вот неудача!\n '
                                        '1)Идти напролом.\n 2)Сверяться с картой аномалий и идти потихоньку.',
                               reply_markup=markup)
    elif data[str(user_id)]["choice"] == '2':
        photo = open('pic/five.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        msg = bot.send_message(user_id,
                               'Тебе нужно искать артефакты, что-бы заработать денег на жизнь. Перед тобой 2 здания.\n '
                               '1)Пойти в общaгу.\n 2)Пойти в лечебницу.',
                               reply_markup=markup)

    bot.register_next_step_handler(msg, loc2)


def loc2(message):
    user_id = message.chat.id
    data = load_data()
    msg = None

    if message.text == '1':
        data[str(user_id)]["loc1"] = '1'
        save_data(data)
    elif message.text == '2':
        data[str(user_id)]["loc1"] = '2'
        save_data(data)
    else:
        data[str(user_id)]["x"] = message.text
    save_data(data)

    if data[str(user_id)]["choice"] == '1':
        if data[str(user_id)]["loc1"] == '1':
            photo = open('pic/zabludilsy1.png', 'rb')
            bot.send_photo(message.chat.id, photo)
            msg = bot.send_message(user_id, 'Тебе удалось выбежать и не..! но ты заблудился. лес...\n'
                                            '1)Идти наугад.\n 2)Идти наугад',
                                   reply_markup=markup)
        elif data[str(user_id)]["loc1"] == '2':
            photo = open('pic/foot.png', 'rb')
            bot.send_photo(message.chat.id, photo)
            msg = bot.send_message(user_id,
                                   'Вот блин...Невнимательность... Ты споткнулся! кажется пластерем не обойтись\n '
                                   '1)Позвонить в службу спасения и ждать.\n 2)Держась обеями руками '
                                   'за ногу, идти хромая.',
                                   reply_markup=markup)

    elif data[str(user_id)]["choice"] == '2':
        if data[str(user_id)]["loc1"] == '1':
            photo = open('pic/chizee_man.png', 'rb')
            bot.send_photo(message.chat.id, photo)
            msg = bot.send_message(user_id, 'Кто это в комнате? Ауууууууу...  класс! Теперь на тебя бежит псих, '
                                            'с битой!\n '
                                            '1)Обороняться.\n 2)! Бежать !',
                                   reply_markup=markup)
        elif data[str(user_id)]["loc1"] == '2':
            photo = open('pic/gg.png', 'rb')
            bot.send_photo(message.chat.id, photo)
            msg = bot.send_message(user_id,
                                   'Тебя вырубили битой!\n '
                                   '1)Проснуться\n 2)Проснуться',
                                   reply_markup=markup)

    bot.register_next_step_handler(msg, loc3)


def loc3(message):
    user_id = message.chat.id
    data = load_data()
    msg = None

    if data[str(user_id)]["choice"] == '1':
        if message.text == '1':
            data[str(user_id)]["loc2"] = '1'
            save_data(data)
        else:
            data[str(user_id)]["loc2"] = '2'
            save_data(data)
    elif data[str(user_id)]["choice"] == '2':
        if message.text == '1':
            data[str(user_id)]["loc2"] = '3'
            save_data(data)
        else:
            data[str(user_id)]["loc2"] = '4'
            save_data(data)
    else:
        data[str(user_id)]["x"] = message.text
    save_data(data)

    if data[str(user_id)]["choice"] == '1':
        if data[str(user_id)]["loc1"] == '1':
            if data[str(user_id)]["loc2"] == '1':
                x = r.randint(1, 2)
                if x == 1:
                    photo = open('pic/cyberpunk.png', 'rb')
                    bot.send_photo(message.chat.id, photo)
                    msg = bot.send_message(user_id,
                                           'Тебе удалось выбраться на пустырь, но! на тебя напали мусорщики из Cyberpunk 2077\n и ты проиграл.')

                else:
                    photo = open('pic/die.png', 'rb')
                    bot.send_photo(message.chat.id, photo)
                    msg = bot.send_message(user_id,
                                           'Тебе не удалось выбраться, и ты №"%;*?"! от голода.')

            elif data[str(user_id)]["loc2"] == '2':
                x = r.randint(1, 2)
                if x == 1:
                    photo = open('pic/cyberpunk.png', 'rb')
                    bot.send_photo(message.chat.id, photo)
                    msg = bot.send_message(user_id,
                                           'Тебе удалось выбраться на пустырь, но! на тебя напали мусорщики из Cyberpunk 2077\n и ты проиграл.')

                else:
                    photo = open('pic/die.png', 'rb')
                    bot.send_photo(message.chat.id, photo)
                    msg = bot.send_message(user_id,
                                           'Тебе не удалось выбраться, и ты №"%;*?"! от голода.')

        elif data[str(user_id)]["loc1"] == '2':
            if data[str(user_id)]["loc2"] == '1':
                photo = open('pic/die.png', 'rb')
                bot.send_photo(message.chat.id, photo)
                msg = bot.send_message(user_id,
                                       'Наступил вечер, никто так и не пришел. Кроме тех волков\nТы проиграл "запах страха"')
            else:
                x = r.randint(1, 2)
                if x == 1:
                    photo = open('pic/gold.png', 'rb')
                    bot.send_photo(message.chat.id, photo)
                    msg = bot.send_message(user_id,
                                           'Ты нашел в небольшой пещерке дорожайший артефакт, засмотревшись на него,\nты споткнулся и уже не смог встать.  голод\nТы проиграл "деньги не еда""')
                elif x == 2:
                    photo = open('pic/medic.png', 'rb')
                    bot.send_photo(message.chat.id, photo)
                    msg = bot.send_message(user_id,
                                           'Ты нашел в небольшой пещерке целебный артефакт, ты вылечился и тебя встретил другой сталкер\n '
                                           '1)Идти с ним\n 2)Идти на базу',
                                           reply_markup=markup)

    else:
        if data[str(user_id)]["loc1"] == '1':
            if data[str(user_id)]["loc2"] == '3':
                photo = open('pic/die.png', 'rb')
                bot.send_photo(message.chat.id, photo)
                msg = bot.send_message(user_id,
                                       'Он оказался слишком силён!\nТы проиграл "слабость"')
            else:
                photo = open('pic/run2.png', 'rb')
                bot.send_photo(message.chat.id, photo)
                msg = bot.send_message(user_id,
                                       'Он все ещё бежит за тобой!\n '
                                       '1)бежать к оврагу\n 2)бежать к полю',
                                       reply_markup=markup)
        else:
            if data[str(user_id)]["loc2"] == '4':
                photo = open('pic/zabludilsy2.png', 'rb')
                bot.send_photo(message.chat.id, photo)
                msg = bot.send_message(user_id,
                                       'Ты очнулся где-то в лесу.\n '
                                       '1)Бродить по лесу.\n 2)Забраться на дерево, что-бы найти выход.',
                                       reply_markup=markup)
            else:
                photo = open('pic/zabludilsy2.png', 'rb')
                bot.send_photo(message.chat.id, photo)
                msg = bot.send_message(user_id,
                                       'Ты очнулся где-то в лесу.\n '
                                       '1)Бродить по лесу.\n 2)Забраться на дерево, что-бы найти выход.',
                                       reply_markup=markup)

    bot.register_next_step_handler(msg, loc4)


def loc4(message):
    user_id = message.chat.id
    data = load_data()
    msg = None

    if data[str(user_id)]["choice"] == '1':
        if message.text == '1':
            data[str(user_id)]["loc3"] = '1'
            save_data(data)
        else:
            data[str(user_id)]["loc3"] = '2'
            save_data(data)
    elif data[str(user_id)]["choice"] == '2':
        if message.text == '1':
            data[str(user_id)]["loc3"] = '3'
            save_data(data)
        else:
            data[str(user_id)]["loc3"] = '4'
            save_data(data)
    else:
        data[str(user_id)]["x"] = message.text
    save_data(data)

    if data[str(user_id)]["choice"] == '1':
        if data[str(user_id)]["loc1"] == '2':
            if data[str(user_id)]["loc2"] == '2':
                if data[str(user_id)]["loc3"] == '1':
                    photo = open('pic/2stalkers.png', 'rb')
                    bot.send_photo(message.chat.id, photo)
                    msg = bot.send_message(user_id,
                                           'Он был новичком и завел вас в ловушку из аномалий!\n '
                                           '1)Толкнуть его вперед и обезвредить аномалию.\n 2)Прыгнуть всторону.   Авось повезёт.',
                                           reply_markup=markup)

                elif data[str(user_id)]["loc3"] == '2':
                    photo = open('pic/base.png', 'rb')
                    bot.send_photo(message.chat.id, photo)
                    msg = bot.send_message(user_id,
                                           'Глубокой ночью ты подходишь к базе, и тут "башня"! Но ты забыл ответ\nКрикнуть в ответ:\n '
                                           '1)"Молния"\n 2)"Самолёт"',
                                           reply_markup=markup)

    elif data[str(user_id)]["choice"] == '2':
        if data[str(user_id)]["loc1"] == '1':
            if data[str(user_id)]["loc2"] == '4':
                if data[str(user_id)]["loc3"] == '3':
                    photo = open('pic/down2.png', 'rb')
                    bot.send_photo(message.chat.id, photo)
                    msg = bot.send_message(user_id,
                                           'Тебе удалось повалить его и столкнуть в ущелье, но он потянул тебя за рукзак\n '
                                           '1)Ухватиться за кусарник\n 2)Опереться ногой на выступ',
                                           reply_markup=markup)

                elif data[str(user_id)]["loc3"] == '4':
                    photo = open('pic/gg2.png', 'rb')
                    bot.send_photo(message.chat.id, photo)
                    msg = bot.send_message(user_id,
                                           'Ты потерял его извиду\n '
                                           '1)Осмотреться\n 2)Спрятаться в лесу',
                                           reply_markup=markup)

        elif data[str(user_id)]["loc1"] == '2':
            if data[str(user_id)]["loc3"] == '3':
                photo = open('pic/forester.png', 'rb')
                bot.send_photo(message.chat.id, photo)
                msg = bot.send_message(user_id,
                                       'Ты наткнулся на дом. Замученный дорогой ты выбился из сил, и в доме лесника '
                                       'ночлега попросил.\n '
                                       '1)Попросить остаться переждать дождь\n 2)Спросить направление у мужика и отправиться на '
                                       'базу',
                                       reply_markup=markup)
            elif data[str(user_id)]["loc3"] == '4':
                photo = open('pic/die.png', 'rb')
                bot.send_photo(message.chat.id, photo)
                msg = bot.send_message(user_id,
                                       'Из за перчаток, у тебя соскальзнула рука и ты сорвался.\nТы проиграл "не в е з е н и е" ')

    bot.register_next_step_handler(msg, final)


def final(message):
    user_id = message.chat.id
    data = load_data()
    if data[str(user_id)]["choice"] == '1':
        if message.text == '1':
            data[str(user_id)]["loc4"] = '1'
            save_data(data)
        else:
            data[str(user_id)]["loc4"] = '2'
            save_data(data)
    elif data[str(user_id)]["choice"] == '2':
        if message.text == '1':
            data[str(user_id)]["loc4"] = '3'
            save_data(data)
        else:
            data[str(user_id)]["loc4"] = '4'
            save_data(data)
    else:
        data[str(user_id)]["x"] = message.text
    save_data(data)

    if data[str(user_id)]["choice"] == '1':
        if data[str(user_id)]["loc1"] == '2':
            if data[str(user_id)]["loc2"] == '2':
                if data[str(user_id)]["loc3"] == '1':
                    if data[str(user_id)]["loc4"] == '1':
                        photo = open('pic/explose.png', 'rb')
                        bot.send_photo(message.chat.id, photo)
                        msg = bot.send_message(user_id,
                                               'Ты толкаешь, и тут ВЗРЫВ. Тебя тоже задело.\nТы проиграл "карма" ')

                    if data[str(user_id)]["loc4"] == '2':
                        x = r.randint(1, 2)
                        if x == 1:
                            photo = open('pic/explose.png', 'rb')
                            bot.send_photo(message.chat.id, photo)
                            msg = bot.send_message(user_id,
                                           'Ты прыгаешь и задеваешь аномалию...   ВЗРЫВ.\nТы проиграл "друг" ')
                        else:
                            photo = open('pic/explose.png', 'rb')
                            bot.send_photo(message.chat.id, photo)
                            msg = bot.send_message(user_id,
                                                   'Ты прыгаешь и он прыгает за тобой, задевая аномалию и тут ВЗРЫВ. Тебя тоже задело.\nТы проиграл "товарищ" ')

                elif data[str(user_id)]["loc3"] == '2':
                    if data[str(user_id)]["loc4"] == '1':
                        photo = open('pic/base.png', 'rb')
                        bot.send_photo(message.chat.id, photo)
                        msg = bot.send_message(user_id,
                                               'Ты заходишь на базу уже ночью. На утро тебе приходит письмо, о неуплате, и тебя выселяют.\nТы прошел игру. "жизнь" ')
                    elif data[str(user_id)]["loc4"] == '2':
                        photo = open('pic/base.png', 'rb')
                        bot.send_photo(message.chat.id, photo)
                        msg = bot.send_message(user_id,
                                               'Тебя расстреливают на месте.\nТы проиграл "друзья!"')

    if data[str(user_id)]["choice"] == '2':
        if data[str(user_id)]["loc1"] == '1':
            if data[str(user_id)]["loc2"] == '4':
                if data[str(user_id)]["loc3"] == '3':
                    if data[str(user_id)]["loc4"] == '3':
                        photo = open('pic/down.png', 'rb')
                        bot.send_photo(message.chat.id, photo)
                        bot.send_message(user_id,
                                         'Вы повисли, ты держался очень долго, но ведь на тебе еще 20кг снаряги и 70кг мужика.\nТы проиграл "вес ы"')
                    elif data[str(user_id)]["loc4"] == '4':
                        photo = open('pic/down.png', 'rb')
                        bot.send_photo(message.chat.id, photo)
                        bot.send_message(user_id,
                                         'Камень отвалился и кое-кто полетел вниз\nТы проиграл "предатель"')

                if data[str(user_id)]["loc3"] == '4':
                    if data[str(user_id)]["loc4"] == '3':
                        bot.send_message(user_id,
                                         'Ты поворачиваешь голову и тут бам!!\nТы проиграл "бита"')
                    elif data[str(user_id)]["loc4"] == '4':
                        bot.send_message(user_id,
                                         'И он...    Шутка! ты спрятался от него, и сам добрался до города!\nТы прошел жизнь "спасение"')

        if data[str(user_id)]["loc1"] == '1':
            if data[str(user_id)]["loc2"] == '4':
                if data[str(user_id)]["loc3"] == '3':
                    if data[str(user_id)]["loc4"] == '3':
                        bot.send_message(user_id,
                                         'Кажеться тот чай был отравлен.\nТы проиграл "Каннибал"')
                    elif data[str(user_id)]["loc4"] == '3':
                        bot.send_message(user_id,
                                         'Когда ты ушел, он натравил на тебя стаю волков\nТы проиграл "мне уже лень придумывать названия, и меня держат в рабстве, в школе"')




bot.infinity_polling()
