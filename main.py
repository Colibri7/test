import crypt
import datetime
import time

from datetime import datetime
import telebot
from telebot import types
import pymysql

bot = telebot.TeleBot('1978328105:AAEaDKcB-XROaLcKzuf1QB2Smu0CEkVjhSU',threaded=False)

bot.remove_webhook()
connection = pymysql.connect(host='62.209.143.131',
                             user='hostmasteruz_pbot',
                             password='bcaxoZyAXDGc',
                             database='hostmasteruz_base',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor
                             )

SQLALCHEMY_ENGINE_OPTIONS = {
    "pool_pre_ping": True,
    "pool_recycle": 300,
}
some_id = 332749197


def domain_60():
    min = connection.cursor()
    min.execute(
        "SELECT `mydomain`.`idmydomain`, `mydomain`.`userid`, `mydomain`.`mydomainname`, NOW() as now_datetime, `mydomain`.`expired`, `contact`.`contactname`, `contact`.`contactcompany` FROM `mydomain`, `contact` WHERE DATE(`mydomain`.`expired`) = DATE(DATE_ADD(NOW(),INTERVAL 60 DAY)) AND `mydomain`.`mydomaincontactcust` = `contact`.`idcontact`;"
    )
    domain_60 = min.fetchall()

    for i in domain_60:
        date = '{:%d-%m-%Y}'.format(i["expired"])
        if i["contactcompany"] == None:
            return bot.send_message(some_id, f'Уважаемый {i["contactname"]}!\n'
                                      f'Уведомляем Вас о том, что срок действия Вашего домена\n'
                                      f'{i["mydomainname"]}.uz истекает {date} года.\n'
                                      f'Просим Вас ознакомиться с тарифами (ссылка на страницу сайта)\n'
                                      f'на продление регистрации доменов, оплатить\nсоответствующую сумму'
                                      f'и сообщить менеджеру о продлении\nдомена. В случае неоплаты,'
                                      f'Ваш домен будет свободен для\nрегистрации другим лицом.\n'
                                      f'С уважением, команда Hostmaster!')
        else:
            return bot.send_message(some_id, f'Уважаемый {i["contactcompany"]}!\n'
                                      f'Уведомляем Вас о том, что срок действия Вашего домена\n'
                                      f'{i["mydomainname"]}.uz истекает {date} года.\n'
                                      f'Просим Вас ознакомиться с тарифами (ссылка на страницу сайта)\n'
                                      f'на продление регистрации доменов, оплатить\nсоответствующую сумму'
                                      f'и сообщить менеджеру о продлении\nдомена. В случае неоплаты,'
                                      f'Ваш домен будет свободен для\nрегистрации другим лицом.\n'
                                      f'С уважением, команда Hostmaster!')


# def send_message():
#     bot.send_message(332749197, 'Hello')
#
#
# schedule.every().day.at("17:23").do(send_message())


def func(message):
    if message.text == 'Главное меню':
        markup = types.InlineKeyboardMarkup(row_width=2)
        lg1 = types.InlineKeyboardButton('Мои услуги', callback_data='my_services')
        lg2 = types.InlineKeyboardButton('Мои контакты', callback_data='my_contacts')
        lg3 = types.InlineKeyboardButton('Вход/Регистрация', callback_data='cabinet')
        lg4 = types.InlineKeyboardButton('Оплата', callback_data='pay_services')
        lg5 = types.InlineKeyboardButton('Настройки', callback_data='settings')

        markup.add(lg1, lg2, lg3, lg4, lg5)
        bot.send_message(message.chat.id,
                         'Это информационный бот компании Hostmaster.'
                         '\nHostmaster – Хостинг провайдер и регистратор доменов в'
                         '\nУзбекистане, в Ташкенте.\nНаш телефон: 71-202-55-11',
                         reply_markup=markup)
        bot.register_next_step_handler(message, language)

    elif message.text == 'Bosh sahifa':
        markup_uz = types.InlineKeyboardMarkup(row_width=2)
        lg1 = types.InlineKeyboardButton("Mijozlarni qo'llab-quvvatlash", callback_data='support')
        lg2 = types.InlineKeyboardButton('Kompaniya veb-sayti', callback_data='web', url='https://www.hostmaster.uz/')
        lg3 = types.InlineKeyboardButton("Xizmatlar uchun tezkor to'lov", callback_data='payment',
                                         url='https://www.hostmaster.uz/pay')
        lg4 = types.InlineKeyboardButton('Balans', callback_data='Balans')
        lg5 = types.InlineKeyboardButton('Yangiliklar kanali', callback_data='tg_channel',
                                         url='https://t.me/hostmasteruz')

        lg6 = types.InlineKeyboardButton("Xizmatlar va to'lovlar", callback_data='pay_services')
        lg7 = types.InlineKeyboardButton('Sozlamalar', callback_data='Sozlamalar')

        markup_uz.add(lg1, lg2, lg3, lg4, lg5, lg6, lg7)
        bot.send_message(message.chat.id,
                         """Bu Hostmaster kompaniyasining axborot boti.\nHostmaster - Xosting provayderi va domen registratori" \nO'zbekiston,Toshkentda. Bizning telefon: 71-202-55-11""",
                         reply_markup=markup_uz)


