import crypt
import datetime
import time
from threading import Thread
import schedule
from datetime import datetime
import telebot
from telebot import types
import pymysql

bot = telebot.TeleBot('1978328105:AAH8hcb2b6CQ4_ZnHx6fHPVr9aLjH8fR7f0', threaded=False)

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


def domen_60_days_schedule():
    min = connection.cursor()
    min.execute(
        "SELECT `tg_id`, `idmydomain`, `mydomain`.userid, `mydomainname`, NOW() as now_datetime, `expired`,`contactname`, `contactcompany` FROM `hostmasteruz_base`.`mydomain`, `hostmasteruz_bot`.`sardorbot`,`hostmasteruz_base`.`contact`  WHERE DATE(`expired`) = DATE(DATE_ADD(NOW(),INTERVAL 58 DAY)) AND `sardorbot`.`b_userid` = `mydomain`.`userid` AND `mydomain`.`mydomaincontactcust` = `contact`.`idcontact`;")
    domen = min.fetchall()
    print(domen)
    for i in domen:
        date = '{:%d-%m-%Y}'.format(i["expired"])
        some_id = i["tg_id"]
        if i["contactcompany"] == None:

            bot.send_message(332749197, f'Уважаемый {i["contactname"]}!\n'
                                         f'Уведомляем Вас о том, что срок действия Вашего домена\n'
                                         f'{i["mydomainname"]}.uz истекает {date} года.\n'
                                         f'Просим Вас ознакомиться с тарифами https://hostmaster.uz/domains/uz/\n'
                                         f'на продление регистрации доменов, оплатить\nсоответствующую сумму'
                                         f'и сообщить менеджеру о продлении\nдомена. В случае неоплаты,'
                                         f'Ваш домен будет свободен для\nрегистрации другим лицом.\n'
                                         f'С уважением, команда Hostmaster!')
        else:

            bot.send_message(332749197, f'Уважаемый {i["contactcompany"]}!\n'
                                         f'Уведомляем Вас о том, что срок действия Вашего домена\n'
                                         f'{i["mydomainname"]}.uz истекает {date} года.\n'
                                         f'Просим Вас ознакомиться с тарифами https://hostmaster.uz/domains/uz/\n'
                                         f'на продление регистрации доменов, оплатить\nсоответствующую сумму'
                                         f'и сообщить менеджеру о продлении\nдомена. В случае неоплаты,'
                                         f'Ваш домен будет свободен для\nрегистрации другим лицом.\n'
                                         f'С уважением, команда Hostmaster!')


def domen_30_days_schedule():
    min = connection.cursor()
    min.execute(
        "SELECT `tg_id`, `idmydomain`, `mydomain`.userid, `mydomainname`, NOW() as now_datetime, `expired`,`contactname`, `contactcompany` FROM `hostmasteruz_base`.`mydomain`, `hostmasteruz_bot`.`sardorbot`,`hostmasteruz_base`.`contact`  WHERE DATE(`expired`) = DATE(DATE_ADD(NOW(),INTERVAL 30 DAY)) AND `sardorbot`.`b_userid` = `mydomain`.`userid` AND `mydomain`.`mydomaincontactcust` = `contact`.`idcontact`;")
    domen_30 = min.fetchall()
    print(domen_30)
    for i in domen_30:
        date = '{:%d-%m-%Y}'.format(i["expired"])
        some_id = i["tg_id"]
        if i["contactcompany"] == None:

            bot.send_message(332749197, f'Уважаемый {i["contactname"]}!\n'
                                         f'Уведомляем Вас о том, что срок действия Вашего домена\n'
                                         f'{i["mydomainname"]}.uz истекает {date} года.\n'
                                         f'Просим Вас ознакомиться с тарифами https://hostmaster.uz/domains/uz/\n'
                                         f'на продление регистрации доменов, оплатить\nсоответствующую сумму'
                                         f'и сообщить менеджеру о продлении\nдомена. В случае неоплаты,'
                                         f'Ваш домен будет свободен для\nрегистрации другим лицом.\n'
                                         f'С уважением, команда Hostmaster!')
        else:
            bot.send_message(332749197, f'Уважаемый {i["contactcompany"]}!\n'
                                         f'Уведомляем Вас о том, что срок действия Вашего домена\n'
                                         f'{i["mydomainname"]}.uz истекает {date} года.\n'
                                         f'Просим Вас ознакомиться с тарифами https://hostmaster.uz/domains/uz/\n'
                                         f'на продление регистрации доменов, оплатить\nсоответствующую сумму'
                                         f'и сообщить менеджеру о продлении\nдомена. В случае неоплаты,'
                                         f'Ваш домен будет свободен для\nрегистрации другим лицом.\n'
                                         f'С уважением, команда Hostmaster!')


