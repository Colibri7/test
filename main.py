import crypt
import datetime
import time
from threading import Thread
import schedule
from datetime import datetime
import telebot
from telebot import types
import pymysql

bot = telebot.TeleBot('1241604248:AAH8khnkopYJPhlvplSPOriYHNStmWHzBuc', threaded=False)


SQLALCHEMY_ENGINE_OPTIONS = {
    "pool_pre_ping": True,
    "pool_recycle": 300,
}

def domen_60_days_schedule():
    connection = pymysql.connect(host='62.209.143.131',
                                 user='hostmasteruz_pbot',
                                 password='bcaxoZyAXDGc',
                                 database='hostmasteruz_base',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor
                                 )
    min = connection.cursor()
    min.execute(
        "SELECT `tg_id`, `idmydomain`, `mydomain`.userid, `mydomainname`, NOW() as now_datetime, `expired`,`contactname`, `contactcompany` FROM `hostmasteruz_base`.`mydomain`, `hostmasteruz_bot`.`sardorbot`,`hostmasteruz_base`.`contact`  WHERE DATE(`expired`) = DATE(DATE_ADD(NOW(),INTERVAL 60 DAY)) AND `sardorbot`.`b_userid` = `mydomain`.`userid` AND `mydomain`.`mydomaincontactcust` = `contact`.`idcontact`;")
    domen = min.fetchall()

    for i in domen:
        date = '{:%d-%m-%Y}'.format(i["expired"])
        some_id = i["tg_id"]
        print('id ', some_id)
        if i["contactcompany"] == None:
            bot.send_message(some_id,
                             f'Уважаемый <b>{i["contactname"]}!</b> Уведомляем Вас о том, '
                             f'что срок действия домена <b>{i["mydomainname"]}.uz</b> истекает <b>{date}</b> '
                             f'года . Для продления регистрации домена Вам необходимо оплатить '
                             f'сумму согласно действующим тарифам на нашем сайте. '
                             f'В случае неоплаты, ваш домен будет свободен для регистрации другим '
                             f'лицом.\n<b>С уважением, команда Hostmaster!</b>',
                             parse_mode='html')

        else:
            bot.send_message(some_id,
                             f'Уважаемый <b>{i["contactcompany"]}!</b> Уведомляем Вас о том, '
                             f'что срок действия домена <b>{i["mydomainname"]}.uz</b> истекает <b>{date}</b> '
                             f'года . Для продления регистрации домена Вам необходимо оплатить '
                             f'сумму согласно действующим тарифам на нашем сайте. '
                             f'В случае неоплаты, ваш домен будет свободен для регистрации другим '
                             f'лицом.\n<b>С уважением, команда Hostmaster!</b>',
                             parse_mode='html')

    min.close()


def domen_30_days_schedule():
    connection = pymysql.connect(host='62.209.143.131',
                                 user='hostmasteruz_pbot',
                                 password='bcaxoZyAXDGc',
                                 database='hostmasteruz_base',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor
                                 )
    min = connection.cursor()
    min.execute(
        "SELECT `tg_id`, `idmydomain`, `mydomain`.userid, "
        "`mydomainname`, NOW() as now_datetime, `expired`,"
        "`contactname`, `contactcompany` FROM "
        "`hostmasteruz_base`.`mydomain`, `hostmasteruz_bot`.`sardorbot`,"
        "`hostmasteruz_base`.`contact`  WHERE DATE(`expired`) ="
        " DATE(DATE_ADD(NOW(),INTERVAL 30 DAY)) AND"
        " `sardorbot`.`b_userid` = `mydomain`.`userid` "
        "AND `mydomain`.`mydomaincontactcust` = `contact`.`idcontact`;")
    domen_30 = min.fetchall()

    for i in domen_30:
        date = '{:%d-%m-%Y}'.format(i["expired"])
        some_id = i["tg_id"]
        print('id ', some_id)
        if i["contactcompany"] is None:

            bot.send_message(some_id, f'Уважаемый <b>{i["contactname"]}!</b> Уведомляем Вас о том, '
                                      f'что срок действия домена <b>{i["mydomainname"]}.uz</b> '
                                      f'истекает <b>{date}</b> '
                                      f'года . Для продления регистрации домена Вам необходимо оплатить '
                                      f'сумму согласно действующим тарифам на нашем сайте. '
                                      f'В случае неоплаты, ваш домен будет свободен для регистрации другим '
                                      f'лицом.\n<b>С уважением, команда Hostmaster!</b>', parse_mode='html')
        else:
            bot.send_message(some_id, f'Уважаемый <b>{i["contactcompany"]}!</b> Уведомляем Вас о том, '
                                      f'что срок действия домена <b>{i["mydomainname"]}.uz</b> '
                                      f'истекает <b>{date}</b> '
                                      f'года . Для продления регистрации домена Вам необходимо оплатить '
                                      f'сумму согласно действующим тарифам на нашем сайте. '
                                      f'В случае неоплаты, ваш домен будет свободен для регистрации другим '
                                      f'лицом.\n<b>С уважением, команда Hostmaster!</b>', parse_mode='html')

    min.close()


def domen_10_days_schedule():
    day_of_month = datetime.now().day
    print(day_of_month)
    if day_of_month == 28:

        connection = pymysql.connect(host='62.209.143.131',
                                     user='hostmasteruz_pbot',
                                     password='bcaxoZyAXDGc',
                                     database='hostmasteruz_base',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor
                                     )
        min = connection.cursor()
        min.execute(
            "SELECT `tg_id`, `idmydomain`, `mydomain`.userid, "
            "`mydomainname`, NOW() as now_datetime, `expired`,"
            "`contactname`, `contactcompany` FROM"
            " `hostmasteruz_base`.`mydomain`,"
            " `hostmasteruz_bot`.`sardorbot`,"
            "`hostmasteruz_base`.`contact`  "
            "WHERE DATE(`expired`) = DATE(DATE_ADD(NOW(),INTERVAL 10 DAY))"
            " AND `sardorbot`.`b_userid` = `mydomain`.`userid`"
            " AND `mydomain`.`mydomaincontactcust` = `contact`.`idcontact`;")
        domen_30 = min.fetchall()

        for i in domen_30:
            date = '{:%d-%m-%Y}'.format(i["expired"])
            some_id = i["tg_id"]
            print('id ', some_id)
            if i["contactcompany"] is None:

                bot.send_message(some_id, f'Уважаемый <b>{i["contactname"]}!</b> Уведомляем Вас о том, '
                                          f'что срок действия домена <b>{i["mydomainname"]}.uz</b> '
                                          f'истекает <b>{date}</b> '
                                          f'года . Для продления регистрации домена Вам необходимо оплатить '
                                          f'сумму согласно действующим тарифам на нашем сайте. '
                                          f'В случае неоплаты, ваш домен будет свободен для регистрации другим '
                                          f'лицом.\n<b>С уважением, команда Hostmaster!</b>', parse_mode='html')
            else:
                bot.send_message(some_id, f'Уважаемый <b>{i["contactcompany"]}!</b> Уведомляем Вас о том, '
                                          f'что срок действия домена <b>{i["mydomainname"]}.uz</b> '
                                          f'истекает <b>{date}</b> '
                                          f'года . Для продления регистрации домена Вам необходимо оплатить '
                                          f'сумму согласно действующим тарифам на нашем сайте. '
                                          f'В случае неоплаты, ваш домен будет свободен для регистрации другим '
                                          f'лицом.\n<b>С уважением, команда Hostmaster!</b>', parse_mode='html')
        min.close()


def domen_1_days_schedule():
    connection = pymysql.connect(host='62.209.143.131',
                                 user='hostmasteruz_pbot',
                                 password='bcaxoZyAXDGc',
                                 database='hostmasteruz_base',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor
                                 )
    min = connection.cursor()
    min.execute(
        "SELECT `tg_id`, `idmydomain`, `mydomain`.userid,"
        " `mydomainname`, NOW() as now_datetime, "
        "`expired`,`contactname`, `contactcompany`"
        " FROM `hostmasteruz_base`.`mydomain`, "
        "`hostmasteruz_bot`.`sardorbot`,`hostmasteruz_base`.`contact` "
        " WHERE DATE(expired) = DATE(NOW()) AND "
        "`sardorbot`.`b_userid` = `mydomain`.`userid`"
        " AND `mydomain`.`mydomaincontactcust` = `contact`.`idcontact`;")
    domen_1 = min.fetchall()

    for i in domen_1:
        date = '{:%d-%m-%Y}'.format(i["expired"])
        some_id = i["tg_id"]
        print('id ', some_id)
        if i["contactcompany"] is None:
            bot.send_message(some_id, f'Уважаемый <b>{i["contactname"]}!</b> Уведомляем Вас о том, '
                                      f'что срок действия домена <b>{i["mydomainname"]}.uz</b> '
                                      f'истек сегодня, <b>{date}</b> года. Для продления регистрации '
                                      f'домена Вам необходимо оплатить сумму согласно действующим '
                                      f'тарифам на нашем сайте. '
                                      f'В случае неоплаты, ваш домен будет свободен для '
                                      f'регистрации другим лицом.\n<b>С уважением, команда Hostmaster!</b>',
                             parse_mode='html')
        else:
            bot.send_message(some_id, f'Уважаемый <b>{i["contactcompany"]}!</b> Уведомляем Вас о том, '
                                      f'что срок действия домена <b>{i["mydomainname"]}.uz</b> '
                                      f'истек сегодня, <b>{date}</b> года. Для продления регистрации '
                                      f'домена Вам необходимо оплатить сумму согласно действующим '
                                      f'тарифам на нашем сайте. '
                                      f'В случае неоплаты, ваш домен будет свободен для '
                                      f'регистрации другим лицом.\n<b>С уважением, команда Hostmaster!</b>',
                             parse_mode='html')
    min.close()


def func(message):
    if message.text == 'Возврат 🔙':
        markup = types.InlineKeyboardMarkup(row_width=2)
        lg1 = types.InlineKeyboardButton('Мои услуги 📊', callback_data='my_services')
        lg2 = types.InlineKeyboardButton('Мои контакты 📋', callback_data='my_contacts')
        lg3 = types.InlineKeyboardButton('Авторизация 🔐', callback_data='cabinet')
        lg4 = types.InlineKeyboardButton('Связь с менеджером 👨🏻‍💻',
                                         callback_data='connect_admin', url='https://t.me/hostmaster_support')
        lg5 = types.InlineKeyboardButton('Зарегистрироваться 📝', callback_data='site',
                                         url='https://hostmaster.uz/site/signup')
        lg6 = types.InlineKeyboardButton('Настройки 🛠', callback_data='settings')

        markup.add(lg1, lg2, lg3, lg4, lg5, lg6)
        bot.send_message(message.chat.id,
                         "Вас приветствует бот компании <b>Hostmaster</b>.\nХостинг, VDS, серверы, домены  в Узбекистане, в Ташкенте.\n\n",
                         reply_markup=markup, parse_mode='html')


    elif message.text == 'Bosh sahifa':
        markup_uz = types.InlineKeyboardMarkup(row_width=2)
        lg1 = types.InlineKeyboardButton('Mening xizmatlarim 📊', callback_data='xizmatlarim')
        lg2 = types.InlineKeyboardButton('Mening kontaktlarim 📋', callback_data='kontaktlarim')
        lg3 = types.InlineKeyboardButton("Kirish 🔐", callback_data="ro'yxatdan_o'tish")
        lg4 = types.InlineKeyboardButton("Menejer bilan aloqa 👨🏻‍💻", callback_data="connect_admin",
                                         url='https://t.me/hostmaster_support')
        lg5 = types.InlineKeyboardButton("Roʻyxatdan o'tish 📝", callback_data="site",
                                         url='https://hostmaster.uz/site/signup')
        lg6 = types.InlineKeyboardButton('Sozlamalar 🛠', callback_data='sozlamalar')
        markup_uz.add(lg1, lg2, lg3, lg4, lg5, lg6)
        bot.send_message(message.chat.id,
                         "<b>Hostmaster</b> botiga xush kelibsiz.\nXosting, VDS, serverlar, domenlar O'zbekistonda, Toshkentda.\n\n",
                         reply_markup=markup_uz, parse_mode='html')