# Start bot
@bot.message_handler(commands=['start', 'menu'])
def send_welcome(message):
    text = f'<b>{message.from_user.first_name}</b> пишет боту'
    markup = types.InlineKeyboardMarkup(row_width=2)
    lg1 = types.InlineKeyboardButton('Мои услуги', callback_data='my_services')
    lg2 = types.InlineKeyboardButton('Мои контакты', callback_data='my_contacts')
    lg3 = types.InlineKeyboardButton('Вход/Регистрация', callback_data='cabinet')
    lg4 = types.InlineKeyboardButton('Оплата', callback_data='pay_services')
    lg5 = types.InlineKeyboardButton('Настройки', callback_data='settings')

    markup.add(lg1, lg2, lg3, lg4, lg5)

    bot.send_message(332749197, text, parse_mode='html')
    bot.send_message(message.chat.id,
                     """Это информационный бот компании Hostmaster.Hostmaster – Хостинг провайдер и регистратор доменов в Узбекистане, в Ташкенте.Наш телефон: 71-202-55-11\n\nBu Hostmaster kompaniyasining axborot boti. Hostmaster - Xosting provayderi va domen registratori  O'zbekiston, Toshkentda. Bizning telefon: 71-202-55-11""",
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def login_reg(message):
    if message.text == 'Зарегистрироваться':
        bot.send_message(message.chat.id, 'Для регистрации, пожалуйста, введите следующие данные:')
        bot.send_message(message.chat.id, 'Адрес е-майл:')


    elif message.text == 'Вход для клиентов':
        bot.send_message(message.chat.id, 'Адрес е-майл:')
        bot.register_next_step_handler(message, log)

    elif message.text == 'Главное меню':
        markup = types.InlineKeyboardMarkup(row_width=2)
        lg1 = types.InlineKeyboardButton('Мои услуги', callback_data='my_services')
        lg2 = types.InlineKeyboardButton('Мои контакты', callback_data='my_contacts')
        lg3 = types.InlineKeyboardButton('Вход/Регистрация', callback_data='cabinet')
        lg4 = types.InlineKeyboardButton('Оплата', callback_data='pay_services')
        lg5 = types.InlineKeyboardButton('Настройки', callback_data='settings')

        markup.add(lg1, lg2, lg3, lg4, lg5)
        bot.send_message(message.chat.id,
                         'Главное меню',
                         reply_markup=markup)
        bot.register_next_step_handler(message, language)


@bot.message_handler(content_types=['text'])
def log(message):
    def password(message):
        def after_login(message):
            def uslugi(message):
                if message.text == 'Мои хостинги':
                    for i in check:
                        id = i["id"]
                        id_connect = connection.cursor()
                        id_connect.execute(
                            'SELECT * FROM hostcontract WHERE status=1 and user_id=%(user_id)s', {'user_id': id})
                        checkContact = id_connect.fetchall()
                        num = 1
                        host_text = ''
                        if checkContact:
                            for i in checkContact:
                                if i["status"] == 1:
                                    i["status"] = 'Active'
                                host_text += f'{num}.{i["hostcontractdomain"]}, Тариф: {i["cptariff"]}, Статус: {i["status"]}\n'
                                bot.send_message(message.chat.id, host_text)
                                num += 1
                        else:
                            bot.send_message(message.chat.id, "У вас нет хостингов")

                    bot.register_next_step_handler(message, uslugi)
                elif message.text == 'Мои домены':
                    for i in check:
                        id = i["id"]
                        id_connect = connection.cursor()
                        id_connect.execute(
                            'SELECT * FROM mydomain WHERE status IN (-2,0,1,3) and userid=%(userid)s', {'userid': id})
                        checkContact = id_connect.fetchall()
                        num = 1
                        domen_text = ''
                        if checkContact:
                            for i in checkContact:

                                if i["status"] == -2:
                                    i["status"] = 'A_REG'
                                elif i["status"] == 0:
                                    i["status"] = 'R_REG'
                                elif i["status"] == 1:
                                    i["status"] = 'ACTIVE'
                                elif i["status"] == 3:
                                    i["status"] = 'W_RED'

                                domen_text += f'{num}.{i["mydomainname"]}.uz, Статус: {(i["status"])}, Дата окончания:{i["expired"].strftime("%d/%m/%Y")}'
                                bot.send_message(message.chat.id, domen_text)
                                num += 1
                        else:
                            bot.send_message(message.chat.id, 'У вас нет доменов')

                    bot.register_next_step_handler(message, uslugi)
                elif message.text == 'Мои VDS':
                    for i in check:
                        id = i["id"]
                        id_connect = connection.cursor()
                        id_connect.execute(
                            'SELECT `vdscontract`.`vdshostname`, `vds_tariffs`.`tariffname` ,`vdscontract`.`status`  FROM `user`, `vdscontract`, `vds_tariffs` WHERE   username=%(username)s AND `user`.`id` = `vdscontract`.`user_id` AND `vdscontract`.`vdsid` = `vds_tariffs`.`idvds` ORDER BY `vdscontract`.`vdshostname`;',
                            {'username': login})
                        checkContact = id_connect.fetchall()
                        num = 1
                        vds_text = ''
                        if checkContact:
                            for i in checkContact:
                                if i["status"] == 1:
                                    i["status"] = 'Active'
                                elif i["status"] == 0:
                                    i["status"] = 'Block'
                                else:
                                    i["status"] = 'Deleted'
                                vds_text += f'vds{num}-{i["vdshostname"]}, Тариф: {i["tariffname"]} , Статус: {i["status"]}'
                                bot.send_message(message.chat.id, vds_text)
                                num += 1
                        else:
                            bot.send_message(message.chat.id, 'У вас нет VDS')

                    bot.register_next_step_handler(message, uslugi)
                elif message.text == 'Мои сервера':

                    bot.send_message(message.chat.id, 'У вас нет сервера')

                    bot.register_next_step_handler(message, uslugi)
                elif message.text == 'Главное меню':
                    markup_ru = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                    lg1 = types.KeyboardButton('Мои услуги')
                    lg2 = types.KeyboardButton('Мои контакты')
                    lg3 = types.KeyboardButton('Главное меню')

                    markup_ru.add(lg1, lg2, lg3)

                    bot.send_message(message.chat.id,
                                     'Главное меню',
                                     reply_markup=markup_ru)
                    bot.register_next_step_handler(message, after_login)

            if message.text == 'Мои контакты':
                for i in check:
                    id = i["id"]
                    id_connect = connection.cursor()
                    id_connect.execute(
                        'SELECT * FROM contact WHERE userid=%(userid)s', {'userid': id})
                    checkContact = id_connect.fetchall()
                    text = ''
                    num = 1
                    for i in checkContact:
                        if i["contactcompany"] == None:
                            text += f'{num}. {i["contactname"]}, balans: {i["balance"]} sum\n\n'
                        else:
                            text += f'{num}. {i["contactcompany"]}, balans: {i["balance"]} sum\n\n'
                        num += 1
                    bot.send_message(message.chat.id, text)
                bot.register_next_step_handler(message, after_login)
            elif message.text == 'Мои услуги':
                markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
                lg1 = types.KeyboardButton('Мои хостинги')
                lg2 = types.KeyboardButton('Мои домены')
                lg3 = types.KeyboardButton('Мои VDS')
                lg4 = types.KeyboardButton('Мои сервера')

                lg5 = types.KeyboardButton('Главное меню')
                markup.add(lg1, lg2, lg3, lg4, lg5)
                bot.send_message(message.chat.id, 'Какую услугу хотите посмотреть ?', reply_markup=markup)
                bot.register_next_step_handler(message, uslugi)
            elif message.text == 'Главное меню':
                markup = types.InlineKeyboardMarkup(row_width=2)
                lg1 = types.InlineKeyboardButton('Мои услуги', callback_data='my_services')
                lg2 = types.InlineKeyboardButton('Мои контакты', callback_data='my_contacts')
                lg3 = types.InlineKeyboardButton('Вход/Регистрация', callback_data='cabinet')
                lg4 = types.InlineKeyboardButton('Оплата', callback_data='pay_services')
                lg5 = types.InlineKeyboardButton('Настройки', callback_data='settings')
                markup.add(lg1, lg2, lg3, lg4, lg5)
                bot.send_message(message.chat.id,
                                 'Главное меню',
                                 reply_markup=markup)
                bot.register_next_step_handler(message, language)

        out = crypt.crypt(message.text, checkUsername["password_hash"])

        if checkUsername["password_hash"] == out:
            min = connection.cursor()
            min.execute(
                'SELECT id,password_hash FROM user WHERE username=%(username)s', {'username': login})

            check = min.fetchall()
            markup_ru = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            lg1 = types.KeyboardButton('Мои услуги')
            lg2 = types.KeyboardButton('Мои контакты')
            lg3 = types.KeyboardButton('Главное меню')

            markup_ru.add(lg1, lg2, lg3)

            bot.send_message(message.chat.id,
                             'Поздравляем! Вы успешно прошли авторизацию!',
                             reply_markup=markup_ru)

            bot.register_next_step_handler(message, after_login)
            # zadoljnsot
            # minus = connection.cursor()
            # minus.execute(
            #     'SELECT `user`.`id`, `user`.`username`, `contact`.`balance` FROM `user`, `contact` WHERE'
            #     ' `user`.`id` = `contact`.`userid` AND `contact`.`balance` < 0'
            #     ' ORDER BY `user`.`id`, `user`.`username`, `contact`.`balance` DESC')
            # checkout = minus.fetchall()
            # for i in checkout:
            #     if login in i.values():
            #         bot.send_message(message.chat.id,
            #                          f'U vas zadoljnost na accounte {i["username"]}: {i["balance"]} sum')
        elif message.text == 'Главное меню':
            markup = types.InlineKeyboardMarkup(row_width=2)
            lg1 = types.InlineKeyboardButton('Мои услуги', callback_data='my_services')
            lg2 = types.InlineKeyboardButton('Мои контакты', callback_data='my_contacts')
            lg3 = types.InlineKeyboardButton('Вход/Регистрация', callback_data='cabinet')
            lg4 = types.InlineKeyboardButton('Оплата', callback_data='pay_services')
            lg5 = types.InlineKeyboardButton('Настройки', callback_data='settings')

            markup.add(lg1, lg2, lg3, lg4, lg5)
            bot.send_message(message.chat.id,
                             'Это информационный бот компании Hostmaster.'
                             '\nHostmaster – Хостинг провайдер и регистратор доменов в'
                             '\nУзбекистане, в Ташкенте.\nНаш телефон: 71-202-55-11',
                             reply_markup=markup)
            bot.register_next_step_handler(message, language)
        else:
            key = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            lg1 = types.KeyboardButton("Главное меню")
            key.add(lg1)
            bot.send_message(message.chat.id, 'Неверный пароль или почта', reply_markup=key)
            bot.register_next_step_handler(message, password)

    login = message.text
    chat_id = message.chat.id
    first_name = message.chat.first_name
    last_name = message.chat.last_name
    username = message.chat.username
    timestamp = message.date
    dt_obj = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
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
        query = "INSERT INTO `sardorbot` (`tg_id`, `tg_username`, `tg_first_name`, `tg_last_name`, `updated`,`b_username`,`b_userid`) " \
                "VALUES ({0},'{1}','{2}','{3}','{4}','{5}','{6}') ON DUPLICATE KEY UPDATE `tg_username` = '{1}', `tg_first_name` = '{2}', `tg_last_name` = '{3}', `updated` = '{4}',`b_username`='{5}',`b_userid`='{6}'".format(
            chat_id, username, first_name, last_name, dt_obj, login, id)

        print(query)
        cursor.execute(query)
    cursor = connection.cursor()
    cursor.execute('SELECT username FROM user')
    checkUsername = cursor.fetchall()
    list = []
    for i in checkUsername:
        list.append(i["username"])

    if message.text.lower() in list:
        cursor.execute('SELECT password_hash FROM user WHERE username=%(username)s', {'username': login})
        checkUsername = cursor.fetchone()
        bot.send_message(message.chat.id, 'Введите пароль:')
        bot.register_next_step_handler(message, password)

    elif message.text == 'Главное меню':
        markup_ru = types.InlineKeyboardMarkup(row_width=2)
        lg1 = types.InlineKeyboardButton('Мои услуги', callback_data='my_services')
        lg2 = types.InlineKeyboardButton('Мои контакты', callback_data='my_contacts')
        lg3 = types.InlineKeyboardButton('Вход/Регистрация', callback_data='cabinet')
        lg4 = types.InlineKeyboardButton('Оплата', callback_data='pay_services')
        lg5 = types.InlineKeyboardButton('Настройки', callback_data='settings')

        markup_ru.add(lg1, lg2, lg3, lg4, lg5)

        bot.send_message(message.chat.id,
                         'Это информационный бот компании Hostmaster.'
                         '\nHostmaster – Хостинг провайдер и регистратор доменов в'
                         '\nУзбекистане, в Ташкенте.\nНаш телефон: 71-202-55-11',
                         reply_markup=markup_ru)

    else:
        key = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        lg1 = types.KeyboardButton("Главное меню")
        key.add(lg1)
        bot.send_message(message.chat.id, 'Повторите попытку', reply_markup=key)
        bot.register_next_step_handler(message, log)


@bot.message_handler(content_types=['text'])
def log_uz(message):
    def password_uz(message):

        out = crypt.crypt(message.text, checkUsername["password_hash"])
        key = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)

        back = types.KeyboardButton('Bosh sahifa')
        key.add(back)
        if checkUsername["password_hash"] == out:

            # contacts
            min = connection.cursor()
            min.execute(
                'SELECT id,password_hash FROM user WHERE username=%(username)s', {'username': login})

            check = min.fetchall()
            for i in check:
                id = i["id"]

                id_connect = connection.cursor()

                id_connect.execute(
                    'SELECT * FROM contact WHERE userid=%(userid)s', {'userid': id})
                checkContact = id_connect.fetchall()
                text = ''
                num = 1
                for i in checkContact:
                    if i["contactcompany"] == None:
                        text += f'{num}. {i["contactname"]}, balans: {i["balance"]} sum\n\n'
                    else:
                        text += f'{num}. {i["contactcompany"]}, balans: {i["balance"]} sum\n\n'
                    num += 1
                bot.send_message(message.chat.id, text, reply_markup=key)

            # zadoljnsot
            # minus = connection.cursor()
            # minus.execute(
            #     'SELECT `user`.`id`, `user`.`username`, `contact`.`balance` FROM `user`, `contact` WHERE'
            #     ' `user`.`id` = `contact`.`userid` AND `contact`.`balance` < 0'
            #     ' ORDER BY `user`.`id`, `user`.`username`, `contact`.`balance` DESC')
            # checkout = minus.fetchall()
            # for i in checkout:
            #     if login in i.values():
            #         bot.send_message(message.chat.id,
            #                          f'U vas zadoljnost na accounte {i["username"]}: {i["balance"]} sum')

            bot.register_next_step_handler(message, func)
        elif message.text == "Bosh sahifa":
            markup_uz = types.InlineKeyboardMarkup(row_width=2)
            lg1 = types.InlineKeyboardButton("Mijozlarni qo'llab-quvvatlash", callback_data='support')
            lg2 = types.InlineKeyboardButton('Kompaniya veb-sayti', callback_data='web',
                                             url='https://www.hostmaster.uz/')
            lg3 = types.InlineKeyboardButton("Xizmatlar uchun tezkor to'lov", callback_data='payment',
                                             url='https://www.hostmaster.uz/pay')
            lg4 = types.InlineKeyboardButton('Balans', callback_data='Balans')
            lg5 = types.InlineKeyboardButton('Yangiliklar kanali', callback_data='tg_channel',
                                             url='https://t.me/hostmasteruz')

            lg6 = types.InlineKeyboardButton("Xizmatlar va to'lovlar", callback_data='pay_services')
            lg7 = types.InlineKeyboardButton('Sozlamalar', callback_data='Sozlamalar')

            markup_uz.add(lg1, lg2, lg3, lg4, lg5, lg6, lg7)
            bot.send_message(message.chat.id,
                             """Bu Hostmaster kompaniyasining axborot boti.\nHostmaster - Xosting provayderi va domen registratori" \nO'zbekiston,Toshkentda. Bizning telefon: 71-202-55-11""",
                             reply_markup=markup_uz)
        else:
            key = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            lg1 = types.KeyboardButton("Bosh sahifa")
            key.add(lg1)
            bot.send_message(message.chat.id, "Noto'g'ri parol yoki pochta", reply_markup=key)
            bot.register_next_step_handler(message, password_uz)

    login = message.text
    cursor = connection.cursor()
    cursor.execute('SELECT username FROM user')
    checkUsername = cursor.fetchall()
    list = []
    for i in checkUsername:
        list.append(i["username"])
    if message.text.lower() in list:
        cursor.execute('SELECT password_hash FROM user WHERE username=%(username)s', {'username': login})
        checkUsername = cursor.fetchone()
        bot.send_message(message.chat.id, 'Parol kiriting')
        bot.register_next_step_handler(message, password_uz)
    elif message.text == 'Bosh sahifa':
        markup_uz = types.InlineKeyboardMarkup(row_width=2)
        lg1 = types.InlineKeyboardButton("Mijozlarni qo'llab-quvvatlash", callback_data='support')
        lg2 = types.InlineKeyboardButton('Kompaniya veb-sayti', callback_data='web', url='https://www.hostmaster.uz/')
        lg3 = types.InlineKeyboardButton("Xizmatlar uchun tezkor to'lov", callback_data='payment',
                                         url='https://www.hostmaster.uz/pay')
        lg4 = types.InlineKeyboardButton('Balans', callback_data='Balans')
        lg5 = types.InlineKeyboardButton('Yangiliklar kanali', callback_data='tg_channel',
                                         url='https://t.me/hostmasteruz')

        lg6 = types.InlineKeyboardButton("Xizmatlar va to'lovlar", callback_data='pay_services')
        lg7 = types.InlineKeyboardButton('Sozlamalar', callback_data='Sozlamalar')

        markup_uz.add(lg1, lg2, lg3, lg4, lg5, lg6, lg7)
        bot.send_message(message.chat.id,
                         """Bu Hostmaster kompaniyasining axborot boti.\nHostmaster - Xosting provayderi va domen registratori" \nO'zbekiston,Toshkentda. Bizning telefon: 71-202-55-11""",
                         reply_markup=markup_uz)


    elif message.text == "Ro'yxatdan o'tish":
        bot.send_message(message.chat.id, "Siz ro'yxatdan o'tishingiz kerak hostmaster.uz")
    else:
        key = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

        lg1 = types.KeyboardButton("Ro'yxatdan o'tish")
        lg2 = types.KeyboardButton("Bosh sahifa")
        key.add(lg1, lg2)
        bot.send_message(message.chat.id, "Yana urinib ko'ring", reply_markup=key)
        bot.register_next_step_handler(message, log_uz)