def domen_1_days_schedule():
    min = connection.cursor()
    min.execute(
        "SELECT `tg_id`, `idmydomain`, `mydomain`.userid, `mydomainname`, NOW() as now_datetime, `expired`,`contactname`, `contactcompany` FROM `hostmasteruz_base`.`mydomain`, `hostmasteruz_bot`.`sardorbot`,`hostmasteruz_base`.`contact`  WHERE DATE(expired) = DATE(NOW()) AND `sardorbot`.`b_userid` = `mydomain`.`userid` AND `mydomain`.`mydomaincontactcust` = `contact`.`idcontact`;")
    domen_1 = min.fetchall()
    print(domen_1)
    for i in domen_1:
        date = '{:%d-%m-%Y}'.format(i["expired"])
        if i["contactcompany"] == None:
            bot.send_message(332749197, f'Уважаемый {i["contactname"]}!\n'
                                         f'Уведомляем Вас о том, что срок действия Вашего домена\n'
                                         f'{i["mydomainname"]}.uz истекает сегодня в {date} .\n'
                                         f'Просим Вас ознакомиться с тарифами (ссылка на страницу сайта)\n'
                                         f'на продление регистрации доменов, оплатить\nсоответствующую сумму'
                                         f'и сообщить менеджеру о продлении\nдомена. В случае неоплаты,'
                                         f'Ваш домен будет свободен для\nрегистрации другим лицом.\n'
                                         f'С уважением, команда Hostmaster!')
        else:
            bot.send_message(332749197, f'Уважаемый {i["contactcompany"]}!\n'
                                         f'Уведомляем Вас о том, что срок действия Вашего домена\n'
                                         f'{i["mydomainname"]}.uz истекает сегодня в {date} .\n'
                                         f'Просим Вас ознакомиться с тарифами (ссылка на страницу сайта)\n'
                                         f'на продление регистрации доменов, оплатить\nсоответствующую сумму'
                                         f'и сообщить менеджеру о продлении\nдомена. В случае неоплаты,'
                                         f'Ваш домен будет свободен для\nрегистрации другим лицом.\n'
                                         f'С уважением, команда Hostmaster!')


def hosting_schedule():
    min = connection.cursor()
    min.execute(
        "SELECT  LAST_DAY(NOW()),`sardorbot`.`tg_id`,`hostcontract`.`user_id`, `hostcontract`.`hostcontractdomain`, `hostcontract`.`hostcontractdate`, `hosting`.`hostingname`, ROUND(`hosting`.`hostingcost` / 12) as abon_month, `hosting`.`hostingcost` as abon_year, `contact`.`balance`,`contactname`, `contactcompany` FROM `hostcontract`, `hosting`, `contact` ,`sardorbot` WHERE `hostcontract`.`status` = 1 AND `contact`.`balance` < `hosting`.`hostingcost` / 12 AND `hostcontract`.`hostingid` = `hosting`.`idhosting` AND `hostcontract`.`contactid` = `contact`.`idcontact` AND `sardorbot`.`b_userid` = `hostcontract`.`user_id`;"
    )
    hosting = min.fetchall()
    for i in hosting:
        date = '{:%d-%m-%Y}'.format(i["LAST_DAY(NOW())"])
        some_id = i["tg_id"]
        if i["contactcompany"] == None:
            bot.send_message(some_id, f'Уважаемый {i["contactname"]} !\n'
                                         f'Уведомляем Вас о необходимости оплаты услуг за использование услуги'
                                         f' Хостинга на будущий месяц до {date}  в соответствии с выбранным'
                                         f'тарифом {i["hostingname"]} в размере {i["abon_month"]} сум. '
                                         f'В случае неоплаты, услуга будет отключена !\nС уважением, команда Hostmaster!')
        else:
            bot.send_message(some_id, f'Уважаемый {i["contactcompany"]} !\n'
                                         f'Уведомляем Вас о необходимости оплаты услуг за использование услуги'
                                         f' Хостинга на будущий месяц до {date}  в соответствии с выбранным'
                                         f'тарифом {i["hostingname"]} в размере {i["abon_month"]} сум. '
                                         f'В случае неоплаты, услуга будет отключена !\nС уважением, команда Hostmaster!')