# Start bot
@bot.message_handler(commands=['start', 'menu'])
def send_welcome(message):
    text = f'Bot in action:\nname: <b>{message.from_user.first_name}</b>\n' \
           f'chat_id: <b>{message.chat.id}</b>\n' \
           f'username: <b>@{message.from_user.username}</b>'

    markup = types.InlineKeyboardMarkup(row_width=2)
    lg1 = types.InlineKeyboardButton('Мои услуги 📊', callback_data='my_services')
    lg2 = types.InlineKeyboardButton('Мои контакты 📋', callback_data='my_contacts')
    lg3 = types.InlineKeyboardButton('Авторизация 🔐', callback_data='cabinet')
    lg4 = types.InlineKeyboardButton('Связь с менеджером 👨🏻‍💻', callback_data='connect_admin',
                                     url='https://t.me/hostmaster_support')
    lg5 = types.InlineKeyboardButton('Зарегистрироваться 📝', callback_data='site',
                                     url='https://hostmaster.uz/site/signup')
    lg6 = types.InlineKeyboardButton('Настройки 🛠', callback_data='settings')

    markup.add(lg1, lg2, lg3, lg4, lg5, lg6)
    bot.send_message(message.chat.id,
                     "Вас приветствует бот компании <b>Hostmaster</b>.\nХостинг, VDS, серверы, домены  в Узбекистане, в Ташкенте.\n\n",
                     reply_markup=markup, parse_mode='html')
    bot.send_message(332749197, text, parse_mode='html')