@bot.message_handler(content_types=['text'])
def language(message):
    if message.text == '🇺🇿Uzbek🇺🇿':
        markup_uz = types.InlineKeyboardMarkup(row_width=2)
        lg1 = types.InlineKeyboardButton("Mijozlarni qo'llab-quvvatlash", callback_data='support')
        lg2 = types.InlineKeyboardButton('Kompaniya veb-sayti', callback_data='web', url='https://www.hostmaster.uz/')
        lg3 = types.InlineKeyboardButton("Xizmatlar uchun tezkor to'lov", callback_data='payment',
                                         url='https://www.hostmaster.uz/pay')
        lg4 = types.InlineKeyboardButton('Balans', callback_data='Balans')
        lg5 = types.InlineKeyboardButton('Yangiliklar kanali', callback_data='tg_channel',
                                         url='https://t.me/hostmasteruz')

        lg6 = types.InlineKeyboardButton("Xizmatlar va to'lovlar", callback_data='pay_services')
        lg7 = types.InlineKeyboardButton('Sozlamalar', callback_data='Sozlamalar')

        markup_uz.add(lg1, lg2, lg3, lg4, lg5, lg6, lg7)
        bot.send_message(message.chat.id,
                         """Bu Hostmaster kompaniyasining axborot boti.\nHostmaster - Xosting provayderi va domen registratori" \nO'zbekiston,Toshkentda. Bizning telefon: 71-202-55-11""",
                         reply_markup=markup_uz)

    elif message.text == '🇷🇺Russian🇷🇺':
        markup_ru = types.InlineKeyboardMarkup(row_width=2)
        lg1 = types.InlineKeyboardButton('Мои услуги', callback_data='my_services')
        lg2 = types.InlineKeyboardButton('Мои контакты', callback_data='my_contacts')
        lg3 = types.InlineKeyboardButton('Вход/Регистрация', callback_data='cabinet')
        lg4 = types.InlineKeyboardButton('Оплата', callback_data='pay_services')
        lg5 = types.InlineKeyboardButton('Настройки', callback_data='settings')

        markup_ru.add(lg1, lg2, lg3, lg4, lg5)

        bot.send_message(message.chat.id,
                         'Это информационный бот компании Hostmaster.'
                         '\nHostmaster – Хостинг провайдер и регистратор доменов в'
                         '\nУзбекистане, в Ташкенте.\nНаш телефон: 71-202-55-11',
                         reply_markup=markup_ru)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == 'cabinet':
        mark = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        reg = types.KeyboardButton('Зарегистрироваться')
        login = types.KeyboardButton('Вход для клиентов')
        menu = types.KeyboardButton('Главное меню')
        mark.add(reg, login, menu)
        bot.send_message(call.message.chat.id, 'Вход/Регистрация', reply_markup=mark)
        bot.register_next_step_handler(call.message, login_reg)

    elif call.data == 'contacts':

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='My contacts',
                              reply_markup=None, parse_mode='html')

    elif call.data == 'settings':
        mark = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        lg1 = types.KeyboardButton('🇷🇺Russian🇷🇺')
        lg2 = types.KeyboardButton('🇺🇿Uzbek🇺🇿')

        mark.add(lg1, lg2)

        bot.send_message(call.message.chat.id, 'Change language', reply_markup=mark)

        bot.register_next_step_handler(call.message, language)

        # uzb
    elif call.data == 'Balans':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=f'Mail kiriting:',
                              reply_markup=None, parse_mode='html')
        bot.register_next_step_handler(call.message, log_uz)

    elif call.data == 'Sozlamalar':
        mark = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        lg1 = types.KeyboardButton('🇷🇺Russian🇷🇺')
        lg2 = types.KeyboardButton('🇺🇿Uzbek🇺🇿')

        mark.add(lg1, lg2)

        bot.send_message(call.message.chat.id, 'Til ozgartirish', reply_markup=mark)

        bot.register_next_step_handler(call.message, language)

#
# def schedule_checker():
#     while True:
#         schedule.run_pending()
#         time.sleep(1)

while True:
    try:
        bot.polling(none_stop=True)

    except Exception as e:
        telebot.logger.error(e)  # или просто print(e) если у вас логгера нет,
        # или import traceback; traceback.print_exc() для печати полной инфы
        time.sleep(15)



# bot.polling(none_stop=True,interval=0)
# if __name__ == "__main__":
#     schedule.every(10).seconds.do(domain_60)
#
#     Thread(target=schedule_checker).start()