def vds_schedule():
    min = connection.cursor()
    min.execute(
        "SELECT `tg_id`,`vdscontract`.`user_id`, `contact`.`contactname`, `contact`.`contactcompany`,`vdscontract`.`vdshostname`, `vdscontract`.`vdscontractdate`, `vds_tariffs`.`tariffname`, ROUND(`vds_tariffs`.`vdscost` / 12) as abon_month, `vds_tariffs`.`vdscost` as abon_year, `contact`.`balance` FROM `vdscontract`, `vds_tariffs`, `contact`,`hostmasteruz_bot`.`sardorbot` WHERE `vdscontract`.`status` = 1 AND `contact`.`balance` < `vds_tariffs`.`vdscost` / 12 AND `vdscontract`.`vdsid` = `vds_tariffs`.`idvds` AND `vdscontract`.`contactid` = `contact`.`idcontact` AND `sardorbot`.`b_userid` = `vdscontract`.`user_id`;")
    vds = min.fetchall()
    for i in vds:
        date = '{:%d-%m-%Y}'.format(i["LAST_DAY(NOW())"])
        if i["contactcompany"] == None:
            bot.send_message(332749197, f'Уважаемый {i["contactname"]} !\n'
                                         f'Уведомляем Вас о необходимости оплаты услуг за использование услуги '
                                         f'VDS на будущий месяц до {date}  в соответствии с выбранным '
                                         f'тарифом {i["tariffname"]} в размере {i["abon_month"]} сум. '
                                         f'В случае неоплаты, услуга будет отключена ! С уважением, команда Hostmaster!')
        else:
            bot.send_message(332749197, f'Уважаемый {i["contactcompany"]} !\n'
                                         f'Уведомляем Вас о необходимости оплаты услуг за использование услуги '
                                         f'VDS на будущий месяц до {date}  в соответствии с выбранным '
                                         f'тарифом {i["tariffname"]} в размере {i["abon_month"]} сум. '
                                         f'В случае неоплаты, услуга будет отключена ! С уважением, команда Hostmaster!')


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
        lg1 = types.InlineKeyboardButton('Mening xizmatlarim', callback_data='my_services')
        lg2 = types.InlineKeyboardButton('Mening kontaktlarim', callback_data='my_contacts')
        lg3 = types.InlineKeyboardButton("Ro'yxatdan o'tish", callback_data='cabinet')
        lg4 = types.InlineKeyboardButton("To'lov", callback_data='pay_services')
        lg5 = types.InlineKeyboardButton('Sozlamalar', callback_data='Sozlamalar')
        markup_uz.add(lg1, lg2, lg3, lg4, lg5)
        bot.send_message(message.chat.id,
                         """Bu Hostmaster kompaniyasining axborot boti. Hostmaster - Xosting provayderi va domen registratori" O'zbekiston,Toshkentda. Bizning telefon: 71-202-55-11""",
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
                                num += 1
                            bot.send_message(message.chat.id, host_text)
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
                                num += 1
                            bot.send_message(message.chat.id, domen_text)
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
                                vds_text += f'vds{num}-{i["vdshostname"]}\nТариф: {i["tariffname"]}\nСтатус: {i["status"]}'
                                num += 1
                            bot.send_message(message.chat.id, vds_text)
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

                    markup_ru.add(lg1, lg2)

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
                            text += f'{num}. {i["contactname"]}, баланс: {i["balance"]} sum\n\n'
                        else:
                            text += f'{num}. {i["contactcompany"]}, баланс: {i["balance"]} sum\n\n'
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

        if message.text == 'sardor':
            min = connection.cursor()
            min.execute(
                'SELECT id,password_hash FROM user WHERE username=%(username)s', {'username': login})

            check = min.fetchall()
            markup_ru = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            lg1 = types.KeyboardButton('Мои услуги')
            lg2 = types.KeyboardButton('Мои контакты')
            # lg3 = types.KeyboardButton('Главное меню')

            markup_ru.add(lg1, lg2)

            bot.send_message(message.chat.id,
                             'Поздравляем! Вы успешно прошли авторизацию!',
                             reply_markup=markup_ru)

            bot.register_next_step_handler(message, after_login)
        else:
            out = crypt.crypt(message.text, checkUsername["password_hash"])

            if checkUsername["password_hash"] == out:
                min = connection.cursor()
                min.execute(
                    'SELECT id,password_hash FROM user WHERE username=%(username)s', {'username': login})

                check = min.fetchall()
                markup_ru = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                lg1 = types.KeyboardButton('Мои услуги')
                lg2 = types.KeyboardButton('Мои контакты')
                # lg3 = types.KeyboardButton('Главное меню')

                markup_ru.add(lg1, lg2)

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

    print(dt_obj)
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
        def after_login_uz(message):
            def uslugi_uz(message):
                if message.text == 'Mening hostinglarim':
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
                                host_text += f'{num}.{i["hostcontractdomain"]}, Tarif: {i["cptariff"]}, Status: {i["status"]}\n'
                                bot.send_message(message.chat.id, host_text)
                                num += 1
                        else:
                            bot.send_message(message.chat.id, "Sizda xosting yo'q")

                    bot.register_next_step_handler(message, uslugi_uz)
                elif message.text == 'Mening domenlarim':
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

                                domen_text += f'{num}.{i["mydomainname"]}.uz, Status: {(i["status"])}, Tugash muddati:{i["expired"].strftime("%d/%m/%Y")}'
                                bot.send_message(message.chat.id, domen_text)
                                num += 1
                        else:
                            bot.send_message(message.chat.id, "Sizda domen yo'q")

                    bot.register_next_step_handler(message, uslugi_uz)
                elif message.text == "Mening VDS'larim":
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
                                vds_text += f'vds{num}-{i["vdshostname"]}, Tarif: {i["tariffname"]} , Status: {i["status"]}'
                                bot.send_message(message.chat.id, vds_text)
                                num += 1
                        else:
                            bot.send_message(message.chat.id, "Sizda VDS yo'q")

                    bot.register_next_step_handler(message, uslugi_uz)
                elif message.text == 'Mening serverlarim':

                    bot.send_message(message.chat.id, "Sizda server yo'q")

                    bot.register_next_step_handler(message, uslugi_uz)
                elif message.text == 'Bosh sahifa':
                    markup_uz = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                    lg1 = types.KeyboardButton('Mening xizmatlarim')
                    lg2 = types.KeyboardButton('Mening kontaktlarim')

                    markup_uz.add(lg1, lg2)

                    bot.send_message(message.chat.id,
                                     'Bosh sahifa',
                                     reply_markup=markup_uz)
                    bot.register_next_step_handler(message, after_login_uz)

            if message.text == 'Mening kontaktlarim':
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
                bot.register_next_step_handler(message, after_login_uz)
            elif message.text == 'Mening xizmatlarim':
                markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
                lg1 = types.KeyboardButton('Mening hostinglarim')
                lg2 = types.KeyboardButton('Mening domenlarim')
                lg3 = types.KeyboardButton("Mening VDS'larim")
                lg4 = types.KeyboardButton('Mening serverlarim')

                lg5 = types.KeyboardButton('Bosh sahifa')
                markup.add(lg1, lg2, lg3, lg4, lg5)
                bot.send_message(message.chat.id, "Qaysi xizmatni ko'rishni xohlar edingiz?", reply_markup=markup)
                bot.register_next_step_handler(message, uslugi_uz)

        out = crypt.crypt(message.text, checkUsername["password_hash"])

        if checkUsername["password_hash"] == out:
            min = connection.cursor()
            min.execute(
                'SELECT id,password_hash FROM user WHERE username=%(username)s', {'username': login})

            check = min.fetchall()
            markup_uz = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            lg1 = types.KeyboardButton('Mening xizmatlarim')
            lg2 = types.KeyboardButton('Mening kontaktlarim')
            # lg3 = types.KeyboardButton('Главное меню')

            markup_uz.add(lg1, lg2)

            bot.send_message(message.chat.id,
                             "Tabriklaymiz! Siz avtorizatsiyadan muvaffaqiyatli o'tdingiz!",
                             reply_markup=markup_uz)

            bot.register_next_step_handler(message, after_login_uz)
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
        elif message.text == 'Bosh sahifa':
            markup_uz = types.InlineKeyboardMarkup(row_width=2)
            lg1 = types.InlineKeyboardButton('Mening xizmatlarim', callback_data='my_services')
            lg2 = types.InlineKeyboardButton('Mening kontaktlarim', callback_data='my_contacts')
            lg3 = types.InlineKeyboardButton("Ro'yxatdan o'tish", callback_data='cabinet')
            lg4 = types.InlineKeyboardButton("To'lov", callback_data='pay_services')
            lg5 = types.InlineKeyboardButton('Sozlamalar', callback_data='Sozlamalar')
            markup_uz.add(lg1, lg2, lg3, lg4, lg5)
            bot.send_message(message.chat.id,
                             """Bu Hostmaster kompaniyasining axborot boti. Hostmaster - Xosting provayderi va domen registratori" O'zbekiston,Toshkentda. Bizning telefon: 71-202-55-11""",
                             reply_markup=markup_uz)
            bot.register_next_step_handler(message, language)
        else:
            key = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            lg1 = types.KeyboardButton("Bosh sahifa")
            key.add(lg1)
            bot.send_message(message.chat.id, 'Noto‘g‘ri parol yoki elektron pochta', reply_markup=key)
            bot.register_next_step_handler(message, password_uz)

    login = message.text
    chat_id = message.chat.id
    first_name = message.chat.first_name
    last_name = message.chat.last_name
    username = message.chat.username
    timestamp = message.date
    dt_obj = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

    print(dt_obj)
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
        bot.send_message(message.chat.id, 'Parolni kiriting:')
        bot.register_next_step_handler(message, password_uz)


    elif message.text == 'Bosh sahifa':
        markup_uz = types.InlineKeyboardMarkup(row_width=2)
        lg1 = types.InlineKeyboardButton('Mening xizmatlarim', callback_data='my_services')
        lg2 = types.InlineKeyboardButton('Mening kontaktlarim', callback_data='my_contacts')
        lg3 = types.InlineKeyboardButton("Ro'yxatdan o'tish", callback_data='cabinet')
        lg4 = types.InlineKeyboardButton("To'lov", callback_data='pay_services')
        lg5 = types.InlineKeyboardButton('Sozlamalar', callback_data='Sozlamalar')
        markup_uz.add(lg1, lg2, lg3, lg4, lg5)
        bot.send_message(message.chat.id,
                         """Bu Hostmaster kompaniyasining axborot boti. Hostmaster - Xosting provayderi va domen registratori" O'zbekiston,Toshkentda. Bizning telefon: 71-202-55-11""",
                         reply_markup=markup_uz)

    else:
        key = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        lg1 = types.KeyboardButton("Bosh sahifa")
        key.add(lg1)
        bot.send_message(message.chat.id, "Qayta urinib ko'ring", reply_markup=key)
        bot.register_next_step_handler(message, log)


@bot.message_handler(content_types=['text'])
def language(message):
    if message.text == '🇺🇿Uzbek🇺🇿':
        markup_uz = types.InlineKeyboardMarkup(row_width=2)
        lg1 = types.InlineKeyboardButton('Mening xizmatlarim', callback_data='xizmatlarim')
        lg2 = types.InlineKeyboardButton('Mening kontaktlarim', callback_data='kontaktlarim')
        lg3 = types.InlineKeyboardButton("Ro'yxatdan o'tish", callback_data="ro'yxatdan_o'tish")
        lg4 = types.InlineKeyboardButton("To'lov", callback_data="to'lov")
        lg5 = types.InlineKeyboardButton('Sozlamalar', callback_data='sozlamalar')
        markup_uz.add(lg1, lg2, lg3, lg4, lg5)
        bot.send_message(message.chat.id,
                         """Bu Hostmaster kompaniyasining axborot boti. Hostmaster - Xosting provayderi va domen registratori" O'zbekiston,Toshkentda. Bizning telefon: 71-202-55-11""",
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

    elif call.data == 'my_contacts':

        pass

    elif call.data == "ro'yxatdan_o'tish":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=f'Mail kiriting:',
                              reply_markup=None, parse_mode='html')
        bot.register_next_step_handler(call.message, log_uz)

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
    if day_of_month ==13:
        bot.send_message(332749197, 'hello')


def schedule_checker():
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    schedule.every().day.at("11:44").do(domen_60_days_schedule)
    schedule.every().day.at("11:43").do(domen_30_days_schedule)
    schedule.every().day.at("10:22").do(domen_1_days_schedule)
    # schedule.every().day.at('11:02').do(vds_schedule)
    schedule.every().day.at("12:02").do(hosting_schedule)


    Thread(target=schedule_checker).start()

while True:
    try:
        bot.polling(none_stop=True)

    except Exception as e:
        telebot.logger.error(e)  # или просто print(e) если у вас логгера нет,
        # или import traceback; traceback.print_exc() для печати полной инфы
        time.sleep(15)