@bot.message_handler(content_types=['text'])
def log(message):
    def password(message):
        def after_login(message):
            def uslugi(message):
                if message.text == 'Мои хостинги 🗂':
                    for i in check:
                        id = i["id"]
                        id_connect = connection.cursor()
                        id_connect.execute(
                            "select hostcontractdomain,cptariff, status from hostcontract where user_id=%(user_id)s and status = 1 union select hostcontractdomain,cptariff, status from hostcontract where user_id=%(user_id)s and status = 0 union select hostcontractdomain,cptariff, status from hostcontract where user_id=%(user_id)s and status = 2",
                            {'user_id': id})
                        checkContact = id_connect.fetchall()
                        num = 1
                        host_text = ''
                        if checkContact:
                            for i in checkContact:
                                if i["status"] == 1:
                                    i["status"] = 'Active ✅'
                                elif i["status"] == 0:
                                    i["status"] = 'Block 🚫'
                                else:
                                    i["status"] = 'Deleted ❌'
                                if i["status"] == 'Deleted ❌' or i["status"] == 'Block 🚫':
                                    host_text += f'{num}. {i["hostcontractdomain"]}, ' \
                                                 f'{i["status"]}\n'
                                else:
                                    host_text += f'{num}. {i["hostcontractdomain"]}, ' \
                                                 f'{i["status"]}, <b>{i["cptariff"]}</b>\n'
                                num += 1
                            bot.send_message(message.chat.id, host_text, parse_mode='html')
                        else:
                            bot.send_message(message.chat.id, "У вас нет услуги аренды хостингов 🤷🏻")

                    bot.register_next_step_handler(message, uslugi)
                elif message.text == 'Мои домены 🔠':
                    for i in check:
                        id = i["id"]
                        id_connect = connection.cursor()
                        id_connect.execute(
                            'SELECT * ,NOW() as now_datetime FROM mydomain WHERE status IN (-2,0,1,3) and userid=%(userid)s ORDER BY expired ASC',
                            {'userid': id})
                        checkContact = id_connect.fetchall()
                        num = 1
                        domen_text = ''
                        if checkContact:
                            for i in checkContact:
                                delta = i["now_datetime"] - i["expired"]
                                if delta.days > 0:
                                    i["expired"] = '{:%d-%m-%-y}'.format(i["expired"])
                                else:
                                    i["expired"] = '{:%d-%m-%-y}'.format(i["expired"])
                                if i["status"] == -2:
                                    i["status"] = 'A_REG'
                                elif i["status"] == 0:
                                    i["status"] = 'R_REG'
                                elif i["status"] == 1:
                                    i["status"] = 'Active ✅'
                                elif i["status"] == 3:
                                    i["status"] = 'W_RED ⚠️'
                                domen_text += f'{num}. {i["mydomainname"]}.uz, ' \
                                              f'{i["status"]}, {i["expired"]}\n'
                                num += 1
                            if len(domen_text) > 4096:
                                for x in range(0, len(domen_text), 4096):
                                    bot.send_message(message.chat.id, '{}'.format(domen_text[x:x + 4096]))
                                bot.register_next_step_handler(message, uslugi)
                            bot.send_message(message.chat.id, domen_text, parse_mode='html')
                        else:
                            bot.send_message(message.chat.id, 'У вас нет доменов 🤷🏻')
                    bot.register_next_step_handler(message, uslugi)
                elif message.text == 'Мои VDS 🗄':
                    for i in check:
                        id = i["id"]
                        id_connect = connection.cursor()
                        id_connect.execute(
                            'SELECT `vdscontract`.`vdshostname`,'
                            ' `vds_tariffs`.`tariffname` ,'
                            '`vdscontract`.`status`  FROM '
                            '`user`, `vdscontract`, `vds_tariffs`'
                            ' WHERE   username=%(username)s AND '
                            '`user`.`id` = `vdscontract`.`user_id`'
                            ' AND `vdscontract`.`vdsid` = `vds_tariffs`.`idvds`'
                            ' ORDER BY vdscontract.status = 1 DESC;',
                            {'username': login})
                        checkContact = id_connect.fetchall()
                        num = 1
                        vds_text = ''
                        if checkContact:
                            for i in checkContact:
                                if i["status"] == 1:
                                    i["status"] = 'Active ✅'
                                elif i["status"] == 0:
                                    i["status"] = 'Block 🚫'
                                else:
                                    i["status"] = 'Deleted ❌'
                                if i["status"] == 'Deleted ❌' or i["status"] == 'Block 🚫':
                                    vds_text += f'{num}. {i["vdshostname"]}, {i["status"]}\n'
                                else:
                                    vds_text += f'{num}. {i["vdshostname"]}, {i["tariffname"]}, {i["status"]}\n'
                                num += 1
                            bot.send_message(message.chat.id, vds_text, parse_mode='html')
                        else:
                            bot.send_message(message.chat.id, 'У вас нет услуги аренды VDS 🤷🏻')

                    bot.register_next_step_handler(message, uslugi)
                elif message.text == 'Мои сервера 💾':
                    for i in check:
                        print(i)
                        id = i["id"]
                        id_connect = connection.cursor()
                        id_connect.execute(
                            "SELECT * FROM colcontract WHERE user_id=%(user_id)s", {'user_id': id})
                        checkContact = id_connect.fetchall()
                        num = 1
                        ser_text = ''
                        if checkContact:

                            for i in checkContact:
                                if i["status"] == 1:
                                    i["status"] = 'Active ✅'
                                elif i["status"] == 2:
                                    i["status"] = 'Block 🚫'
                                ser_text += f'{num}. <b>{i["colhostname"]}</b>, <b>{i["status"]}</b>\n'
                                num += 1
                            bot.send_message(message.chat.id, ser_text, parse_mode='html')
                        else:
                            bot.send_message(message.chat.id, 'У вас нет услуги аренды сервера 🤷🏻')

                    bot.register_next_step_handler(message, uslugi)
                elif message.text == 'Возврат 🔙':
                    markup_ru = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
                    lg1 = types.KeyboardButton('Мои услуги 📊')
                    lg2 = types.KeyboardButton('Мои контакты 📋')
                    lg3 = types.KeyboardButton('Уведомления')
                    lg4 = types.KeyboardButton('Возврат 🔙')
                    markup_ru.add(lg1, lg2, lg3, lg4)
                    bot.send_message(message.chat.id, 'Возврат 🔙', reply_markup=markup_ru, parse_mode='html')
                    bot.register_next_step_handler(message, after_login)

            def doljniki(message):
                def doljniki_domen(message):
                    if message.text == '60 дней':
                        connection = pymysql.connect(host='62.209.143.131',
                                                     user='hostmasteruz_pbot',
                                                     password='bcaxoZyAXDGc',
                                                     database='hostmasteruz_base',
                                                     charset='utf8mb4',
                                                     cursorclass=pymysql.cursors.DictCursor
                                                     )
                        min = connection.cursor()
                        min.execute(
                            "SELECT `idmydomain`, `userid`, `mydomainname`, NOW() as now_datetime, `expired` FROM `mydomain` WHERE DATE(`expired`) = DATE(DATE_ADD(NOW(),INTERVAL 60 DAY))")
                        domendays_60 = min.fetchall()
                        if not domendays_60:
                            bot.send_message(message.chat.id, 'Сегодня должников нет')
                        else:
                            days_60 = ''
                            n = 1
                            for i in domendays_60:
                                days_60 += f'{n}. {i["mydomainname"]}.uz\n'
                                n += 1
                            print(days_60)
                            bot.send_message(message.chat.id, days_60)
                        min.close()
                        bot.register_next_step_handler(message, doljniki_domen)
                    elif message.text == '30 дней':
                        connection = pymysql.connect(host='62.209.143.131',
                                                     user='hostmasteruz_pbot',
                                                     password='bcaxoZyAXDGc',
                                                     database='hostmasteruz_base',
                                                     charset='utf8mb4',
                                                     cursorclass=pymysql.cursors.DictCursor
                                                     )
                        min = connection.cursor()
                        min.execute(
                            "SELECT `idmydomain`, `userid`, `mydomainname`, "
                            "NOW() as now_datetime, `expired` "
                            "FROM `mydomain` WHERE "
                            "DATE(`expired`) = DATE(DATE_ADD(NOW(),INTERVAL 30 DAY))")
                        domendays_30 = min.fetchall()
                        if not domendays_30:
                            bot.send_message(message.chat.id, 'Сегодня должников нет')
                        else:
                            days_30 = ''
                            n = 1
                            for i in domendays_30:
                                days_30 += f'{n}. {i["mydomainname"]}.uz\n'
                                n += 1
                            print(days_30)
                            bot.send_message(message.chat.id, days_30)
                        min.close()
                        bot.register_next_step_handler(message, doljniki_domen)
                    elif message.text == '10 дней':
                        connection = pymysql.connect(host='62.209.143.131',
                                                     user='hostmasteruz_pbot',
                                                     password='bcaxoZyAXDGc',
                                                     database='hostmasteruz_base',
                                                     charset='utf8mb4',
                                                     cursorclass=pymysql.cursors.DictCursor
                                                     )
                        min = connection.cursor()
                        min.execute(
                            "SELECT `idmydomain`, `userid`, "
                            "`mydomainname`, NOW() as now_datetime, "
                            "`expired` FROM `mydomain` "
                            "WHERE DATE(`expired`) = DATE(DATE_ADD(NOW(),INTERVAL 10 DAY))")
                        domendays_10 = min.fetchall()
                        if not domendays_10:
                            bot.send_message(message.chat.id, 'Сегодня должников нет')
                        else:
                            days_10 = ''
                            n = 1
                            for i in domendays_10:
                                days_10 += f'{n}. {i["mydomainname"]}.uz\n'
                                n += 1
                            print(days_10)
                            bot.send_message(message.chat.id, days_10)
                        min.close()
                        bot.register_next_step_handler(message, doljniki_domen)
                    elif message.text == 'Сегодня':
                        connection = pymysql.connect(host='62.209.143.131',
                                                     user='hostmasteruz_pbot',
                                                     password='bcaxoZyAXDGc',
                                                     database='hostmasteruz_base',
                                                     charset='utf8mb4',
                                                     cursorclass=pymysql.cursors.DictCursor
                                                     )
                        min = connection.cursor()
                        min.execute(
                            "SELECT `idmydomain`, `userid`,"
                            " `mydomainname`, NOW() as now_datetime, "
                            "`expired` FROM `mydomain` "
                            "WHERE DATE(`expired`) = DATE(NOW())")
                        domendays_1 = min.fetchall()
                        if not domendays_1:
                            bot.send_message(message.chat.id, 'Сегодня должников нет')
                        else:
                            days_1 = ''
                            n = 1
                            for i in domendays_1:
                                days_1 += f'{n}. {i["mydomainname"]}.uz\n'
                                n += 1
                            print(days_1)
                            bot.send_message(message.chat.id, days_1)
                        min.close()
                        bot.register_next_step_handler(message, doljniki_domen)
                    elif message.text == 'Redemption':
                        connection = pymysql.connect(host='62.209.143.131',
                                                     user='hostmasteruz_pbot',
                                                     password='bcaxoZyAXDGc',
                                                     database='hostmasteruz_base',
                                                     charset='utf8mb4',
                                                     cursorclass=pymysql.cursors.DictCursor
                                                     )
                        min = connection.cursor()
                        min.execute(
                            "SELECT `idmydomain`, `userid`, "
                            "`mydomainname`, NOW() as now_datetime,"
                            " `expired` FROM `mydomain` WHERE status=3")
                        redemption = min.fetchall()
                        red = ''
                        n = 1
                        for i in redemption:
                            red += f'{n}. {i["mydomainname"]}.uz\n'
                            n += 1
                        print(red)
                        bot.send_message(message.chat.id, red)
                        min.close()
                        bot.register_next_step_handler(message, doljniki_domen)
                    elif message.text == 'Назад':
                        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
                        lg1 = types.KeyboardButton('Домен')
                        # lg2 = types.KeyboardButton('Хостинг')
                        # lg3 = types.KeyboardButton('VDS')
                        lg4 = types.KeyboardButton('Возврат 🔙')
                        markup.add(lg1, lg4)
                        bot.send_message(message.chat.id, 'Уведомления', reply_markup=markup)
                        bot.register_next_step_handler(message, doljniki)

                if message.text == 'Домен':
                    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
                    lg1 = types.KeyboardButton('60 дней')
                    lg2 = types.KeyboardButton('30 дней')
                    lg3 = types.KeyboardButton('10 дней')
                    lg4 = types.KeyboardButton('Сегодня')
                    lg5 = types.KeyboardButton('Redemption')
                    lg6 = types.KeyboardButton('Назад')
                    markup.add(lg1, lg2, lg3, lg4, lg5, lg6)
                    bot.send_message(message.chat.id, 'Уведомления Доменов', reply_markup=markup)
                    bot.register_next_step_handler(message, doljniki_domen)

                elif message.text == 'Возврат 🔙':
                    markup_ru = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
                    lg1 = types.KeyboardButton('Мои услуги 📊')
                    lg2 = types.KeyboardButton('Мои контакты 📋')
                    lg3 = types.KeyboardButton('Уведомления')
                    lg4 = types.KeyboardButton('Возврат 🔙')
                    markup_ru.add(lg1, lg2, lg3, lg4)
                    bot.send_message(message.chat.id, 'Возврат 🔙', reply_markup=markup_ru)
                bot.register_next_step_handler(message, after_login)

            if message.text == 'Мои контакты 📋':
                for i in check:
                    id = i["id"]
                    id_connect = connection.cursor()
                    id_connect.execute(
                        'SELECT * FROM contact WHERE userid=%(userid)s', {'userid': id})
                    checkContact = id_connect.fetchall()
                    text = ''
                    num = 1
                    for i in checkContact:
                        if i["contactcompany"] is None:
                            text += f'{num}. {i["contactname"]}\nБаланс: <b>{i["balance"]} сум 💰</b>\n'
                        else:
                            text += f'{num}. {i["contactcompany"]}\nБаланс: <b>{i["balance"]} сум 💰</b>\n'
                        num += 1
                    bot.send_message(message.chat.id, text, parse_mode='html')
                bot.register_next_step_handler(message, after_login)
            elif message.text == 'Мои услуги 📊':
                markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
                lg1 = types.KeyboardButton('Мои хостинги 🗂')
                lg2 = types.KeyboardButton('Мои домены 🔠')
                lg3 = types.KeyboardButton('Мои VDS 🗄')
                lg4 = types.KeyboardButton('Мои сервера 💾')
                lg5 = types.KeyboardButton('Возврат 🔙')
                markup.add(lg1, lg2, lg3, lg4, lg5)
                bot.send_message(message.chat.id, 'Мои услуги 📊', reply_markup=markup)
                bot.register_next_step_handler(message, uslugi)
            elif message.text == 'Уведомления':
                markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
                lg1 = types.KeyboardButton('Домен')
                lg4 = types.KeyboardButton('Возврат 🔙')
                # lg2 = types.KeyboardButton('Хостинг')
                # lg3 = types.KeyboardButton('VDS')
                markup.add(lg1, lg4)
                bot.send_message(message.chat.id, 'Уведомления', reply_markup=markup)
                bot.register_next_step_handler(message, doljniki)
            elif message.text == 'Возврат 🔙':
                markup = types.InlineKeyboardMarkup(row_width=2)
                lg1 = types.InlineKeyboardButton('Мои услуги 📊', callback_data='my_services')
                lg2 = types.InlineKeyboardButton('Мои контакты 📋', callback_data='my_contacts')
                lg3 = types.InlineKeyboardButton('Авторизация 🔐', callback_data='cabinet')
                lg4 = types.InlineKeyboardButton('Связь с менеджером 👨🏻‍💻', callback_data='connect_admin',
                                                 url='https://t.me/hostmaster_support')
                lg5 = types.InlineKeyboardButton('Зарегистрироваться 📝', callback_data='site',
                                                 url='https://hostmaster.uz/site/signup')
                lg6 = types.InlineKeyboardButton('Настройки 🛠', callback_data='settings')

                markup.add(lg1, lg2, lg3, lg4, lg5, lg6)
                bot.send_message(message.chat.id,
                                 "Вас приветствует бот компании <b>Hostmaster</b>.\nХостинг, VDS, серверы, домены  в Узбекистане, в Ташкенте.\n\n",
                                 reply_markup=markup, parse_mode='html')

        if message.text == 'sardor':
            connection = pymysql.connect(host='62.209.143.131',
                                         user='hostmasteruz_pbot',
                                         password='bcaxoZyAXDGc',
                                         database='hostmasteruz_base',
                                         charset='utf8mb4',
                                         cursorclass=pymysql.cursors.DictCursor
                                         )
            min = connection.cursor()
            min.execute(
                'SELECT id,password_hash FROM user WHERE username=%(username)s', {'username': login})

            check = min.fetchall()

            markup_ru = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
            lg1 = types.KeyboardButton('Мои услуги 📊')
            lg2 = types.KeyboardButton('Мои контакты 📋')
            lg3 = types.KeyboardButton('Уведомления')
            lg4 = types.KeyboardButton('Возврат 🔙')
            markup_ru.add(lg1, lg2, lg3, lg4)
            bot.send_message(message.chat.id,
                             "Вы вошли под админом",
                             reply_markup=markup_ru, parse_mode='html')
            bot.send_message(332749197,
                             f'{message.from_user.first_name} Successfully authorized for admin')

            min.close()
            bot.register_next_step_handler(message, after_login)
        else:
            out = crypt.crypt(message.text, checkUsername["password_hash"])

            connection = pymysql.connect(host='62.209.143.131',
                                         user='hostmasteruz_pbot',
                                         password='bcaxoZyAXDGc',
                                         database='hostmasteruz_base',
                                         charset='utf8mb4',
                                         cursorclass=pymysql.cursors.DictCursor
                                         )
            if checkUsername["password_hash"] == out:

                min = connection.cursor()
                min.execute(
                    'SELECT id,password_hash FROM user WHERE username=%(username)s', {'username': login})

                check = min.fetchall()
                markup = types.InlineKeyboardMarkup(row_width=2)
                lg1 = types.InlineKeyboardButton('Мои услуги 📊', callback_data='my_services')
                lg2 = types.InlineKeyboardButton('Мои контакты 📋', callback_data='my_contacts')
                lg3 = types.InlineKeyboardButton('Авторизация 🔐', callback_data='cabinet')
                lg4 = types.InlineKeyboardButton('Связь с менеджером 👨🏻‍💻', callback_data='connect_admin',
                                                 url='https://t.me/hostmaster_support')
                lg5 = types.InlineKeyboardButton('Зарегистрироваться 📝', callback_data='site',
                                                 url='https://hostmaster.uz/site/signup')
                lg6 = types.InlineKeyboardButton('Настройки 🛠', callback_data='settings')

                markup.add(lg1, lg2, lg3, lg4, lg5, lg6)
                bot_con = pymysql.connect(host='62.209.143.131',
                                          user='hostmasteruz_pbot',
                                          password='bcaxoZyAXDGc',
                                          database='hostmasteruz_bot',
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor
                                          )

                min = connection.cursor()
                min.execute(
                    'SELECT `user`.`id`  FROM `user` WHERE username=%(username)s', {'username': login})
                check = min.fetchall()
                for i in check:
                    id = i["id"]

                    cursor = bot_con.cursor()
                    query = "INSERT INTO `sardorbot` (`tg_id`, `tg_username`, `tg_first_name`," \
                            " `tg_last_name`, `updated`,`b_username`,`b_userid`) " \
                            "VALUES ({0},'{1}','{2}','{3}','{4}','{5}','{6}') " \
                            "ON DUPLICATE KEY UPDATE `tg_username` = '{1}'," \
                            " `tg_first_name` = '{2}', `tg_last_name` = '{3}', " \
                            "`updated` = '{4}',`b_username`='{5}',`b_userid`='{6}'".format(
                        chat_id, username, first_name, last_name, dt_obj, login, id)
                    cursor.execute(query)
                bot.send_message(message.chat.id,
                                 "Вас приветствует бот компании <b>Hostmaster</b>.\nХостинг, VDS, серверы, домены  в Узбекистане, в Ташкенте.\n\n",
                                 reply_markup=markup, parse_mode='html')
                bot.send_message(332749197,
                                 f'{message.from_user.first_name} Successfully authorized')
                bot_con.close()
                min.close()
            elif message.text == 'Возврат 🔙':
                markup = types.InlineKeyboardMarkup(row_width=2)
                lg1 = types.InlineKeyboardButton('Мои услуги 📊', callback_data='my_services')
                lg2 = types.InlineKeyboardButton('Мои контакты 📋', callback_data='my_contacts')
                lg3 = types.InlineKeyboardButton('Авторизация 🔐', callback_data='cabinet')
                lg4 = types.InlineKeyboardButton('Связь с менеджером 👨🏻‍💻', callback_data='connect_admin',
                                                 url='https://t.me/hostmaster_support')
                lg5 = types.InlineKeyboardButton('Зарегистрироваться 📝', callback_data='site',
                                                 url='https://hostmaster.uz/site/signup')
                lg6 = types.InlineKeyboardButton('Настройки 🛠', callback_data='settings')

                markup.add(lg1, lg2, lg3, lg4, lg5, lg6)
                bot.send_message(message.chat.id,
                                 "Вас приветствует бот компании <b>Hostmaster</b>.\nХостинг, VDS, серверы, домены  в Узбекистане, в Ташкенте.\n\n",
                                 reply_markup=markup, parse_mode='html')

            else:
                key = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
                lg1 = types.KeyboardButton("Возврат 🔙")
                key.add(lg1)
                bot.send_message(message.chat.id, 'Неверный пароль или почта', reply_markup=key)
                bot.send_message(332749197,
                                 f'{message.from_user.first_name} Неверный пароль')

                bot.register_next_step_handler(message, password)

    if message.text == 'Возврат 🔙':
        markup = types.InlineKeyboardMarkup(row_width=2)
        lg1 = types.InlineKeyboardButton('Мои услуги 📊', callback_data='my_services')
        lg2 = types.InlineKeyboardButton('Мои контакты 📋', callback_data='my_contacts')
        lg3 = types.InlineKeyboardButton('Авторизация 🔐', callback_data='cabinet')
        lg4 = types.InlineKeyboardButton('Связь с менеджером 👨🏻‍💻', callback_data='connect_admin',
                                         url='https://t.me/hostmaster_support')
        lg5 = types.InlineKeyboardButton('Зарегистрироваться 📝', callback_data='site',
                                         url='https://hostmaster.uz/site/signup')
        lg6 = types.InlineKeyboardButton('Настройки 🛠', callback_data='settings')

        markup.add(lg1, lg2, lg3, lg4, lg5, lg6)
        bot.send_message(message.chat.id,
                         "Вас приветствует бот компании <b>Hostmaster</b>.\nХостинг, VDS, серверы, домены  в Узбекистане, в Ташкенте.\n\n",
                         reply_markup=markup, parse_mode='html')

    else:
        login = message.text
        chat_id = message.chat.id
        first_name = message.chat.first_name
        last_name = message.chat.last_name
        username = message.chat.username
        timestamp = message.date
        dt_obj = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

        print(dt_obj)
        connection = pymysql.connect(host='62.209.143.131',
                                     user='hostmasteruz_pbot',
                                     password='bcaxoZyAXDGc',
                                     database='hostmasteruz_base',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor
                                     )

        cursor = connection.cursor()
        cursor.execute('SELECT username FROM user')
        checkUsername = cursor.fetchall()
        list = []
        for i in checkUsername:
            list.append(i["username"])

        if message.text in list:
            cursor.execute('SELECT password_hash FROM user WHERE username=%(username)s', {'username': login})
            checkUsername = cursor.fetchone()
            bot.send_message(message.chat.id, 'Введите пароль:')
            bot.register_next_step_handler(message, password)

        elif message.text == 'Возврат 🔙':
            markup_ru = types.InlineKeyboardMarkup(row_width=2)
            lg1 = types.InlineKeyboardButton('Мои услуги 📊', callback_data='my_services')
            lg2 = types.InlineKeyboardButton('Мои контакты 📋', callback_data='my_contacts')
            lg3 = types.InlineKeyboardButton('Авторизация 🔐', callback_data='cabinet')
            lg4 = types.InlineKeyboardButton('Связь с менеджером 👨🏻‍💻', callback_data='connect_admin',
                                             url='https://t.me/hostmaster_support')
            lg5 = types.InlineKeyboardButton('Зарегистрироваться 📝', callback_data='site',
                                             url='https://hostmaster.uz/site/signup')
            lg6 = types.InlineKeyboardButton('Настройки 🛠', callback_data='settings')

            markup_ru.add(lg1, lg2, lg3, lg4, lg5, lg6)
            bot.send_message(message.chat.id,
                             "Вас приветствует бот компании <b>Hostmaster</b>.\nХостинг, VDS, серверы, домены  в Узбекистане, в Ташкенте.\n\n",
                             reply_markup=markup_ru, parse_mode='html')

        elif message.text not in list:
            key = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
            lg1 = types.KeyboardButton("Возврат 🔙")
            key.add(lg1)
            bot.send_message(message.chat.id, 'Повторите попытку', reply_markup=key)
            bot.send_message(332749197,
                             f'{message.from_user.first_name} Cant log in')

        cursor.close()


@bot.message_handler(content_types=['text'])
def log_uz(message):
    def password_uz(message):
        def after_login_uz(message):
            def uslugi_uz(message):
                if message.text == 'Мои хостинги 🗂':
                    for i in check:
                        id = i["id"]
                        id_connect = connection.cursor()
                        id_connect.execute(
                            "select hostcontractdomain,cptariff, status from hostcontract where user_id=%(user_id)s and status = 1 union select hostcontractdomain,cptariff, status from hostcontract where user_id=%(user_id)s and status = 0 union select hostcontractdomain,cptariff, status from hostcontract where user_id=%(user_id)s and status = 2",
                            {'user_id': id})
                        checkContact = id_connect.fetchall()
                        num = 1
                        host_text = ''
                        if checkContact:
                            for i in checkContact:
                                if i["status"] == 1:
                                    i["status"] = 'Active ✅'
                                elif i["status"] == 0:
                                    i["status"] = 'Block 🚫'
                                else:
                                    i["status"] = 'Deleted ❌'
                                if i["status"] == 'Deleted ❌' or i["status"] == 'Block 🚫':
                                    host_text += f'{num}. {i["hostcontractdomain"]}, ' \
                                                 f'{i["status"]}\n'
                                else:
                                    host_text += f'{num}. {i["hostcontractdomain"]}, ' \
                                                 f'{i["status"]}, <b>{i["cptariff"]}</b>\n'
                                num += 1
                            bot.send_message(message.chat.id, host_text, parse_mode='html')
                        else:
                            bot.send_message(message.chat.id, "У вас нет услуги аренды хостингов 🤷🏻")
                    bot.register_next_step_handler(message, uslugi_uz)
                elif message.text == 'Мои домены 🔠':
                    for i in check:
                        id = i["id"]
                        id_connect = connection.cursor()
                        id_connect.execute(
                            'SELECT * ,NOW() as now_datetime FROM mydomain WHERE status IN (-2,0,1,3) and userid=%(userid)s ORDER BY expired ASC',
                            {'userid': id})
                        checkContact = id_connect.fetchall()
                        num = 1
                        domen_text = ''
                        if checkContact:
                            for i in checkContact:
                                delta = i["now_datetime"] - i["expired"]
                                if delta.days > 0:
                                    i["expired"] = '{:%d-%m-%-y} ⚠️'.format(i["expired"])
                                else:
                                    i["expired"] = '{:%d-%m-%-y}'.format(i["expired"])
                                if i["status"] == -2:
                                    i["status"] = 'A_REG'
                                elif i["status"] == 0:
                                    i["status"] = 'R_REG'
                                elif i["status"] == 1:
                                    i["status"] = 'Active ✅'
                                elif i["status"] == 3:
                                    i["status"] = 'W_RED'

                                domen_text += f'{num}. {i["mydomainname"]}.uz, ' \
                                              f'{i["status"]}, {i["expired"]}\n'
                                num += 1
                            if len(domen_text) > 4096:
                                for x in range(0, len(domen_text), 4096):
                                    bot.send_message(message.chat.id, '{}'.format(domen_text[x:x + 4096]))
                                bot.register_next_step_handler(message, uslugi_uz)
                            bot.send_message(message.chat.id, domen_text, parse_mode='html')
                        else:
                            bot.send_message(message.chat.id, 'У вас нет доменов 🤷🏻')
                    bot.register_next_step_handler(message, uslugi_uz)
                elif message.text == 'Мои VDS 🗄':
                    for i in check:
                        id = i["id"]
                        id_connect = connection.cursor()
                        id_connect.execute(
                            'SELECT `vdscontract`.`vdshostname`,'
                            ' `vds_tariffs`.`tariffname` ,'
                            '`vdscontract`.`status`  FROM '
                            '`user`, `vdscontract`, `vds_tariffs`'
                            ' WHERE   username=%(username)s AND '
                            '`user`.`id` = `vdscontract`.`user_id`'
                            ' AND `vdscontract`.`vdsid` = `vds_tariffs`.`idvds`'
                            ' ORDER BY vdscontract.status = 1 DESC;',
                            {'username': login})
                        checkContact = id_connect.fetchall()
                        num = 1
                        vds_text = ''
                        if checkContact:
                            for i in checkContact:
                                if i["status"] == 1:
                                    i["status"] = 'Active ✅'
                                elif i["status"] == 0:
                                    i["status"] = 'Block 🚫'
                                else:
                                    i["status"] = 'Deleted ❌'
                                if i["status"] == 'Deleted ❌' or i["status"] == 'Block 🚫':
                                    vds_text += f'{num}. {i["vdshostname"]}, {i["status"]}\n'

                                else:
                                    vds_text += f'{num}. {i["vdshostname"]}, {i["tariffname"]}, {i["status"]}\n'
                                num += 1
                            bot.send_message(message.chat.id, vds_text, parse_mode='html')
                        else:
                            bot.send_message(message.chat.id, 'У вас нет услуги аренды VDS 🤷🏻')

                    bot.register_next_step_handler(message, uslugi_uz)
                elif message.text == 'Мои сервера 💾':
                    for i in check:
                        print(i)
                        id = i["id"]
                        id_connect = connection.cursor()
                        id_connect.execute(
                            "SELECT * FROM colcontract WHERE user_id=%(user_id)s", {'user_id': id})
                        checkContact = id_connect.fetchall()
                        num = 1
                        ser_text = ''
                        if checkContact:

                            for i in checkContact:
                                if i["status"] == 1:
                                    i["status"] = 'Active ✅'
                                elif i["status"] == 2:
                                    i["status"] = 'Block 🚫'
                                ser_text += f'{num}. <b>{i["colhostname"]}</b>, <b>{i["status"]}</b>\n'
                                num += 1
                            bot.send_message(message.chat.id, ser_text, parse_mode='html')
                        else:
                            bot.send_message(message.chat.id, 'У вас нет услуги аренды сервера 🤷🏻')

                    bot.register_next_step_handler(message, uslugi_uz)
                elif message.text == 'Возврат 🔙':
                    markup_ru = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
                    lg1 = types.KeyboardButton('Мои услуги 📊')
                    lg2 = types.KeyboardButton('Мои контакты 📋')
                    lg3 = types.KeyboardButton('Уведомления')
                    lg4 = types.KeyboardButton('Возврат 🔙')
                    markup_ru.add(lg1, lg2, lg3, lg4)
                    bot.send_message(message.chat.id, 'Возврат 🔙', reply_markup=markup_ru, parse_mode='html')
                    bot.register_next_step_handler(message, after_login_uz)

            def doljniki(message):
                def doljniki_domen(message):
                    if message.text == '60 дней':
                        connection = pymysql.connect(host='62.209.143.131',
                                                     user='hostmasteruz_pbot',
                                                     password='bcaxoZyAXDGc',
                                                     database='hostmasteruz_base',
                                                     charset='utf8mb4',
                                                     cursorclass=pymysql.cursors.DictCursor
                                                     )
                        min = connection.cursor()
                        min.execute(
                            "SELECT `idmydomain`, `userid`, `mydomainname`, NOW() as now_datetime, `expired` FROM `mydomain` WHERE DATE(`expired`) = DATE(DATE_ADD(NOW(),INTERVAL 60 DAY))")
                        domendays_60 = min.fetchall()
                        if not domendays_60:
                            bot.send_message(message.chat.id, 'Сегодня должников нет')
                        else:
                            days_60 = ''
                            n = 1
                            for i in domendays_60:
                                days_60 += f'{n}. {i["mydomainname"]}.uz\n'
                                n += 1
                            print(days_60)
                            bot.send_message(message.chat.id, days_60)
                        min.close()
                        bot.register_next_step_handler(message, doljniki_domen)
                    elif message.text == '30 дней':
                        connection = pymysql.connect(host='62.209.143.131',
                                                     user='hostmasteruz_pbot',
                                                     password='bcaxoZyAXDGc',
                                                     database='hostmasteruz_base',
                                                     charset='utf8mb4',
                                                     cursorclass=pymysql.cursors.DictCursor
                                                     )
                        min = connection.cursor()
                        min.execute(
                            "SELECT `idmydomain`, `userid`, `mydomainname`, "
                            "NOW() as now_datetime, `expired` "
                            "FROM `mydomain` WHERE "
                            "DATE(`expired`) = DATE(DATE_ADD(NOW(),INTERVAL 30 DAY))")
                        domendays_30 = min.fetchall()
                        if not domendays_30:
                            bot.send_message(message.chat.id, 'Сегодня должников нет')
                        else:
                            days_30 = ''
                            n = 1
                            for i in domendays_30:
                                days_30 += f'{n}. {i["mydomainname"]}.uz\n'
                                n += 1
                            print(days_30)
                            bot.send_message(message.chat.id, days_30)
                        min.close()
                        bot.register_next_step_handler(message, doljniki_domen)
                    elif message.text == '10 дней':
                        connection = pymysql.connect(host='62.209.143.131',
                                                     user='hostmasteruz_pbot',
                                                     password='bcaxoZyAXDGc',
                                                     database='hostmasteruz_base',
                                                     charset='utf8mb4',
                                                     cursorclass=pymysql.cursors.DictCursor
                                                     )
                        min = connection.cursor()
                        min.execute(
                            "SELECT `idmydomain`, `userid`, "
                            "`mydomainname`, NOW() as now_datetime, "
                            "`expired` FROM `mydomain` "
                            "WHERE DATE(`expired`) = DATE(DATE_ADD(NOW(),INTERVAL 10 DAY))")
                        domendays_10 = min.fetchall()
                        if not domendays_10:
                            bot.send_message(message.chat.id, 'Сегодня должников нет')
                        else:
                            days_10 = ''
                            n = 1
                            for i in domendays_10:
                                days_10 += f'{n}. {i["mydomainname"]}.uz\n'
                                n += 1
                            print(days_10)
                            bot.send_message(message.chat.id, days_10)
                        min.close()
                        bot.register_next_step_handler(message, doljniki_domen)
                    elif message.text == 'Сегодня':
                        connection = pymysql.connect(host='62.209.143.131',
                                                     user='hostmasteruz_pbot',
                                                     password='bcaxoZyAXDGc',
                                                     database='hostmasteruz_base',
                                                     charset='utf8mb4',
                                                     cursorclass=pymysql.cursors.DictCursor
                                                     )
                        min = connection.cursor()
                        min.execute(
                            "SELECT `idmydomain`, `userid`,"
                            " `mydomainname`, NOW() as now_datetime, "
                            "`expired` FROM `mydomain` "
                            "WHERE DATE(`expired`) = DATE(NOW())")
                        domendays_1 = min.fetchall()
                        if not domendays_1:
                            bot.send_message(message.chat.id, 'Сегодня должников нет')
                        else:
                            days_1 = ''
                            n = 1
                            for i in domendays_1:
                                days_1 += f'{n}. {i["mydomainname"]}.uz\n'
                                n += 1
                            print(days_1)
                            bot.send_message(message.chat.id, days_1)
                        min.close()
                        bot.register_next_step_handler(message, doljniki_domen)
                    elif message.text == 'Redemption':
                        connection = pymysql.connect(host='62.209.143.131',
                                                     user='hostmasteruz_pbot',
                                                     password='bcaxoZyAXDGc',
                                                     database='hostmasteruz_base',
                                                     charset='utf8mb4',
                                                     cursorclass=pymysql.cursors.DictCursor
                                                     )
                        min = connection.cursor()
                        min.execute(
                            "SELECT `idmydomain`, `userid`, "
                            "`mydomainname`, NOW() as now_datetime,"
                            " `expired` FROM `mydomain` WHERE status=3")
                        redemption = min.fetchall()
                        red = ''
                        n = 1
                        for i in redemption:
                            red += f'{n}. {i["mydomainname"]}.uz\n'
                            n += 1
                        print(red)
                        bot.send_message(message.chat.id, red)
                        min.close()
                        bot.register_next_step_handler(message, doljniki_domen)
                    elif message.text == 'Назад':
                        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
                        lg1 = types.KeyboardButton('Домен')
                        # lg2 = types.KeyboardButton('Хостинг')
                        # lg3 = types.KeyboardButton('VDS')
                        lg4 = types.KeyboardButton('Возврат 🔙')
                        markup.add(lg1, lg4)
                        bot.send_message(message.chat.id, 'Уведомления', reply_markup=markup)
                        bot.register_next_step_handler(message, doljniki)

                if message.text == 'Домен':
                    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
                    lg1 = types.KeyboardButton('60 дней')
                    lg2 = types.KeyboardButton('30 дней')
                    lg3 = types.KeyboardButton('10 дней')
                    lg4 = types.KeyboardButton('Сегодня')
                    lg5 = types.KeyboardButton('Redemption')
                    lg6 = types.KeyboardButton('Назад')
                    markup.add(lg1, lg2, lg3, lg4, lg5, lg6)
                    bot.send_message(message.chat.id, 'Уведомления Доменов', reply_markup=markup)
                    bot.register_next_step_handler(message, doljniki_domen)

                elif message.text == 'Возврат 🔙':
                    markup_ru = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
                    lg1 = types.KeyboardButton('Мои услуги 📊')
                    lg2 = types.KeyboardButton('Мои контакты 📋')
                    lg3 = types.KeyboardButton('Уведомления')
                    lg4 = types.KeyboardButton('Возврат 🔙')

                    markup_ru.add(lg1, lg2, lg3, lg4)

                    bot.send_message(message.chat.id,
                                     "Вас приветствует бот компании <b>Hostmaster</b>.\nХостинг, VDS, серверы, домены  в Узбекистане, в Ташкенте.\n\n",
                                     reply_markup=markup_ru, parse_mode='html')
                bot.register_next_step_handler(message, after_login_uz)

            if message.text == 'Мои контакты 📋':
                for i in check:
                    id = i["id"]
                    id_connect = connection.cursor()
                    id_connect.execute(
                        'SELECT * FROM contact WHERE userid=%(userid)s', {'userid': id})
                    checkContact = id_connect.fetchall()
                    text = ''
                    num = 1
                    for i in checkContact:
                        if i["contactcompany"] is None:
                            text += f'{num}. {i["contactname"]}\nБаланс: <b>{i["balance"]} сум 💰</b>\n'
                        else:
                            text += f'{num}. {i["contactcompany"]}\nБаланс: <b>{i["balance"]} сум 💰</b>\n'
                        num += 1
                    bot.send_message(message.chat.id, text, parse_mode='html')
                bot.register_next_step_handler(message, after_login_uz)
            elif message.text == 'Мои услуги 📊':
                markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
                lg1 = types.KeyboardButton('Мои хостинги 🗂')
                lg2 = types.KeyboardButton('Мои домены 🔠')
                lg3 = types.KeyboardButton('Мои VDS 🗄')
                lg4 = types.KeyboardButton('Мои сервера 💾')
                lg5 = types.KeyboardButton('Возврат 🔙')
                markup.add(lg1, lg2, lg3, lg4, lg5)
                bot.send_message(message.chat.id, 'Мои услуги 📊', reply_markup=markup)
                bot.register_next_step_handler(message, uslugi_uz)
            elif message.text == 'Уведомления':
                markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
                lg1 = types.KeyboardButton('Домен')
                # lg2 = types.KeyboardButton('Хостинг')
                # lg3 = types.KeyboardButton('VDS')
                lg4 = types.KeyboardButton('Назад')
                markup.add(lg1, lg4)
                bot.send_message(message.chat.id, 'Уведомления', reply_markup=markup)
                bot.register_next_step_handler(message, doljniki)
            elif message.text == 'Возврат 🔙':
                markup = types.InlineKeyboardMarkup(row_width=2)
                lg1 = types.InlineKeyboardButton('Мои услуги 📊', callback_data='my_services')
                lg2 = types.InlineKeyboardButton('Мои контакты 📋', callback_data='my_contacts')
                lg3 = types.InlineKeyboardButton('Авторизация 🔐', callback_data='cabinet')
                lg4 = types.InlineKeyboardButton('Связь с менеджером 👨🏻‍💻', callback_data='connect_admin',
                                                 url='https://t.me/hostmaster_support')
                lg5 = types.InlineKeyboardButton('Зарегистрироваться 📝', callback_data='site',
                                                 url='https://hostmaster.uz/site/signup')
                lg6 = types.InlineKeyboardButton('Настройки 🛠', callback_data='settings')

                markup.add(lg1, lg2, lg3, lg4, lg5, lg6)
                bot.send_message(message.chat.id,
                                 "Вас приветствует бот компании <b>Hostmaster</b>.\nХостинг, VDS, серверы, домены  в Узбекистане, в Ташкенте.\n\n",
                                 reply_markup=markup, parse_mode='html')

        if message.text == 'sardor':
            connection = pymysql.connect(host='62.209.143.131',
                                         user='hostmasteruz_pbot',
                                         password='bcaxoZyAXDGc',
                                         database='hostmasteruz_base',
                                         charset='utf8mb4',
                                         cursorclass=pymysql.cursors.DictCursor
                                         )
            min = connection.cursor()
            min.execute(
                'SELECT id,password_hash FROM user WHERE username=%(username)s', {'username': login})

            check = min.fetchall()
            markup_ru = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
            lg1 = types.KeyboardButton('Мои услуги 📊')
            lg2 = types.KeyboardButton('Мои контакты 📋')
            lg3 = types.KeyboardButton('Уведомления')
            lg4 = types.KeyboardButton('Возврат 🔙')
            markup_ru.add(lg1, lg2, lg3, lg4)
            bot.send_message(message.chat.id,
                             "Вы вошли под админом",
                             reply_markup=markup_ru, parse_mode='html')
            bot.send_message(332749197,
                             f'{message.from_user.first_name} Successfully authorized for admin')
            min.close()
            bot.register_next_step_handler(message, after_login_uz)
        else:
            out = crypt.crypt(message.text, checkUsername["password_hash"])

            connection = pymysql.connect(host='62.209.143.131',
                                         user='hostmasteruz_pbot',
                                         password='bcaxoZyAXDGc',
                                         database='hostmasteruz_base',
                                         charset='utf8mb4',
                                         cursorclass=pymysql.cursors.DictCursor
                                         )
            if checkUsername["password_hash"] == out:
                min = connection.cursor()
                min.execute(
                    'SELECT id,password_hash FROM user WHERE username=%(username)s', {'username': login})

                check = min.fetchall()
                markup_uz = types.InlineKeyboardMarkup(row_width=2)
                lg1 = types.InlineKeyboardButton('Mening xizmatlarim 📊', callback_data='xizmatlarim')
                lg2 = types.InlineKeyboardButton('Mening kontaktlarim 📋', callback_data='kontaktlarim')
                lg3 = types.InlineKeyboardButton("Kirish 🔐", callback_data="ro'yxatdan_o'tish")
                lg4 = types.InlineKeyboardButton("Menejer bilan aloqa 👨🏻‍💻", callback_data="connect_admin",
                                                 url='https://t.me/hostmaster_support')
                lg5 = types.InlineKeyboardButton("Roʻyxatdan o'tish 📝", callback_data="site",
                                                 url='https://hostmaster.uz/site/signup')
                lg6 = types.InlineKeyboardButton('Sozlamalar 🛠', callback_data='sozlamalar')
                markup_uz.add(lg1, lg2, lg3, lg4, lg5, lg6)

                bot_con = pymysql.connect(host='62.209.143.131',
                                          user='hostmasteruz_pbot',
                                          password='bcaxoZyAXDGc',
                                          database='hostmasteruz_bot',
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor
                                          )
                min = connection.cursor()
                min.execute(
                    'SELECT `user`.`id`  FROM `user` WHERE username=%(username)s', {'username': login})
                check = min.fetchall()
                for i in check:
                    id = i["id"]
                    cursor = bot_con.cursor()
                    query = "INSERT INTO `sardorbot` (`tg_id`, `tg_username`, `tg_first_name`," \
                            " `tg_last_name`, `updated`,`b_username`,`b_userid`) " \
                            "VALUES ({0},'{1}','{2}','{3}','{4}','{5}','{6}')" \
                            " ON DUPLICATE KEY UPDATE " \
                            "`tg_username` = '{1}', `tg_first_name` = '{2}', " \
                            "`tg_last_name` = '{3}', `updated` = '{4}'," \
                            "`b_username`='{5}',`b_userid`='{6}'".format(
                        chat_id, username, first_name, last_name, dt_obj, login, id)
                    cursor.execute(query)
                bot.send_message(message.chat.id,
                                 "<b>Hostmaster</b> botiga xush kelibsiz.\nXosting, VDS, serverlar, domenlar O'zbekistonda, Toshkentda.\n\n",
                                 reply_markup=markup_uz, parse_mode='html')
                bot.send_message(332749197,
                                 f'{message.from_user.first_name} Successfully authorized')
                bot_con.close()
                min.close()
            elif message.text == 'Qaytish 🔙':
                markup_uz = types.InlineKeyboardMarkup(row_width=2)
                lg1 = types.InlineKeyboardButton('Mening xizmatlarim 📊', callback_data='xizmatlarim')
                lg2 = types.InlineKeyboardButton('Mening kontaktlarim 📋', callback_data='kontaktlarim')
                lg3 = types.InlineKeyboardButton("Kirish 🔐", callback_data="ro'yxatdan_o'tish")
                lg4 = types.InlineKeyboardButton("Menejer bilan aloqa 👨🏻‍💻", callback_data="connect_admin",
                                                 url='https://t.me/hostmaster_support')
                lg5 = types.InlineKeyboardButton("Roʻyxatdan o'tish 📝", callback_data="site",
                                                 url='https://hostmaster.uz/site/signup')
                lg6 = types.InlineKeyboardButton('Sozlamalar 🛠', callback_data='sozlamalar')
                markup_uz.add(lg1, lg2, lg3, lg4, lg5, lg6)
                bot.send_message(message.chat.id,
                                 "<b>Hostmaster</b> botiga xush kelibsiz.\nXosting, VDS, serverlar, domenlar O'zbekistonda, Toshkentda.\n\n",
                                 reply_markup=markup_uz, parse_mode='html')

            else:
                key = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
                lg1 = types.KeyboardButton("Qaytish 🔙")
                key.add(lg1)
                bot.send_message(332749197,
                                 f'{message.from_user.first_name} Cant log in')
                bot.send_message(message.chat.id, 'Noto‘g‘ri parol yoki elektron pochta', reply_markup=key)

                bot.register_next_step_handler(message, password_uz)

    if message.text == 'Qaytish 🔙':
        markup_uz = types.InlineKeyboardMarkup(row_width=2)
        lg1 = types.InlineKeyboardButton('Mening xizmatlarim 📊', callback_data='xizmatlarim')
        lg2 = types.InlineKeyboardButton('Mening kontaktlarim 📋', callback_data='kontaktlarim')
        lg3 = types.InlineKeyboardButton("Kirish 🔐", callback_data="ro'yxatdan_o'tish")
        lg4 = types.InlineKeyboardButton("Menejer bilan aloqa 👨🏻‍💻", callback_data="connect_admin",
                                         url='https://t.me/hostmaster_support')
        lg5 = types.InlineKeyboardButton("Roʻyxatdan o'tish 📝", callback_data="site",
                                         url='https://hostmaster.uz/site/signup')
        lg6 = types.InlineKeyboardButton('Sozlamalar 🛠', callback_data='sozlamalar')
        markup_uz.add(lg1, lg2, lg3, lg4, lg5, lg6)
        bot.send_message(message.chat.id,
                         "<b>Hostmaster</b> botiga xush kelibsiz.\nXosting, VDS, serverlar, domenlar O'zbekistonda, Toshkentda.\n\n",
                         reply_markup=markup_uz, parse_mode='html')

    else:
        login = message.text
        chat_id = message.chat.id
        first_name = message.chat.first_name
        last_name = message.chat.last_name
        username = message.chat.username
        timestamp = message.date
        dt_obj = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
        connection = pymysql.connect(host='62.209.143.131',
                                     user='hostmasteruz_pbot',
                                     password='bcaxoZyAXDGc',
                                     database='hostmasteruz_base',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor
                                     )
        cursor = connection.cursor()
        cursor.execute('SELECT username FROM user')
        checkUsername = cursor.fetchall()
        list = []
        for i in checkUsername:
            list.append(i["username"])

        if message.text in list:
            cursor.execute('SELECT password_hash FROM user WHERE username=%(username)s', {'username': login})
            checkUsername = cursor.fetchone()
            bot.send_message(message.chat.id, 'Parolni kiriting:')
            bot.register_next_step_handler(message, password_uz)

        elif message.text == 'Qaytish 🔙':
            markup_uz = types.InlineKeyboardMarkup(row_width=2)
            lg1 = types.InlineKeyboardButton('Mening xizmatlarim 📊', callback_data='xizmatlarim')
            lg2 = types.InlineKeyboardButton('Mening kontaktlarim 📋', callback_data='kontaktlarim')
            lg3 = types.InlineKeyboardButton("Kirish 🔐", callback_data="ro'yxatdan_o'tish")
            lg4 = types.InlineKeyboardButton("Menejer bilan aloqa 👨🏻‍💻", callback_data="connect_admin",
                                             url='https://t.me/hostmaster_support')
            lg5 = types.InlineKeyboardButton("Roʻyxatdan o'tish 📝", callback_data="site",
                                             url='https://hostmaster.uz/site/signup')
            lg6 = types.InlineKeyboardButton('Sozlamalar 🛠', callback_data='sozlamalar')
            markup_uz.add(lg1, lg2, lg3, lg4, lg5, lg6)
            bot.send_message(message.chat.id,
                             "<b>Hostmaster</b> botiga xush kelibsiz.\nXosting, VDS, serverlar, domenlar O'zbekistonda, Toshkentda.\n\n",
                             reply_markup=markup_uz, parse_mode='html')


        else:
            key = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
            lg1 = types.KeyboardButton("Qaytish 🔙")
            key.add(lg1)
            bot.send_message(message.chat.id, "Qayta urinib ko'ring", reply_markup=key)
            bot.send_message(332749197,
                             f'{message.from_user.first_name} Cant log in')
            bot.register_next_step_handler(message, log_uz)

        cursor.close()


@bot.message_handler(content_types=['text'])
def language(message):
    if message.text == '🇺🇿Uzbek🇺🇿':
        markup_uz = types.InlineKeyboardMarkup(row_width=2)
        lg1 = types.InlineKeyboardButton('Mening xizmatlarim 📊', callback_data='xizmatlarim')
        lg2 = types.InlineKeyboardButton('Mening kontaktlarim 📋', callback_data='kontaktlarim')
        lg3 = types.InlineKeyboardButton("Kirish 🔐", callback_data="ro'yxatdan_o'tish")
        lg4 = types.InlineKeyboardButton("Menejer bilan aloqa 👨🏻‍💻", callback_data="connect_admin",
                                         url='https://t.me/hostmaster_support')
        lg5 = types.InlineKeyboardButton("Roʻyxatdan o'tish 📝", callback_data="site",
                                         url='https://hostmaster.uz/site/signup')
        lg6 = types.InlineKeyboardButton('Sozlamalar 🛠', callback_data='sozlamalar')
        markup_uz.add(lg1, lg2, lg3, lg4, lg5, lg6)
        bot.send_message(message.chat.id,
                         "<b>Hostmaster</b> botiga xush kelibsiz.\nXosting, VDS, serverlar, domenlar O'zbekistonda, Toshkentda.\n\n",
                         reply_markup=markup_uz, parse_mode='html')

    elif message.text == '🇷🇺Russian🇷🇺':
        markup_ru = types.InlineKeyboardMarkup(row_width=2)
        lg1 = types.InlineKeyboardButton('Мои услуги 📊', callback_data='my_services')
        lg2 = types.InlineKeyboardButton('Мои контакты 📋', callback_data='my_contacts')
        lg3 = types.InlineKeyboardButton('Авторизация 🔐', callback_data='cabinet')
        lg4 = types.InlineKeyboardButton('Связь с менеджером 👨🏻‍💻', callback_data='connect_admin',
                                         url='https://t.me/hostmaster_support')
        lg5 = types.InlineKeyboardButton('Зарегистрироваться 📝', callback_data='site',
                                         url='https://hostmaster.uz/site/signup')
        lg6 = types.InlineKeyboardButton('Настройки 🛠', callback_data='settings')

        markup_ru.add(lg1, lg2, lg3, lg4, lg5, lg6)
        bot.send_message(message.chat.id,
                         "Вас приветствует бот компании <b>Hostmaster</b>.\nХостинг, VDS, серверы, домены  в Узбекистане, в Ташкенте.\n\n",
                         reply_markup=markup_ru, parse_mode='html')


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    connection = pymysql.connect(host='62.209.143.131',
                                 user='hostmasteruz_pbot',
                                 password='bcaxoZyAXDGc',
                                 database='hostmasteruz_base',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor
                                 )
    if call.data == 'cabinet':
        mark = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        menu = types.KeyboardButton('Возврат 🔙')
        mark.add(menu)
        bot.send_message(call.message.chat.id, 'Адрес е-майл:', reply_markup=mark)
        bot.register_next_step_handler(call.message, log)
    elif call.data == 'my_contacts':
        tg_con = pymysql.connect(host='62.209.143.131',
                                 user='hostmasteruz_pbot',
                                 password='bcaxoZyAXDGc',
                                 database='hostmasteruz_bot',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor
                                 )
        min = tg_con.cursor()
        min.execute(
            "SELECT `tg_id` FROM sardorbot ")

        td_check = min.fetchall()
        arr = []
        for i in td_check:
            arr.append(i["tg_id"])
        if call.message.chat.id in arr:
            bot_con = pymysql.connect(host='62.209.143.131',
                                      user='hostmasteruz_pbot',
                                      password='bcaxoZyAXDGc',
                                      database='hostmasteruz_bot',
                                      charset='utf8mb4',
                                      cursorclass=pymysql.cursors.DictCursor
                                      )
            min = bot_con.cursor()
            tg_id = call.message.chat.id
            min.execute(
                'SELECT `hostmasteruz_base`.`contact`.*, '
                '`hostmasteruz_bot`.`sardorbot`.`b_userid`'
                ' FROM `hostmasteruz_base`.`contact`, '
                '`hostmasteruz_bot`.`sardorbot` WHERE '
                '`hostmasteruz_bot`.`sardorbot`.`tg_id` = %(tg_id)s AND'
                ' `hostmasteruz_base`.`contact`.`userid` = `hostmasteruz_bot`.`sardorbot`.`b_userid`;',
                {'tg_id': tg_id})
            check = min.fetchall()
            text = ''
            num = 1
            for i in check:
                if i["contactcompany"] is None:
                    text += f'{num}. {i["contactname"]}\nБаланс: <b>{i["balance"]} сум 💰</b>\n'
                else:
                    text += f'{num}. {i["contactcompany"]}\nБаланс: <b>{i["balance"]} сум 💰</b>\n'
                num += 1
            bot.send_message(call.message.chat.id, 'Контакты')
            bot.send_message(call.message.chat.id, text, parse_mode='html')
            bot_con.close()
        else:
            bot.send_message(call.message.chat.id, 'Если Вы зарегистрированный клиент - Вам необходимо выбрать «Авторизация», если новый - «Зарегистрироваться»')
        tg_con.close()
    elif call.data == 'my_services':
        tg_con = pymysql.connect(host='62.209.143.131',
                                 user='hostmasteruz_pbot',
                                 password='bcaxoZyAXDGc',
                                 database='hostmasteruz_bot',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor
                                 )
        min = tg_con.cursor()
        min.execute(
            "SELECT `tg_id` FROM sardorbot ")

        td_check = min.fetchall()
        arr = []
        for i in td_check:
            arr.append(i["tg_id"])
        if call.message.chat.id in arr:
            bot_con = pymysql.connect(host='62.209.143.131',
                                      user='hostmasteruz_pbot',
                                      password='bcaxoZyAXDGc',
                                      database='hostmasteruz_bot',
                                      charset='utf8mb4',
                                      cursorclass=pymysql.cursors.DictCursor
                                      )
            min = bot_con.cursor()
            tg_id = call.message.chat.id
            print(tg_id)
            min.execute(
                'SELECT `sardorbot`.`b_userid` FROM '
                '`hostmasteruz_bot`.`sardorbot` WHERE '
                '`hostmasteruz_bot`.`sardorbot`.`tg_id` = %(tg_id)s',
                {'tg_id': tg_id})
            check = min.fetchall()
            for i in check:
                print(i["b_userid"])

            def uslugi(message):
                if message.text == 'Мои хостинги 🗂':
                    for i in check:
                        id = i["b_userid"]
                        id_connect = connection.cursor()
                        id_connect.execute(
                            "select hostcontractdomain,cptariff, status from hostcontract where user_id=%(user_id)s and status = 1 union select hostcontractdomain,cptariff, status from hostcontract where user_id=%(user_id)s and status = 0 union select hostcontractdomain,cptariff, status from hostcontract where user_id=%(user_id)s and status = 2",
                            {'user_id': id})
                        checkContact = id_connect.fetchall()
                        num = 1
                        host_text = ''
                        if checkContact:
                            for i in checkContact:
                                if i["status"] == 1:
                                    i["status"] = 'Active ✅'
                                elif i["status"] == 0:
                                    i["status"] = 'Block 🚫'
                                else:
                                    i["status"] = 'Deleted ❌'
                                if i["status"] == 'Deleted ❌' or i["status"] == 'Block 🚫':
                                    host_text += f'{num}. {i["hostcontractdomain"]}, ' \
                                                 f'{i["status"]}\n'
                                else:
                                    host_text += f'{num}. {i["hostcontractdomain"]}, ' \
                                                 f'{i["status"]}, <b>{i["cptariff"]}</b>\n'
                                num += 1
                            bot.send_message(message.chat.id, host_text, parse_mode='html')
                        else:
                            bot.send_message(message.chat.id, "У вас нет услуги аренды хостингов 🤷🏻")

                    bot.register_next_step_handler(message, uslugi)
                elif message.text == 'Мои домены 🔠':
                    for i in check:
                        id = i["b_userid"]
                        id_connect = connection.cursor()
                        id_connect.execute(
                            'SELECT *, NOW() as now_datetime FROM mydomain WHERE status IN (-2,0,1,3) and userid=%(userid)s ORDER BY expired ASC ',
                            {'userid': id})
                        checkContact = id_connect.fetchall()
                        num = 1
                        domen_text = ''
                        if checkContact:
                            for i in checkContact:
                                delta = i["now_datetime"] - i["expired"]
                                if delta.days > 0:
                                    i["expired"] = '{:%d-%m-%-y}'.format(i["expired"])
                                else:
                                    i["expired"] = '{:%d-%m-%-y}'.format(i["expired"])
                                if i["status"] == -2:
                                    i["status"] = 'A_REG'
                                elif i["status"] == 0:
                                    i["status"] = 'R_REG'
                                elif i["status"] == 1:
                                    i["status"] = 'Active ✅'
                                elif i["status"] == 3:
                                    i["status"] = 'W_RED ⚠️'
                                domen_text += f'{num}. {i["mydomainname"]}.uz, ' \
                                              f'{i["status"]}, {i["expired"]}\n'
                                num += 1
                            bot.send_message(message.chat.id, domen_text, parse_mode='html')
                        else:
                            bot.send_message(message.chat.id, 'У вас нет доменов 🤷🏻')

                    bot.register_next_step_handler(message, uslugi)
                elif message.text == 'Мои VDS 🗄':
                    for i in check:
                        id = i["b_userid"]
                        id_connect = connection.cursor()
                        id_connect.execute(
                            'SELECT `vdscontract`.`vdshostname`,'
                            ' `vds_tariffs`.`tariffname` ,'
                            '`vdscontract`.`status`  FROM  '
                            '`vdscontract`, `vds_tariffs` WHERE '
                            ' `vdscontract`.`vdsid` = `vds_tariffs`.`idvds` AND user_id=%(user_id)s ORDER BY vdscontract.status = 1 DESC;',
                            {'user_id': id})
                        checkContact = id_connect.fetchall()
                        num = 1
                        vds_text = ''
                        if checkContact:
                            for i in checkContact:
                                if i["status"] == 1:
                                    i["status"] = 'Active ✅'
                                elif i["status"] == 0:
                                    i["status"] = 'Block 🚫'
                                else:
                                    i["status"] = 'Deleted ❌'
                                if i["status"] == 'Deleted ❌' or i["status"] == 'Block 🚫':
                                    vds_text += f'{num}. {i["vdshostname"]}, {i["status"]}\n'

                                else:
                                    vds_text += f'{num}. {i["vdshostname"]}, {i["tariffname"]}, {i["status"]}\n'
                                num += 1
                            bot.send_message(message.chat.id, vds_text, parse_mode='html')
                        else:
                            bot.send_message(message.chat.id, 'У вас нет услуги аренды VDS 🤷🏻')

                    bot.register_next_step_handler(message, uslugi)
                elif message.text == 'Мои сервера 💾':
                    for i in check:
                        print(i)
                        id = i["b_userid"]
                        id_connect = connection.cursor()
                        id_connect.execute(
                            "SELECT * FROM colcontract WHERE user_id=%(user_id)s", {'user_id': id})
                        checkContact = id_connect.fetchall()
                        num = 1
                        ser_text = ''
                        if checkContact:

                            for i in checkContact:
                                if i["status"] == 1:
                                    i["status"] = 'Active ✅'
                                elif i["status"] == 2:
                                    i["status"] = 'Block 🚫'
                                ser_text += f'{num}. <b>{i["colhostname"]}</b>, <b>{i["status"]}</b>\n'
                                num += 1
                            bot.send_message(message.chat.id, ser_text, parse_mode='html')
                        else:
                            bot.send_message(message.chat.id, 'У вас нет услуги аренды сервера 🤷🏻')

                    bot.register_next_step_handler(message, uslugi)
                elif message.text == 'Возврат 🔙':
                    markup = types.InlineKeyboardMarkup(row_width=2)
                    lg1 = types.InlineKeyboardButton('Мои услуги 📊', callback_data='my_services')
                    lg2 = types.InlineKeyboardButton('Мои контакты 📋', callback_data='my_contacts')
                    lg3 = types.InlineKeyboardButton('Авторизация 🔐', callback_data='cabinet')
                    lg4 = types.InlineKeyboardButton('Связь с менеджером 👨🏻‍💻', callback_data='connect_admin',
                                                     url='https://t.me/hostmaster_support')
                    lg5 = types.InlineKeyboardButton('Зарегистрироваться 📝', callback_data='site',
                                                     url='https://hostmaster.uz/site/signup')
                    lg6 = types.InlineKeyboardButton('Настройки 🛠', callback_data='settings')

                    markup.add(lg1, lg2, lg3, lg4, lg5, lg6)
                    bot.send_message(message.chat.id,
                                     "Вас приветствует бот компании <b>Hostmaster</b>.\nХостинг, VDS, серверы, домены  в Узбекистане, в Ташкенте.\n\n",
                                     reply_markup=markup, parse_mode='html')

            markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
            lg1 = types.KeyboardButton('Мои хостинги 🗂')
            lg2 = types.KeyboardButton('Мои домены 🔠')
            lg3 = types.KeyboardButton('Мои VDS 🗄')
            lg4 = types.KeyboardButton('Мои сервера 💾')

            lg5 = types.KeyboardButton('Возврат 🔙')
            markup.add(lg1, lg2, lg3, lg4, lg5)
            bot.send_message(call.message.chat.id, 'Мои услуги 📊', reply_markup=markup)
            bot.register_next_step_handler(call.message, uslugi)
            bot_con.close()
        else:
            bot.send_message(call.message.chat.id, 'Если Вы зарегистрированный клиент - Вам необходимо выбрать «Авторизация», если новый - «Зарегистрироваться»')
        tg_con.close()
    elif call.data == 'settings':
        mark = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        lg1 = types.KeyboardButton('🇷🇺Russian🇷🇺')
        lg2 = types.KeyboardButton('🇺🇿Uzbek🇺🇿')

        mark.add(lg1, lg2)
        bot.send_message(call.message.chat.id, 'Смена языка', reply_markup=mark)
        bot.register_next_step_handler(call.message, language)
    elif call.data == "ro'yxatdan_o'tish":
        mark = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        menu = types.KeyboardButton('Qaytish 🔙')
        mark.add(menu)
        bot.send_message(call.message.chat.id, 'Mail pochta manzili:', reply_markup=mark)
        bot.register_next_step_handler(call.message, log_uz)
    elif call.data == 'xizmatlarim':
        tg_con = pymysql.connect(host='62.209.143.131',
                                 user='hostmasteruz_pbot',
                                 password='bcaxoZyAXDGc',
                                 database='hostmasteruz_bot',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor
                                 )
        min = tg_con.cursor()
        min.execute(
            "SELECT `tg_id` FROM sardorbot ")

        td_check = min.fetchall()
        arr = []
        for i in td_check:
            arr.append(i["tg_id"])
        if call.message.chat.id in arr:
            bot_con = pymysql.connect(host='62.209.143.131',
                                      user='hostmasteruz_pbot',
                                      password='bcaxoZyAXDGc',
                                      database='hostmasteruz_bot',
                                      charset='utf8mb4',
                                      cursorclass=pymysql.cursors.DictCursor
                                      )
            min = bot_con.cursor()
            tg_id = call.message.chat.id
            print(tg_id)
            min.execute(
                'SELECT `sardorbot`.`b_userid` FROM '
                '`hostmasteruz_bot`.`sardorbot` WHERE '
                '`hostmasteruz_bot`.`sardorbot`.`tg_id` = %(tg_id)s',
                {'tg_id': tg_id})
            check = min.fetchall()
            for i in check:
                print(i["b_userid"])

            def uslugi_uz(message):
                if message.text == 'Xostinglarim 🗂':
                    for i in check:
                        id = i["b_userid"]
                        id_connect = connection.cursor()
                        id_connect.execute(
                            "select hostcontractdomain,cptariff, status from hostcontract where user_id=%(user_id)s and status = 1 union select hostcontractdomain,cptariff, status from hostcontract where user_id=%(user_id)s and status = 0 union select hostcontractdomain,cptariff, status from hostcontract where user_id=%(user_id)s and status = 2",
                            {'user_id': id})
                        checkContact = id_connect.fetchall()
                        num = 1
                        host_text = ''
                        if checkContact:
                            for i in checkContact:
                                if i["status"] == 1:
                                    i["status"] = 'Active ✅'
                                elif i["status"] == 0:
                                    i["status"] = 'Block 🚫'
                                else:
                                    i["status"] = 'Deleted ❌'
                                if i["status"] == 'Deleted ❌' or i["status"] == 'Block 🚫':
                                    host_text += f'{num}. {i["hostcontractdomain"]}, ' \
                                                 f'{i["status"]}\n'
                                else:
                                    host_text += f'{num}. {i["hostcontractdomain"]}, ' \
                                                 f'{i["status"]}, <b>{i["cptariff"]}</b>\n'
                                num += 1
                            bot.send_message(message.chat.id, host_text, parse_mode='html')
                        else:
                            bot.send_message(message.chat.id, "Sizda xosting ijarasi xizmati mavjud emas 🤷🏻")

                    bot.register_next_step_handler(message, uslugi_uz)
                elif message.text == 'Domenlarim 🔠':
                    for i in check:
                        id = i["b_userid"]
                        id_connect = connection.cursor()
                        id_connect.execute(
                            'SELECT *,NOW() as now_datetime FROM mydomain WHERE status IN (-2,0,1,3) and userid=%(userid)s ORDER BY expired ASC',
                            {'userid': id})
                        checkContact = id_connect.fetchall()
                        num = 1
                        domen_text = ''
                        if checkContact:
                            for i in checkContact:
                                delta = i["now_datetime"] - i["expired"]
                                if delta.days > 0:
                                    i["expired"] = '{:%d-%m-%-y}'.format(i["expired"])
                                else:
                                    i["expired"] = '{:%d-%m-%-y}'.format(i["expired"])
                                if i["status"] == -2:
                                    i["status"] = 'A_REG'
                                elif i["status"] == 0:
                                    i["status"] = 'R_REG'
                                elif i["status"] == 1:
                                    i["status"] = 'Active ✅'
                                elif i["status"] == 3:
                                    i["status"] = 'W_RED ⚠️'

                                domen_text += f'{num}. {i["mydomainname"]}.uz, ' \
                                              f'{i["status"]}, {i["expired"]}\n'

                                num += 1
                            bot.send_message(message.chat.id, domen_text, parse_mode='html')
                        else:
                            bot.send_message(message.chat.id, "Sizda domen yo'q 🤷🏻")

                    bot.register_next_step_handler(message, uslugi_uz)
                elif message.text == "VDS'larim 🗄":
                    for i in check:
                        id = i["b_userid"]
                        id_connect = connection.cursor()
                        id_connect.execute(
                            'SELECT `vdscontract`.`vdshostname`, '
                            '`vds_tariffs`.`tariffname` ,'
                            '`vdscontract`.`status`  FROM  '
                            '`vdscontract`, `vds_tariffs` WHERE '
                            ' `vdscontract`.`vdsid` = `vds_tariffs`.`idvds` AND user_id=%(user_id)s ORDER BY vdscontract.status = 1 DESC;',
                            {'user_id': id})
                        checkContact = id_connect.fetchall()
                        num = 1
                        vds_text = ''
                        if checkContact:
                            for i in checkContact:
                                if i["status"] == 1:
                                    i["status"] = 'Active ✅'
                                elif i["status"] == 0:
                                    i["status"] = 'Block 🚫'
                                else:
                                    i["status"] = 'Deleted ❌'
                                if i["status"] == 'Deleted ❌' or i["status"] == 'Block 🚫':
                                    vds_text += f'{num}. {i["vdshostname"]}, {i["status"]}\n'
                                else:
                                    vds_text += f'{num}. {i["vdshostname"]}, {i["tariffname"]}, {i["status"]}\n'
                                num += 1
                            bot.send_message(message.chat.id, vds_text, parse_mode='html')
                        else:
                            bot.send_message(message.chat.id, "Sizda vds ijarasi xizmati mavjud emas 🤷🏻")

                    bot.register_next_step_handler(message, uslugi_uz)
                elif message.text == 'Serverlarim 💾':
                    for i in check:
                        id = i["b_userid"]
                        id_connect = connection.cursor()
                        id_connect.execute(
                            "SELECT * FROM colcontract WHERE user_id=%(user_id)s", {'user_id': id})
                        checkContact = id_connect.fetchall()
                        num = 1
                        ser_text = ''
                        if checkContact:
                            for i in checkContact:
                                if i["status"] == 1:
                                    i["status"] = 'Active ✅'
                                elif i["status"] == 2:
                                    i["status"] = 'Block 🚫'
                                ser_text += f'{num}. <b>{i["colhostname"]}</b>, <b>{i["status"]}</b>\n'
                                num += 1
                            bot.send_message(message.chat.id, ser_text, parse_mode='html')
                        else:
                            bot.send_message(message.chat.id, "Sizda server ijarasi xizmati mavjud emas 🤷🏻")

                    bot.register_next_step_handler(message, uslugi_uz)
                elif message.text == 'Qaytish 🔙':
                    markup_uz = types.InlineKeyboardMarkup(row_width=2)
                    lg1 = types.InlineKeyboardButton("Mening xizmatlarim 📊", callback_data='xizmatlarim')
                    lg2 = types.InlineKeyboardButton("Mening kontaktlarim 📋", callback_data='kontaktlarim')
                    lg3 = types.InlineKeyboardButton("Kirish 🔐", callback_data="ro'yxatdan_o'tish")
                    lg4 = types.InlineKeyboardButton("Menejer bilan aloqa 👨🏻‍💻", callback_data="connect_admin",
                                                     url='https://t.me/hostmaster_support')
                    lg5 = types.InlineKeyboardButton("Roʻyxatdan o'tish 📝", callback_data="site",
                                                     url='https://hostmaster.uz/site/signup')
                    lg6 = types.InlineKeyboardButton("Sozlamalar 🛠", callback_data='sozlamalar')
                    markup_uz.add(lg1, lg2, lg3, lg4, lg5, lg6)
                    bot.send_message(message.chat.id,
                                     "<b>Hostmaster</b> botiga xush kelibsiz.\nXosting, VDS, serverlar, domenlar O'zbekistonda, Toshkentda.\n\n",
                                     reply_markup=markup_uz, parse_mode='html')

            markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
            lg1 = types.KeyboardButton('Xostinglarim 🗂')
            lg2 = types.KeyboardButton('Domenlarim 🔠')
            lg3 = types.KeyboardButton("VDS'larim 🗄")
            lg4 = types.KeyboardButton('Serverlarim 💾')

            lg5 = types.KeyboardButton('Qaytish 🔙')
            markup.add(lg1, lg2, lg3, lg4, lg5)
            bot.send_message(call.message.chat.id, 'Mening xizmatlarim 📊', reply_markup=markup)
            bot.register_next_step_handler(call.message, uslugi_uz)
        else:
            bot.send_message(call.message.chat.id, """Agar siz ro'yxatdan o'tgan mijoz bo'lsangiz - «Kirish»ni tanlashingiz kerak, agar yangi mijoz bo'lsangiz - "Ro'yxatdan o'tish»""")
    elif call.data == 'kontaktlarim':
        tg_con = pymysql.connect(host='62.209.143.131',
                                 user='hostmasteruz_pbot',
                                 password='bcaxoZyAXDGc',
                                 database='hostmasteruz_bot',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor
                                 )
        min = tg_con.cursor()
        min.execute(
            "SELECT `tg_id` FROM sardorbot ")

        td_check = min.fetchall()
        arr = []
        for i in td_check:
            arr.append(i["tg_id"])
        if call.message.chat.id in arr:
            bot_con = pymysql.connect(host='62.209.143.131',
                                      user='hostmasteruz_pbot',
                                      password='bcaxoZyAXDGc',
                                      database='hostmasteruz_bot',
                                      charset='utf8mb4',
                                      cursorclass=pymysql.cursors.DictCursor
                                      )
            min = bot_con.cursor()
            tg_id = call.message.chat.id
            min.execute(
                'SELECT `hostmasteruz_base`.`contact`.*,'
                '`hostmasteruz_bot`.`sardorbot`.`b_userid` '
                'FROM `hostmasteruz_base`.`contact`, '
                '`hostmasteruz_bot`.`sardorbot` WHERE'
                ' `hostmasteruz_bot`.`sardorbot`.`tg_id` = %(tg_id)s '
                'AND `hostmasteruz_base`.`contact`.`userid` '
                '= `hostmasteruz_bot`.`sardorbot`.`b_userid`;',
                {'tg_id': tg_id})
            check = min.fetchall()
            text = ''
            num = 1
            for i in check:
                if i["contactcompany"] is None:
                    text += f'{num}. {i["contactname"]}\nBalans: <b>{i["balance"]} sum 💰</b>\n'
                else:
                    text += f'{num}. {i["contactcompany"]}\nBalans: <b>{i["balance"]} sum 💰</b>\n'
                num += 1
            bot.send_message(call.message.chat.id, 'Kontaktlar')
            bot.send_message(call.message.chat.id, text, parse_mode='html')
        else:
            bot.send_message(call.message.chat.id, """Agar siz ro'yxatdan o'tgan mijoz bo'lsangiz - «Kirish»ni tanlashingiz kerak, agar yangi mijoz bo'lsangiz - "Ro'yxatdan o'tish»""")
    elif call.data == 'sozlamalar':
        mark = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        lg1 = types.KeyboardButton('🇷🇺Russian🇷🇺')
        lg2 = types.KeyboardButton('🇺🇿Uzbek🇺🇿')
        mark.add(lg1, lg2)
        bot.send_message(call.message.chat.id, 'Til ozgartirish', reply_markup=mark)

        bot.register_next_step_handler(call.message, language)


def job2():
    day_of_month = datetime.now().day
    print(day_of_month)
    if day_of_month == 27:
        bot.send_message(332749197, 'hello')


def schedule_checker():
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    schedule.every().day.at("17:11").do(domen_60_days_schedule)
    schedule.every().day.at("17:07").do(domen_30_days_schedule)
    schedule.every().day.at("11:46").do(domen_10_days_schedule)
    schedule.every().day.at("11:33").do(domen_1_days_schedule)
    # schedule.every().day.at('12:14').do(vds_schedule)
    # schedule.every().day.at("12:15").do(hosting_schedule)
    Thread(target=schedule_checker).start()
# while True:
#     try:
bot.polling(none_stop=True)
