import crypt
import datetime
import time
from threading import Thread
import schedule
from datetime import datetime
import telebot
from telebot import types
import pymysql

bot = telebot.TeleBot('1978328105:AAHB4mv6pfCcUm4B-qSy3nSOXCntSoNm9KU', threaded=False)

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
        "SELECT `tg_id`, `idmydomain`, `mydomain`.userid, `mydomainname`, NOW() as now_datetime, `expired`,`contactname`, `contactcompany` FROM `hostmasteruz_base`.`mydomain`, `hostmasteruz_bot`.`sardorbot`,`hostmasteruz_base`.`contact`  WHERE DATE(`expired`) = DATE(DATE_ADD(NOW(),INTERVAL 59 DAY)) AND `sardorbot`.`b_userid` = `mydomain`.`userid` AND `mydomain`.`mydomaincontactcust` = `contact`.`idcontact`;")
    domen = min.fetchall()

    for i in domen:
        date = '{:%d-%m-%Y}'.format(i["expired"])
        some_id = i["tg_id"]
        print('id ', some_id)
        if i["contactcompany"] == None:
            bot.send_message(332749197,
                             f'Уважаемый <b>{i["contactname"]}!</b> Уведомляем Вас о том, '
                             f'что срок действия домена <b>{i["mydomainname"]}.uz</b> истекает <b>{date}</b> '
                             f'года . Для продления регистрации домена Вам необходимо оплатить '
                             f'сумму согласно действующим тарифам через личный кабинет на нашем сайте. '
                             f'В случае неоплаты, ваш домен будет свободен для регистрации другим '
                             f'лицом.\n<b>С уважением, команда Hostmaster!</b>',
                             parse_mode='html')
        else:
            bot.send_message(332749197,
                             f'Уважаемый <b>{i["contactcompany"]}!</b> Уведомляем Вас о том, '
                             f'что срок действия домена <b>{i["mydomainname"]}.uz</b> истекает <b>{date}</b> '
                             f'года . Для продления регистрации домена Вам необходимо оплатить '
                             f'сумму согласно действующим тарифам через личный кабинет на нашем сайте. '
                             f'В случае неоплаты, ваш домен будет свободен для регистрации другим '
                             f'лицом.\n<b>С уважением, команда Hostmaster!</b>',
                             parse_mode='html')


def domen_30_days_schedule():
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

            bot.send_message(332749197, f'Уважаемый <b>{i["contactname"]}!</b> Уведомляем Вас о том, '
                                        f'что срок действия домена <b>{i["mydomainname"]}.uz</b> '
                                        f'истекает <b>{date}</b> '
                                        f'года . Для продления регистрации домена Вам необходимо оплатить '
                                        f'сумму согласно действующим тарифам через личный кабинет на нашем сайте. '
                                        f'В случае неоплаты, ваш домен будет свободен для регистрации другим '
                                        f'лицом.\n<b>С уважением, команда Hostmaster!</b>', parse_mode='html')
        else:
            bot.send_message(332749197, f'Уважаемый <b>{i["contactcompany"]}!</b> Уведомляем Вас о том, '
                                        f'что срок действия домена <b>{i["mydomainname"]}.uz</b> '
                                        f'истекает <b>{date}</b> '
                                        f'года . Для продления регистрации домена Вам необходимо оплатить '
                                        f'сумму согласно действующим тарифам через личный кабинет на нашем сайте. '
                                        f'В случае неоплаты, ваш домен будет свободен для регистрации другим '
                                        f'лицом.\n<b>С уважением, команда Hostmaster!</b>', parse_mode='html')


def domen_10_days_schedule():
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

            bot.send_message(332749197, f'Уважаемый <b>{i["contactname"]}!</b> Уведомляем Вас о том, '
                                        f'что срок действия домена <b>{i["mydomainname"]}.uz</b> '
                                        f'истекает <b>{date}</b> '
                                        f'года . Для продления регистрации домена Вам необходимо оплатить '
                                        f'сумму согласно действующим тарифам через личный кабинет на нашем сайте. '
                                        f'В случае неоплаты, ваш домен будет свободен для регистрации другим '
                                        f'лицом.\n<b>С уважением, команда Hostmaster!</b>', parse_mode='html')
        else:
            bot.send_message(332749197, f'Уважаемый <b>{i["contactcompany"]}!</b> Уведомляем Вас о том, '
                                        f'что срок действия домена <b>{i["mydomainname"]}.uz</b> '
                                        f'истекает <b>{date}</b> '
                                        f'года . Для продления регистрации домена Вам необходимо оплатить '
                                        f'сумму согласно действующим тарифам через личный кабинет на нашем сайте. '
                                        f'В случае неоплаты, ваш домен будет свободен для регистрации другим '
                                        f'лицом.\n<b>С уважением, команда Hostmaster!</b>', parse_mode='html')


def domen_1_days_schedule():
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
            bot.send_message(332749197, f'Уважаемый <b>{i["contactname"]}!</b> Уведомляем Вас о том, '
                                        f'что срок действия домена <b>{i["mydomainname"]}.uz</b> '
                                        f'истек сегодня, <b>{date}</b> года. Для продления регистрации '
                                        f'домена Вам необходимо оплатить сумму согласно действующим '
                                        f'тарифам через личный кабинет на нашем сайте. '
                                        f'В случае неоплаты, ваш домен будет свободен для '
                                        f'регистрации другим лицом.\n<b>С уважением, команда Hostmaster!</b>',
                             parse_mode='html')
        else:
            bot.send_message(332749197, f'Уважаемый <b>{i["contactcompany"]}!</b> Уведомляем Вас о том, '
                                        f'что срок действия домена <b>{i["mydomainname"]}.uz</b> '
                                        f'истек сегодня, <b>{date}</b> года. Для продления регистрации '
                                        f'домена Вам необходимо оплатить сумму согласно действующим '
                                        f'тарифам через личный кабинет на нашем сайте. '
                                        f'В случае неоплаты, ваш домен будет свободен для '
                                        f'регистрации другим лицом.\n<b>С уважением, команда Hostmaster!</b>',
                             parse_mode='html')


def hosting_schedule():
    min = connection.cursor()
    min.execute(
        "SELECT  LAST_DAY(NOW()),`tg_id`,`hostcontract`.`user_id`,"
        " `hostcontract`.`hostcontractdomain`, "
        "`hostcontract`.`hostcontractdate`, `hosting`.`hostingname`,"
        " ROUND(`hosting`.`hostingcost` / 12) as abon_month,"
        " `hosting`.`hostingcost` as abon_year, `contact`.`balance`,"
        "`contactname`, `contactcompany` FROM `hostcontract`, `hosting`, "
        "`contact` ,`hostmasteruz_bot`.`sardorbot` WHERE"
        " `hostcontract`.`status` = 1 AND `contact`.`balance` "
        "< `hosting`.`hostingcost` / 12 AND `hostcontract`.`hostingid` = `hosting`.`idhosting`"
        " AND `hostcontract`.`contactid` = `contact`.`idcontact` "
        "AND `sardorbot`.`b_userid` = `hostcontract`.`user_id`"
    )
    hosting = min.fetchall()
    for i in hosting:
        date = '{:%d-%m-%Y}'.format(i["LAST_DAY(NOW())"])
        some_id = i["tg_id"]
        if i["contactcompany"] is None:
            bot.send_message(some_id, f'Уважаемый <b>{i["contactname"]}</b> !\n'
                                      f'Уведомляем Вас о необходимости оплаты услуг за использование услуги'
                                      f' Хостинга на будущий месяц до <b>{date}</b>  в соответствии с выбранным'
                                      f'тарифом <b>{i["hostingname"]}</b> в размере <b>{i["abon_month"]}</b> сум. '
                                      f'В случае неоплаты, услуга будет отключена !\n'
                                      f'<b>\nС уважением, команда Hostmaster!</b>',
                             parse_mode='html')
        else:
            bot.send_message(some_id, f'Уважаемый <b>{i["contactcompany"]}</b> !\n'
                                      f'Уведомляем Вас о необходимости оплаты услуг за использование услуги'
                                      f' Хостинга на будущий месяц до <b>{date}</b>  в соответствии с выбранным'
                                      f'тарифом <b>{i["hostingname"]}</b> в размере <b>{i["abon_month"]}</b> сум. '
                                      f'В случае неоплаты, услуга будет отключена !\n'
                                      f'<b>\nС уважением, команда Hostmaster!</b>',
                             parse_mode='html')


def vds_schedule():
    min = connection.cursor()
    min.execute(
        "SELECT LAST_DAY(NOW()),`tg_id`,`vdscontract`.`user_id`,"
        " `contact`.`contactname`, `contact`.`contactcompany`,"
        "`vdscontract`.`vdshostname`, `vdscontract`.`vdscontractdate`,"
        " `vds_tariffs`.`tariffname`, ROUND(`vds_tariffs`.`vdscost` / 12) "
        "as abon_month, `vds_tariffs`.`vdscost` as abon_year, "
        "`contact`.`balance` FROM `vdscontract`, `vds_tariffs`,"
        " `contact`,`hostmasteruz_bot`.`sardorbot` WHERE "
        "`vdscontract`.`status` = 1 AND `contact`.`balance` <"
        " `vds_tariffs`.`vdscost` / 12 AND `vdscontract`.`vdsid` = `vds_tariffs`.`idvds` "
        "AND `vdscontract`.`contactid` = `contact`.`idcontact` AND"
        " `sardorbot`.`b_userid` = `vdscontract`.`user_id`")
    vds = min.fetchall()
    for i in vds:
        date = '{:%d-%m-%Y}'.format(i["LAST_DAY(NOW())"])
        some_id = i["tg_id"]
        print(some_id)
        if i["contactcompany"] is None:
            bot.send_message(332749197, f'Уважаемый <b>{i["contactname"]}</b>!\n'
                                        f'Уведомляем Вас о необходимости оплаты услуг за использование услуги '
                                        f'VDS на будущий месяц до <b>{date}</b>  в соответствии с выбранным '
                                        f'тарифом <b>{i["tariffname"]}</b> в размере <b>{i["abon_month"]}</b> сум. '
                                        f'В случае неоплаты, услуга будет отключена ! '
                                        f'<b>\nС уважением, команда Hostmaster!</b>',
                             parse_mode='html')
        else:
            bot.send_message(332749197, f'Уважаемый <b>{i["contactcompany"]}</b> !\n'
                                        f'Уведомляем Вас о необходимости оплаты услуг за использование услуги '
                                        f'VDS на будущий месяц до <b>{date}</b>  в соответствии с выбранным '
                                        f'тарифом <b>{i["tariffname"]}</b> в размере <b>{i["abon_month"]}</b> сум. '
                                        f'В случае неоплаты, услуга будет отключена ! '
                                        f'<b>\nС уважением, команда Hostmaster!</b>',
                             parse_mode='html')


def func(message):
    if message.text == 'Возврат':
        markup = types.InlineKeyboardMarkup(row_width=2)
        lg1 = types.InlineKeyboardButton('Мои услуги', callback_data='my_services')
        lg2 = types.InlineKeyboardButton('Мои контакты', callback_data='my_contacts')
        lg3 = types.InlineKeyboardButton('Авторизация', callback_data='cabinet')
        lg4 = types.InlineKeyboardButton('Связь с менеджером',
                                         callback_data='connect_admin', url='https://t.me/hostmaster_support')
        lg5 = types.InlineKeyboardButton('Перейти на сайт', callback_data='site', url='https://hostmaster.uz/')
        lg6 = types.InlineKeyboardButton('Настройки', callback_data='settings')

        markup.add(lg1, lg2, lg3, lg4, lg5, lg6)
        bot.send_message(message.chat.id,
                         "Это информационный бот компании <b>Hostmaster.</b> "
                         "Hostmaster – Хостинг провайдер и регистратор доменов в "
                         "Узбекистане, в Ташкенте.\nНаш телефон: <b>71-202-55-11</b>",
                         reply_markup=markup, parse_mode='html')


    elif message.text == 'Bosh sahifa':
        markup_uz = types.InlineKeyboardMarkup(row_width=2)
        lg1 = types.InlineKeyboardButton('Mening xizmatlarim', callback_data='xizmatlarim')
        lg2 = types.InlineKeyboardButton('Mening kontaktlarim', callback_data='kontaktlarim')
        lg3 = types.InlineKeyboardButton("Ro'yxatdan o'tish", callback_data="ro'yxatdan_o'tish")
        lg4 = types.InlineKeyboardButton("Menejer bilan aloqa", callback_data="connect_admin",
                                         url='https://t.me/hostmaster_support')
        lg5 = types.InlineKeyboardButton("Saytga o'tish", callback_data="site", url='https://hostmaster.uz/')
        lg6 = types.InlineKeyboardButton('Sozlamalar', callback_data='sozlamalar')
        markup_uz.add(lg1, lg2, lg3, lg4, lg5, lg6)
        bot.send_message(message.chat.id,
                         "Bu <b>Hostmaster</b> kompaniyasining "
                         "axborot boti. Hostmaster - Xosting "
                         "provayderi va domen registratori "
                         "O'zbekiston,Toshkentda. "
                         "Bizning telefon: <b>71-202-55-11</b>",
                         reply_markup=markup_uz, parse_mode='html')


# Start bot
@bot.message_handler(commands=['start', 'menu'])
def send_welcome(message):
    text = f'Bot in action:\nname: <b>{message.from_user.first_name}</b>\n' \
           f'chat_id: <b>{message.chat.id}</b>\n' \
           f'username: <b>@{message.from_user.username}</b>'
    markup = types.InlineKeyboardMarkup(row_width=2)
    lg1 = types.InlineKeyboardButton('Мои услуги', callback_data='my_services')
    lg2 = types.InlineKeyboardButton('Мои контакты', callback_data='my_contacts')
    lg3 = types.InlineKeyboardButton('Авторизация', callback_data='cabinet')
    lg4 = types.InlineKeyboardButton('Связь с менеджером',
                                     callback_data='connect_admin', url='https://t.me/hostmaster_support')
    lg5 = types.InlineKeyboardButton('Перейти на сайт', callback_data='site', url='https://hostmaster.uz/')
    lg6 = types.InlineKeyboardButton('Настройки', callback_data='settings')

    markup.add(lg1, lg2, lg3, lg4, lg5, lg6)
    bot.send_message(332749197, text, parse_mode='html')
    bot.send_message(message.chat.id,
                     "Это информационный бот компании <b>Hostmaster.</b> "
                     "Hostmaster – Хостинг провайдер и регистратор доменов в "
                     "Узбекистане, в Ташкенте.\nНаш телефон: <b>71-202-55-11</b>",
                     reply_markup=markup, parse_mode='html')


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
                                host_text += f'{num}.{i["hostcontractdomain"]}, ' \
                                             f'Тариф: {i["cptariff"]}, Статус: {i["status"]}\n'
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

                                domen_text += f'{num}.{i["mydomainname"]}.uz, ' \
                                              f'Статус: {(i["status"])}, ' \
                                              f'Дата окончания:{i["expired"].strftime("%d/%m/%Y")}'
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
                            'SELECT `vdscontract`.`vdshostname`,'
                            ' `vds_tariffs`.`tariffname` ,'
                            '`vdscontract`.`status`  FROM '
                            '`user`, `vdscontract`, `vds_tariffs`'
                            ' WHERE   username=%(username)s AND '
                            '`user`.`id` = `vdscontract`.`user_id`'
                            ' AND `vdscontract`.`vdsid` = `vds_tariffs`.`idvds`'
                            ' ORDER BY `vdscontract`.`vdshostname`;',
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
                                vds_text += f'<b>vds №{num}</b>. {i["vdshostname"]}\n' \
                                            f'Тариф: {i["tariffname"]}\n' \
                                            f'Статус: {i["status"]}\n'
                                num += 1
                            bot.send_message(message.chat.id, vds_text, parse_mode='html')
                        else:
                            bot.send_message(message.chat.id, 'У вас нет VDS')

                    bot.register_next_step_handler(message, uslugi)
                elif message.text == 'Мои сервера':
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
                                    i["status"] = 'Active'
                                elif i["status"] == 2:
                                    i["status"] = 'Block'
                                ser_text += f'{num}. <b>{i["colhostname"]}</b>, Статус: <b>{i["status"]}</b>\n'
                                num += 1
                            bot.send_message(message.chat.id, ser_text, parse_mode='html')
                        else:
                            bot.send_message(message.chat.id, 'У вас нет сервера')

                    bot.register_next_step_handler(message, uslugi)
                elif message.text == 'Возврат':
                    markup_ru = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
                    lg1 = types.KeyboardButton('Мои услуги')
                    lg2 = types.KeyboardButton('Мои контакты')
                    lg3 = types.KeyboardButton('Возврат')
                    markup_ru.add(lg1, lg2, lg3)
                    bot.send_message(message.chat.id,
                                     "Это информационный бот компании <b>Hostmaster.</b> "
                                     "Hostmaster – Хостинг провайдер и регистратор доменов в "
                                     "Узбекистане, в Ташкенте.\nНаш телефон: <b>71-202-55-11</b>",
                                     reply_markup=markup_ru, parse_mode='html')
                    bot.register_next_step_handler(message, after_login)

            def doljniki(message):
                def doljniki_domen(message):
                    if message.text == '60 дней':
                        min = connection.cursor()
                        min.execute(
                            "SELECT `idmydomain`, `userid`, `mydomainname`, NOW() as now_datetime, `expired` FROM `mydomain` WHERE DATE(`expired`) = DATE(DATE_ADD(NOW(),INTERVAL 60 DAY))")
                        domendays_60 = min.fetchall()
                        days_60 = ''
                        n = 1
                        for i in domendays_60:
                            days_60 += f'{n}. {i["mydomainname"]}.uz\n'
                            n += 1
                        print(days_60)
                        bot.send_message(message.chat.id, days_60)
                        bot.register_next_step_handler(message, doljniki_domen)
                    elif message.text == '30 дней':
                        min = connection.cursor()
                        min.execute(
                            "SELECT `idmydomain`, `userid`, `mydomainname`, "
                            "NOW() as now_datetime, `expired` "
                            "FROM `mydomain` WHERE "
                            "DATE(`expired`) = DATE(DATE_ADD(NOW(),INTERVAL 30 DAY))")
                        domendays_30 = min.fetchall()
                        days_30 = ''
                        n = 1
                        for i in domendays_30:
                            days_30 += f'{n}. {i["mydomainname"]}.uz\n'
                            n += 1
                        print(days_30)
                        bot.send_message(message.chat.id, days_30)
                        bot.register_next_step_handler(message, doljniki_domen)
                    elif message.text == '10 дней':
                        min = connection.cursor()
                        min.execute(
                            "SELECT `idmydomain`, `userid`, "
                            "`mydomainname`, NOW() as now_datetime, "
                            "`expired` FROM `mydomain` "
                            "WHERE DATE(`expired`) = DATE(DATE_ADD(NOW(),INTERVAL 10 DAY))")
                        domendays_10 = min.fetchall()
                        days_10 = ''
                        n = 1
                        for i in domendays_10:
                            days_10 += f'{n}. {i["mydomainname"]}.uz\n'
                            n += 1
                        print(days_10)
                        bot.send_message(message.chat.id, days_10)
                        bot.register_next_step_handler(message, doljniki_domen)
                    elif message.text == 'Сегодня':
                        min = connection.cursor()
                        min.execute(
                            "SELECT `idmydomain`, `userid`,"
                            " `mydomainname`, NOW() as now_datetime, "
                            "`expired` FROM `mydomain` "
                            "WHERE DATE(`expired`) = DATE(NOW())")
                        domendays_1 = min.fetchall()
                        days_1 = ''
                        n = 1
                        for i in domendays_1:
                            days_1 += f'{n}. {i["mydomainname"]}.uz\n'
                            n += 1
                        print(days_1)
                        bot.send_message(message.chat.id, days_1)
                        bot.register_next_step_handler(message, doljniki_domen)
                    elif message.text == 'Redemption':
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
                        bot.register_next_step_handler(message, doljniki_domen)
                    elif message.text == 'Назад':
                        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
                        lg1 = types.KeyboardButton('Домен')
                        lg2 = types.KeyboardButton('Хостинг')
                        lg3 = types.KeyboardButton('VDS')
                        lg4 = types.KeyboardButton('Возврат')
                        markup.add(lg1, lg2, lg3, lg4)
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

                elif message.text == 'Возврат':
                    markup_ru = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
                    lg1 = types.KeyboardButton('Мои услуги')
                    lg2 = types.KeyboardButton('Мои контакты')
                    lg3 = types.KeyboardButton('Уведомления')
                    lg4 = types.KeyboardButton('Возврат')

                    markup_ru.add(lg1, lg2, lg3, lg4)

                    bot.send_message(message.chat.id,
                                     "Это информационный бот компании <b>Hostmaster.</b> "
                                     "Hostmaster – Хостинг провайдер и регистратор доменов в "
                                     "Узбекистане, в Ташкенте.\nНаш телефон: <b>71-202-55-11</b>",

                                     reply_markup=markup_ru, parse_mode='html')
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
                        if i["contactcompany"] is None:
                            text += f'{num}. {i["contactname"]}, Баланс: <b>{i["balance"]} sum</b>\n'
                        else:
                            text += f'{num}. {i["contactcompany"]}, Баланс: <b>{i["balance"]} sum</b>\n'
                        num += 1
                    bot.send_message(message.chat.id, text, parse_mode='html')
                bot.register_next_step_handler(message, after_login)
            elif message.text == 'Мои услуги':
                markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
                lg1 = types.KeyboardButton('Мои хостинги')
                lg2 = types.KeyboardButton('Мои домены')
                lg3 = types.KeyboardButton('Мои VDS')
                lg4 = types.KeyboardButton('Мои сервера')
                lg5 = types.KeyboardButton('Возврат')
                markup.add(lg1, lg2, lg3, lg4, lg5)
                bot.send_message(message.chat.id, 'Мои услуги', reply_markup=markup)
                bot.register_next_step_handler(message, uslugi)
            elif message.text == 'Уведомления':
                markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
                lg1 = types.KeyboardButton('Домен')
                lg2 = types.KeyboardButton('Хостинг')
                lg3 = types.KeyboardButton('VDS')
                lg4 = types.KeyboardButton('Назад')
                markup.add(lg1, lg2, lg3, lg4)
                bot.send_message(message.chat.id, 'Уведомления', reply_markup=markup)
                bot.register_next_step_handler(message, doljniki)
            elif message.text == 'Возврат':
                markup = types.InlineKeyboardMarkup(row_width=2)
                lg1 = types.InlineKeyboardButton('Мои услуги', callback_data='my_services')
                lg2 = types.InlineKeyboardButton('Мои контакты', callback_data='my_contacts')
                lg3 = types.InlineKeyboardButton('Авторизация', callback_data='cabinet')
                lg4 = types.InlineKeyboardButton('Связь с менеджером', callback_data='connect_admin',
                                                 url='https://t.me/hostmaster_support')
                lg5 = types.InlineKeyboardButton('Перейти на сайт', callback_data='site', url='https://hostmaster.uz/')
                lg6 = types.InlineKeyboardButton('Настройки', callback_data='settings')

                markup.add(lg1, lg2, lg3, lg4, lg5, lg6)
                bot.send_message(message.chat.id,
                                 "Это информационный бот компании <b>Hostmaster.</b> "
                                 "Hostmaster – Хостинг провайдер и регистратор доменов в "
                                 "Узбекистане, в Ташкенте.\nНаш телефон: <b>71-202-55-11</b>",
                                 reply_markup=markup, parse_mode='html')

        if message.text == 'sardor':
            min = connection.cursor()
            min.execute(
                'SELECT id,password_hash FROM user WHERE username=%(username)s', {'username': login})

            check = min.fetchall()
            markup_ru = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
            lg1 = types.KeyboardButton('Мои услуги')
            lg2 = types.KeyboardButton('Мои контакты')
            lg3 = types.KeyboardButton('Уведомления')
            lg4 = types.KeyboardButton('Возврат')

            markup_ru.add(lg1, lg2, lg3, lg4)

            bot.send_message(message.chat.id,
                             "Это информационный бот компании <b>Hostmaster.</b> "
                             "Hostmaster – Хостинг провайдер и регистратор доменов в "
                             "Узбекистане, в Ташкенте.\nНаш телефон: <b>71-202-55-11</b>\n"
                             "Поздравляем! Вы успешно прошли авторизацию!",
                             reply_markup=markup_ru, parse_mode='html')
            bot.send_message(332749197,
                             f'{message.from_user.first_name} Successfully authorized for admin')

            bot.register_next_step_handler(message, after_login)
        else:
            out = crypt.crypt(message.text, checkUsername["password_hash"])

            if checkUsername["password_hash"] == out:
                min = connection.cursor()
                min.execute(
                    'SELECT id,password_hash FROM user WHERE username=%(username)s', {'username': login})

                check = min.fetchall()
                markup = types.InlineKeyboardMarkup(row_width=2)
                lg1 = types.InlineKeyboardButton('Мои услуги', callback_data='my_services')
                lg2 = types.InlineKeyboardButton('Мои контакты', callback_data='my_contacts')
                lg3 = types.InlineKeyboardButton('Авторизация', callback_data='cabinet')
                lg4 = types.InlineKeyboardButton('Связь с менеджером', callback_data='connect_admin',
                                                 url='https://t.me/hostmaster_support')
                lg5 = types.InlineKeyboardButton('Перейти на сайт', callback_data='site', url='https://hostmaster.uz/')
                lg6 = types.InlineKeyboardButton('Настройки', callback_data='settings')

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
                                 "Это информационный бот компании <b>Hostmaster.</b> "
                                 "Hostmaster – Хостинг провайдер и регистратор доменов в "
                                 "Узбекистане, в Ташкенте.\nНаш телефон: <b>71-202-55-11</b>\n"
                                 "Поздравляем! Вы успешно прошли авторизацию!",
                                 reply_markup=markup, parse_mode='html')
                bot.send_message(332749197,
                                 f'{message.from_user.first_name} Successfully authorized')
            elif message.text == 'Возврат':
                markup = types.InlineKeyboardMarkup(row_width=2)
                lg1 = types.InlineKeyboardButton('Мои услуги', callback_data='my_services')
                lg2 = types.InlineKeyboardButton('Мои контакты', callback_data='my_contacts')
                lg3 = types.InlineKeyboardButton('Авторизация', callback_data='cabinet')
                lg4 = types.InlineKeyboardButton('Связь с менеджером', callback_data='connect_admin',
                                                 url='https://t.me/hostmaster_support')
                lg5 = types.InlineKeyboardButton('Перейти на сайт', callback_data='site', url='https://hostmaster.uz/')
                lg6 = types.InlineKeyboardButton('Настройки', callback_data='settings')

                markup.add(lg1, lg2, lg3, lg4, lg5, lg6)
                bot.send_message(message.chat.id,
                                 "Это информационный бот компании <b>Hostmaster.</b> "
                                 "Hostmaster – Хостинг провайдер и регистратор доменов в "
                                 "Узбекистане, в Ташкенте.\nНаш телефон: <b>71-202-55-11</b>",
                                 reply_markup=markup, parse_mode='html')

            else:
                key = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
                lg1 = types.KeyboardButton("Возврат")
                key.add(lg1)
                bot.send_message(332749197,
                                 f'{message.from_user.first_name} Cant log in')
                bot.send_message(message.chat.id, 'Неверный пароль или почта', reply_markup=key)

                bot.register_next_step_handler(message, password)

    if message.text == 'Возврат':
        markup = types.InlineKeyboardMarkup(row_width=2)
        lg1 = types.InlineKeyboardButton('Мои услуги', callback_data='my_services')
        lg2 = types.InlineKeyboardButton('Мои контакты', callback_data='my_contacts')
        lg3 = types.InlineKeyboardButton('Авторизация', callback_data='cabinet')
        lg4 = types.InlineKeyboardButton('Связь с менеджером', callback_data='connect_admin',
                                         url='https://t.me/hostmaster_support')
        lg5 = types.InlineKeyboardButton('Перейти на сайт', callback_data='site', url='https://hostmaster.uz/')
        lg6 = types.InlineKeyboardButton('Настройки', callback_data='settings')

        markup.add(lg1, lg2, lg3, lg4, lg5, lg6)
        bot.send_message(message.chat.id,
                         "Это информационный бот компании <b>Hostmaster.</b> "
                         "Hostmaster – Хостинг провайдер и регистратор доменов в "
                         "Узбекистане, в Ташкенте.\nНаш телефон: <b>71-202-55-11</b>",
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

        elif message.text == 'Возврат':
            markup_ru = types.InlineKeyboardMarkup(row_width=2)
            lg1 = types.InlineKeyboardButton('Мои услуги', callback_data='my_services')
            lg2 = types.InlineKeyboardButton('Мои контакты', callback_data='my_contacts')
            lg3 = types.InlineKeyboardButton('Авторизация', callback_data='cabinet')
            lg4 = types.InlineKeyboardButton('Связь с менеджером', callback_data='connect_admin',
                                             url='https://t.me/hostmaster_support')
            lg5 = types.InlineKeyboardButton('Перейти на сайт', callback_data='site', url='https://hostmaster.uz/')
            lg6 = types.InlineKeyboardButton('Настройки', callback_data='settings')

            markup_ru.add(lg1, lg2, lg3, lg4, lg5, lg6)
            bot.send_message(message.chat.id,
                             "Это информационный бот компании <b>Hostmaster.</b> "
                             "Hostmaster – Хостинг провайдер и регистратор доменов в "
                             "Узбекистане, в Ташкенте.\nНаш телефон: <b>71-202-55-11</b>",
                             reply_markup=markup_ru, parse_mode='html')


        else:
            key = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
            lg1 = types.KeyboardButton("Возврат")
            key.add(lg1)
            bot.send_message(message.chat.id, 'Повторите попытку', reply_markup=key)
            bot.send_message(332749197,
                             f'{message.from_user.first_name} Cant log in')
            bot.register_next_step_handler(message, log)


@bot.message_handler(content_types=['text'])
def log_uz(message):
    def password_uz(message):
        def after_login_uz(message):
            def uslugi_uz(message):
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
                                host_text += f'{num}.{i["hostcontractdomain"]},' \
                                             f' Тариф: {i["cptariff"]}, Статус: {i["status"]}\n'
                                num += 1
                            bot.send_message(message.chat.id, host_text)
                        else:
                            bot.send_message(message.chat.id, "У вас нет хостингов")

                    bot.register_next_step_handler(message, uslugi_uz)
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

                                domen_text += f'{num}.{i["mydomainname"]}.uz, ' \
                                              f'Статус: {(i["status"])}, ' \
                                              f'Дата окончания:{i["expired"].strftime("%d/%m/%Y")}'
                                num += 1
                            bot.send_message(message.chat.id, domen_text)
                        else:
                            bot.send_message(message.chat.id, 'У вас нет доменов')

                    bot.register_next_step_handler(message, uslugi_uz)
                elif message.text == 'Мои VDS':
                    for i in check:
                        id = i["id"]
                        id_connect = connection.cursor()
                        id_connect.execute(
                            'SELECT `vdscontract`.`vdshostname`, '
                            '`vds_tariffs`.`tariffname` ,'
                            '`vdscontract`.`status`  FROM '
                            '`user`, `vdscontract`, `vds_tariffs` WHERE '
                            ' username=%(username)s AND `user`.`id` = `vdscontract`.`user_id`'
                            ' AND `vdscontract`.`vdsid` = `vds_tariffs`.`idvds` '
                            'ORDER BY `vdscontract`.`vdshostname`;',
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
                                vds_text += f'<b>vds №{num}</b>. {i["vdshostname"]}\n' \
                                            f'Тариф: {i["tariffname"]}\n' \
                                            f'Статус: {i["status"]}\n'
                                num += 1
                            bot.send_message(message.chat.id, vds_text, parse_mode='html')
                        else:
                            bot.send_message(message.chat.id, 'У вас нет VDS')

                    bot.register_next_step_handler(message, uslugi_uz)
                elif message.text == 'Мои сервера':
                    for i in check:
                        print(i)
                        id = i["user_id"]
                        id_connect = connection.cursor()
                        id_connect.execute(
                            "SELECT * FROM colcontract WHERE user_id=%(user_id)s", {'user_id': id})
                        checkContact = id_connect.fetchall()
                        num = 1
                        ser_text = ''
                        if checkContact:
                            for i in checkContact:
                                ser_text += f'server - {num}. {i["colhostname"]}\nСтатус: {i["status"]}\n'
                                num += 1
                            bot.send_message(message.chat.id, ser_text)
                        else:
                            bot.send_message(message.chat.id, 'У вас нет сервера')

                    bot.register_next_step_handler(message, uslugi_uz)
                elif message.text == 'Возврат':
                    markup_ru = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
                    lg1 = types.KeyboardButton('Мои услуги')
                    lg2 = types.KeyboardButton('Мои контакты')
                    lg3 = types.KeyboardButton('Возврат')
                    markup_ru.add(lg1, lg2, lg3)
                    bot.send_message(message.chat.id,
                                     "Это информационный бот компании <b>Hostmaster.</b> "
                                     "Hostmaster – Хостинг провайдер и регистратор доменов в "
                                     "Узбекистане, в Ташкенте.\nНаш телефон: <b>71-202-55-11</b>",
                                     reply_markup=markup_ru, parse_mode='html')
                    bot.register_next_step_handler(message, after_login_uz)

            def doljniki(message):
                def doljniki_domen(message):
                    if message.text == '60 дней':
                        min = connection.cursor()
                        min.execute(
                            "SELECT `idmydomain`, `userid`,"
                            " `mydomainname`, NOW() as"
                            " now_datetime, `expired` FROM "
                            "`mydomain` WHERE DATE(`expired`) = DATE(DATE_ADD(NOW(),INTERVAL 60 DAY))")
                        domendays_60 = min.fetchall()
                        days_60 = ''
                        n = 1
                        for i in domendays_60:
                            days_60 += f'{n}. {i["mydomainname"]}.uz\n'
                            n += 1
                        print(days_60)
                        bot.send_message(message.chat.id, days_60)
                        bot.register_next_step_handler(message, doljniki_domen)
                    elif message.text == '30 дней':
                        min = connection.cursor()
                        min.execute(
                            "SELECT `idmydomain`, `userid`,"
                            " `mydomainname`, NOW() as now_datetime,"
                            " `expired` FROM `mydomain` "
                            "WHERE DATE(`expired`) = DATE(DATE_ADD(NOW(),INTERVAL 30 DAY))")
                        domendays_30 = min.fetchall()
                        days_30 = ''
                        n = 1
                        for i in domendays_30:
                            days_30 += f'{n}. {i["mydomainname"]}.uz\n'
                            n += 1
                        print(days_30)
                        bot.send_message(message.chat.id, days_30)
                        bot.register_next_step_handler(message, doljniki_domen)
                    elif message.text == '10 дней':
                        min = connection.cursor()
                        min.execute(
                            "SELECT `idmydomain`, `userid`, "
                            "`mydomainname`, NOW() as now_datetime,"
                            " `expired` FROM `mydomain` "
                            "WHERE DATE(`expired`) = DATE(DATE_ADD(NOW(),INTERVAL 10 DAY))")
                        domendays_10 = min.fetchall()
                        days_10 = ''
                        n = 1
                        for i in domendays_10:
                            days_10 += f'{n}. {i["mydomainname"]}.uz\n'
                            n += 1
                        print(days_10)
                        bot.send_message(message.chat.id, days_10)
                        bot.register_next_step_handler(message, doljniki_domen)
                    elif message.text == 'Сегодня':
                        min = connection.cursor()
                        min.execute(
                            "SELECT `idmydomain`, `userid`,"
                            " `mydomainname`, NOW() as now_datetime, "
                            "`expired` FROM `mydomain` WHERE DATE(`expired`) = DATE(NOW())")
                        domendays_1 = min.fetchall()
                        days_1 = ''
                        n = 1
                        for i in domendays_1:
                            days_1 += f'{n}. {i["mydomainname"]}.uz\n'
                            n += 1
                        print(days_1)
                        bot.send_message(message.chat.id, days_1)
                        bot.register_next_step_handler(message, doljniki_domen)
                    elif message.text == 'Redemption':
                        min = connection.cursor()
                        min.execute(
                            "SELECT `idmydomain`, `userid`,"
                            " `mydomainname`, NOW() "
                            "as now_datetime, `expired` FROM `mydomain` WHERE status=3")
                        redemption = min.fetchall()
                        red = ''
                        n = 1
                        for i in redemption:
                            red += f'{n}. {i["mydomainname"]}.uz\n'
                            n += 1
                        print(red)
                        bot.send_message(message.chat.id, red)
                        bot.register_next_step_handler(message, doljniki_domen)
                    elif message.text == 'Назад':
                        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
                        lg1 = types.KeyboardButton('Домен')
                        lg2 = types.KeyboardButton('Хостинг')
                        lg3 = types.KeyboardButton('VDS')
                        lg4 = types.KeyboardButton('Возврат')
                        markup.add(lg1, lg2, lg3, lg4)
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

                elif message.text == 'Возврат':
                    markup_ru = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
                    lg1 = types.KeyboardButton('Мои услуги')
                    lg2 = types.KeyboardButton('Мои контакты')
                    lg3 = types.KeyboardButton('Уведомления')
                    lg4 = types.KeyboardButton('Возврат')

                    markup_ru.add(lg1, lg2, lg3, lg4)

                    bot.send_message(message.chat.id,
                                     "Это информационный бот компании <b>Hostmaster.</b> "
                                     "Hostmaster – Хостинг провайдер и регистратор доменов в "
                                     "Узбекистане, в Ташкенте.\nНаш телефон: <b>71-202-55-11</b>",
                                     reply_markup=markup_ru, parse_mode='html')
                bot.register_next_step_handler(message, after_login_uz)

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
                        if i["contactcompany"] is None:
                            text += f'{num}. {i["contactname"]}, Баланс: <b>{i["balance"]} sum</b>\n'
                        else:
                            text += f'{num}. {i["contactcompany"]}, Баланс: <b>{i["balance"]} sum</b>\n'
                        num += 1
                    bot.send_message(message.chat.id, text, parse_mode='html')
                bot.register_next_step_handler(message, after_login_uz)
            elif message.text == 'Мои услуги':
                markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
                lg1 = types.KeyboardButton('Мои хостинги')
                lg2 = types.KeyboardButton('Мои домены')
                lg3 = types.KeyboardButton('Мои VDS')
                lg4 = types.KeyboardButton('Мои сервера')
                lg5 = types.KeyboardButton('Возврат')
                markup.add(lg1, lg2, lg3, lg4, lg5)
                bot.send_message(message.chat.id, 'Мои услуги', reply_markup=markup)
                bot.register_next_step_handler(message, uslugi_uz)
            elif message.text == 'Уведомления':
                markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
                lg1 = types.KeyboardButton('Домен')
                lg2 = types.KeyboardButton('Хостинг')
                lg3 = types.KeyboardButton('VDS')
                lg4 = types.KeyboardButton('Назад')
                markup.add(lg1, lg2, lg3, lg4)
                bot.send_message(message.chat.id, 'Уведомления', reply_markup=markup)
                bot.register_next_step_handler(message, doljniki)
            elif message.text == 'Возврат':
                markup = types.InlineKeyboardMarkup(row_width=2)
                lg1 = types.InlineKeyboardButton('Мои услуги', callback_data='my_services')
                lg2 = types.InlineKeyboardButton('Мои контакты', callback_data='my_contacts')
                lg3 = types.InlineKeyboardButton('Авторизация', callback_data='cabinet')
                lg4 = types.InlineKeyboardButton('Связь с менеджером', callback_data='connect_admin',
                                                 url='https://t.me/hostmaster_support')
                lg5 = types.InlineKeyboardButton('Перейти на сайт', callback_data='site', url='https://hostmaster.uz/')
                lg6 = types.InlineKeyboardButton('Настройки', callback_data='settings')

                markup.add(lg1, lg2, lg3, lg4, lg5, lg6)
                bot.send_message(message.chat.id,
                                 "Это информационный бот компании <b>Hostmaster.</b> "
                                 "Hostmaster – Хостинг провайдер и регистратор доменов в "
                                 "Узбекистане, в Ташкенте.\nНаш телефон: <b>71-202-55-11</b>",
                                 reply_markup=markup, parse_mode='html')

        if message.text == 'sardor':
            min = connection.cursor()
            min.execute(
                'SELECT id,password_hash FROM user WHERE username=%(username)s', {'username': login})

            check = min.fetchall()
            markup_ru = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
            lg1 = types.KeyboardButton('Мои услуги')
            lg2 = types.KeyboardButton('Мои контакты')
            lg3 = types.KeyboardButton('Уведомления')
            lg4 = types.KeyboardButton('Возврат')

            markup_ru.add(lg1, lg2, lg3, lg4)

            bot.send_message(message.chat.id,
                             'Вы вошли в админ',
                             reply_markup=markup_ru)
            bot.send_message(332749197,
                             f'{message.from_user.first_name} Successfully authorized for admin')

            bot.register_next_step_handler(message, after_login_uz)
        else:
            out = crypt.crypt(message.text, checkUsername["password_hash"])

            if checkUsername["password_hash"] == out:
                min = connection.cursor()
                min.execute(
                    'SELECT id,password_hash FROM user WHERE username=%(username)s', {'username': login})

                check = min.fetchall()
                markup_uz = types.InlineKeyboardMarkup(row_width=2)
                lg1 = types.InlineKeyboardButton('Mening xizmatlarim', callback_data='xizmatlarim')
                lg2 = types.InlineKeyboardButton('Mening kontaktlarim', callback_data='kontaktlarim')
                lg3 = types.InlineKeyboardButton("Ro'yxatdan o'tish", callback_data="ro'yxatdan_o'tish")
                lg4 = types.InlineKeyboardButton("Menejer bilan aloqa", callback_data="connect_admin",
                                                 url='https://t.me/hostmaster_support')
                lg5 = types.InlineKeyboardButton("Saytga o'tish", callback_data="site", url='https://hostmaster.uz/')
                lg6 = types.InlineKeyboardButton('Sozlamalar', callback_data='sozlamalar')
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
                                 "Bu <b>Hostmaster</b> kompaniyasining "
                                 "axborot boti. Hostmaster - Xosting "
                                 "provayderi va domen registratori "
                                 "O'zbekiston,Toshkentda. "
                                 "Bizning telefon: <b>71-202-55-11</b>\n\n"
                                 "<b>Tabriklaymiz! Siz avtorizatsiyadan muvaffaqiyatli o'tdingiz!</b>",
                                 reply_markup=markup_uz, parse_mode='html')
                bot.send_message(332749197,
                                 f'{message.from_user.first_name} Successfully authorized')
            elif message.text == 'Qaytish':
                markup_uz = types.InlineKeyboardMarkup(row_width=2)
                lg1 = types.InlineKeyboardButton('Mening xizmatlarim', callback_data='xizmatlarim')
                lg2 = types.InlineKeyboardButton('Mening kontaktlarim', callback_data='kontaktlarim')
                lg3 = types.InlineKeyboardButton("Ro'yxatdan o'tish", callback_data="ro'yxatdan_o'tish")
                lg4 = types.InlineKeyboardButton("Menejer bilan aloqa", callback_data="connect_admin",
                                                 url='https://t.me/hostmaster_support')
                lg5 = types.InlineKeyboardButton("Saytga o'tish", callback_data="site", url='https://hostmaster.uz/')
                lg6 = types.InlineKeyboardButton('Sozlamalar', callback_data='sozlamalar')
                markup_uz.add(lg1, lg2, lg3, lg4, lg5, lg6)
                bot.send_message(message.chat.id,
                                 "Bu <b>Hostmaster</b> kompaniyasining "
                                 "axborot boti. Hostmaster - Xosting "
                                 "provayderi va domen registratori "
                                 "O'zbekiston,Toshkentda. "
                                 "Bizning telefon: <b>71-202-55-11</b>",
                                 reply_markup=markup_uz, parse_mode='html')

            else:
                key = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
                lg1 = types.KeyboardButton("Qaytish")
                key.add(lg1)
                bot.send_message(332749197,
                                 f'{message.from_user.first_name} Cant log in')
                bot.send_message(message.chat.id, 'Noto‘g‘ri parol yoki elektron pochta', reply_markup=key)

                bot.register_next_step_handler(message, password_uz)

    if message.text == 'Qaytish':
        markup_uz = types.InlineKeyboardMarkup(row_width=2)
        lg1 = types.InlineKeyboardButton('Mening xizmatlarim', callback_data='xizmatlarim')
        lg2 = types.InlineKeyboardButton('Mening kontaktlarim', callback_data='kontaktlarim')
        lg3 = types.InlineKeyboardButton("Ro'yxatdan o'tish", callback_data="ro'yxatdan_o'tish")
        lg4 = types.InlineKeyboardButton("Menejer bilan aloqa", callback_data="connect_admin",
                                         url='https://t.me/hostmaster_support')
        lg5 = types.InlineKeyboardButton("Saytga o'tish", callback_data="site", url='https://hostmaster.uz/')
        lg6 = types.InlineKeyboardButton('Sozlamalar', callback_data='sozlamalar')
        markup_uz.add(lg1, lg2, lg3, lg4, lg5, lg6)
        bot.send_message(message.chat.id,
                         "Bu <b>Hostmaster</b> kompaniyasining "
                         "axborot boti. Hostmaster - Xosting "
                         "provayderi va domen registratori "
                         "O'zbekiston,Toshkentda. "
                         "Bizning telefon: <b>71-202-55-11</b>",
                         reply_markup=markup_uz, parse_mode='html')

    else:
        login = message.text
        chat_id = message.chat.id
        first_name = message.chat.first_name
        last_name = message.chat.last_name
        username = message.chat.username
        timestamp = message.date
        dt_obj = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

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

        elif message.text == 'Qaytish':
            markup_uz = types.InlineKeyboardMarkup(row_width=2)
            lg1 = types.InlineKeyboardButton('Mening xizmatlarim', callback_data='xizmatlarim')
            lg2 = types.InlineKeyboardButton('Mening kontaktlarim', callback_data='kontaktlarim')
            lg3 = types.InlineKeyboardButton("Ro'yxatdan o'tish", callback_data="ro'yxatdan_o'tish")
            lg4 = types.InlineKeyboardButton("Menejer bilan aloqa", callback_data="connect_admin",
                                             url='https://t.me/hostmaster_support')
            lg5 = types.InlineKeyboardButton("Saytga o'tish", callback_data="site", url='https://hostmaster.uz/')
            lg6 = types.InlineKeyboardButton('Sozlamalar', callback_data='sozlamalar')
            markup_uz.add(lg1, lg2, lg3, lg4, lg5, lg6)
            bot.send_message(message.chat.id,
                             "Bu <b>Hostmaster</b> kompaniyasining "
                             "axborot boti. Hostmaster - Xosting "
                             "provayderi va domen registratori "
                             "O'zbekiston,Toshkentda. "
                             "Bizning telefon: <b>71-202-55-11</b>",
                             reply_markup=markup_uz, parse_mode='html')


        else:
            key = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
            lg1 = types.KeyboardButton("Qaytish")
            key.add(lg1)
            bot.send_message(message.chat.id, "Qayta urinib ko'ring", reply_markup=key)
            bot.send_message(332749197,
                             f'{message.from_user.first_name} Cant log in')
            bot.register_next_step_handler(message, log)


@bot.message_handler(content_types=['text'])
def language(message):
    if message.text == '🇺🇿Uzbek🇺🇿':
        markup_uz = types.InlineKeyboardMarkup(row_width=2)
        lg1 = types.InlineKeyboardButton('Mening xizmatlarim', callback_data='xizmatlarim')
        lg2 = types.InlineKeyboardButton('Mening kontaktlarim', callback_data='kontaktlarim')
        lg3 = types.InlineKeyboardButton("Ro'yxatdan o'tish", callback_data="ro'yxatdan_o'tish")
        lg4 = types.InlineKeyboardButton("Menejer bilan aloqa", callback_data="connect_admin",
                                         url='https://t.me/hostmaster_support')
        lg5 = types.InlineKeyboardButton("Saytga o'tish", callback_data="site", url='https://hostmaster.uz/')
        lg6 = types.InlineKeyboardButton('Sozlamalar', callback_data='sozlamalar')
        markup_uz.add(lg1, lg2, lg3, lg4, lg5, lg6)
        bot.send_message(message.chat.id,
                         "Bu <b>Hostmaster</b> kompaniyasining "
                         "axborot boti. Hostmaster - Xosting "
                         "provayderi va domen registratori "
                         "O'zbekiston,Toshkentda. "
                         "Bizning telefon: <b>71-202-55-11</b>",
                         reply_markup=markup_uz, parse_mode='html')

    elif message.text == '🇷🇺Russian🇷🇺':
        markup_ru = types.InlineKeyboardMarkup(row_width=2)
        lg1 = types.InlineKeyboardButton('Мои услуги', callback_data='my_services')
        lg2 = types.InlineKeyboardButton('Мои контакты', callback_data='my_contacts')
        lg3 = types.InlineKeyboardButton('Авторизация', callback_data='cabinet')
        lg4 = types.InlineKeyboardButton('Связь с менеджером', callback_data='connect_admin',
                                         url='https://t.me/hostmaster_support')
        lg5 = types.InlineKeyboardButton('Перейти на сайт', callback_data='site', url='https://hostmaster.uz/')
        lg6 = types.InlineKeyboardButton('Настройки', callback_data='settings')

        markup_ru.add(lg1, lg2, lg3, lg4, lg5, lg6)
        bot.send_message(message.chat.id,
                         "Это информационный бот компании <b>Hostmaster.</b> "
                         "Hostmaster – Хостинг провайдер и регистратор доменов в "
                         "Узбекистане, в Ташкенте.\nНаш телефон: <b>71-202-55-11</b>",
                         reply_markup=markup_ru, parse_mode='html')

    # elif message.text == 'Возврат':
    #     markup = types.InlineKeyboardMarkup(row_width=2)
    #     lg1 = types.InlineKeyboardButton('Мои услуги', callback_data='my_services')
    #     lg2 = types.InlineKeyboardButton('Мои контакты', callback_data='my_contacts')
    #     lg3 = types.InlineKeyboardButton('Авторизация', callback_data='cabinet')
    #     lg4 = types.InlineKeyboardButton('Связь с менеджером', callback_data='connect_admin',
    #                                      url='https://t.me/hostmaster_support')
    #     lg5 = types.InlineKeyboardButton('Перейти на сайт', callback_data='site', url='https://hostmaster.uz/')
    #     lg6 = types.InlineKeyboardButton('Настройки', callback_data='settings')
    #
    #     markup.add(lg1, lg2, lg3, lg4, lg5, lg6)
    #     bot.send_message(message.chat.id,
    #                      "Это информационный бот компании <b>Hostmaster.</b> "
    #                      "Hostmaster – Хостинг провайдер и регистратор доменов в "
    #                      "Узбекистане, в Ташкенте.\nНаш телефон: <b>71-202-55-11</b>",
    #                      reply_markup=markup, parse_mode='html')


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == 'cabinet':
        mark = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        menu = types.KeyboardButton('Возврат')
        mark.add(menu)
        bot.send_message(call.message.chat.id, 'Адрес е-майл:', reply_markup=mark)
        bot.register_next_step_handler(call.message, log)
    elif call.data == 'my_contacts':
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
                text += f'{num}. {i["contactname"]}, Баланс: <b>{i["balance"]} sum</b>\n'
            else:
                text += f'{num}. {i["contactcompany"]}, Баланс: <b>{i["balance"]} sum</b>\n'
            num += 1
        bot.send_message(call.message.chat.id, 'Контакты')
        bot.send_message(call.message.chat.id, text, parse_mode='html')
    elif call.data == 'my_services':
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
            if message.text == 'Мои хостинги':
                for i in check:
                    id = i["b_userid"]
                    id_connect = connection.cursor()
                    id_connect.execute(
                        'SELECT `hostcontract`.*, `hosting`.`hostingname`'
                        ' FROM `hostcontract`, `hosting` WHERE '
                        '`hostcontract`.`status` IN (0,1) and'
                        ' `hostcontract`.`user_id` = %(user_id)s'
                        ' AND `hosting`.`idhosting` = `hostcontract`.`hostingid`',
                        {'user_id': id})
                    checkContact = id_connect.fetchall()
                    num = 1
                    host_text = ''
                    if checkContact:
                        for i in checkContact:
                            if i["status"] == 1:
                                i["status"] = 'Active'
                            host_text += f'{num}. {i["hostcontractdomain"]}, ' \
                                         f'Тариф: <b>{i["hostingname"]}</b>, ' \
                                         f'Статус: <b>{i["status"]}</b>\n'
                            num += 1
                        bot.send_message(message.chat.id, host_text, parse_mode='html')
                    else:
                        bot.send_message(message.chat.id, "У вас нет хостингов")

                bot.register_next_step_handler(message, uslugi)
            elif message.text == 'Мои домены':
                for i in check:
                    id = i["b_userid"]
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

                            domen_text += f'{num}. {i["mydomainname"]}.uz, ' \
                                          f'Активен до <b>{i["expired"].strftime("%d/%m/%Y")}</b>\n'
                            num += 1
                        bot.send_message(message.chat.id, domen_text, parse_mode='html')
                    else:
                        bot.send_message(message.chat.id, 'У вас нет доменов')

                bot.register_next_step_handler(message, uslugi)
            elif message.text == 'Мои VDS':
                for i in check:
                    id = i["b_userid"]
                    id_connect = connection.cursor()
                    id_connect.execute(
                        'SELECT `vdscontract`.`vdshostname`,'
                        ' `vds_tariffs`.`tariffname` ,'
                        '`vdscontract`.`status`  FROM  '
                        '`vdscontract`, `vds_tariffs` WHERE '
                        ' `vdscontract`.`vdsid` = `vds_tariffs`.`idvds` AND user_id=%(user_id)s',
                        {'user_id': id})
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
                            vds_text += f'{num}. {i["vdshostname"]}, ' \
                                        f'Тариф: <b>{i["tariffname"]}</b>, ' \
                                        f'Статус: <b>{i["status"]}</b>\n'
                            num += 1
                        bot.send_message(message.chat.id, vds_text, parse_mode='html')
                    else:
                        bot.send_message(message.chat.id, 'У вас нет VDS')

                bot.register_next_step_handler(message, uslugi)
            elif message.text == 'Мои сервера':
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
                                i["status"] = 'Active'
                            elif i["status"] == 2:
                                i["status"] = 'Block'
                            ser_text += f'{num}. <b>{i["colhostname"]}</b>, Статус: <b>{i["status"]}</b>\n'
                            num += 1
                        bot.send_message(message.chat.id, ser_text, parse_mode='html')
                    else:
                        bot.send_message(message.chat.id, 'У вас нет сервера')

                bot.register_next_step_handler(message, uslugi)
            elif message.text == 'Возврат':
                markup = types.InlineKeyboardMarkup(row_width=2)
                lg1 = types.InlineKeyboardButton('Мои услуги', callback_data='my_services')
                lg2 = types.InlineKeyboardButton('Мои контакты', callback_data='my_contacts')
                lg3 = types.InlineKeyboardButton('Авторизация', callback_data='cabinet')
                lg4 = types.InlineKeyboardButton('Связь с менеджером', callback_data='connect_admin',
                                                 url='https://t.me/hostmaster_support')
                lg5 = types.InlineKeyboardButton('Перейти на сайт', callback_data='site', url='https://hostmaster.uz/')
                lg6 = types.InlineKeyboardButton('Настройки', callback_data='settings')

                markup.add(lg1, lg2, lg3, lg4, lg5, lg6)
                bot.send_message(message.chat.id,
                                 "Это информационный бот компании <b>Hostmaster.</b> "
                                 "Hostmaster – Хостинг провайдер и регистратор доменов в "
                                 "Узбекистане, в Ташкенте.\nНаш телефон: <b>71-202-55-11</b>",
                                 reply_markup=markup, parse_mode='html')

        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
        lg1 = types.KeyboardButton('Мои хостинги')
        lg2 = types.KeyboardButton('Мои домены')
        lg3 = types.KeyboardButton('Мои VDS')
        lg4 = types.KeyboardButton('Мои сервера')

        lg5 = types.KeyboardButton('Возврат')
        markup.add(lg1, lg2, lg3, lg4, lg5)
        bot.send_message(call.message.chat.id, 'Мои услуги', reply_markup=markup)
        bot.register_next_step_handler(call.message, uslugi)
    elif call.data == 'settings':
        mark = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        lg1 = types.KeyboardButton('🇷🇺Russian🇷🇺')
        lg2 = types.KeyboardButton('🇺🇿Uzbek🇺🇿')
        # lg3 = types.KeyboardButton('Возврат')
        mark.add(lg1, lg2)
        bot.send_message(call.message.chat.id, 'Смена языка', reply_markup=mark)
        bot.register_next_step_handler(call.message, language)
    elif call.data == "ro'yxatdan_o'tish":
        mark = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        menu = types.KeyboardButton('Qaytish')
        mark.add(menu)
        bot.send_message(call.message.chat.id, 'Mail pochta manzili:', reply_markup=mark)
        bot.register_next_step_handler(call.message, log_uz)
    elif call.data == 'xizmatlarim':
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
            if message.text == 'Mening xostinglarim':
                for i in check:
                    id = i["b_userid"]
                    id_connect = connection.cursor()
                    id_connect.execute(
                        'SELECT `hostcontract`.*, `hosting`.`hostingname`'
                        ' FROM `hostcontract`, `hosting` WHERE'
                        ' `hostcontract`.`status` IN (0,1) and'
                        ' `hostcontract`.`user_id` = %(user_id)s '
                        'AND `hosting`.`idhosting` = `hostcontract`.`hostingid`',
                        {'user_id': id})
                    checkContact = id_connect.fetchall()
                    num = 1
                    host_text = ''
                    if checkContact:
                        for i in checkContact:
                            if i["status"] == 1:
                                i["status"] = 'Active'
                            host_text += f'{num}. {i["hostcontractdomain"]}, ' \
                                         f'Tarif: <b>{i["hostingname"]}</b>, ' \
                                         f'Holat: <b>{i["status"]}</b>\n'
                            num += 1
                        bot.send_message(message.chat.id, host_text, parse_mode='html')
                    else:
                        bot.send_message(message.chat.id, "Sizda xosting yo'q")

                bot.register_next_step_handler(message, uslugi_uz)
            elif message.text == 'Mening domenlarim':
                for i in check:
                    id = i["b_userid"]
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

                            domen_text += f'{num}. {i["mydomainname"]}.uz, ' \
                                          f'<b>{i["expired"].strftime("%d/%m/%Y")}</b> gacha faol\n'
                            num += 1
                        bot.send_message(message.chat.id, domen_text, parse_mode='html')
                    else:
                        bot.send_message(message.chat.id, "Sizda domen yo'q")

                bot.register_next_step_handler(message, uslugi_uz)
            elif message.text == "Mening VDS'larim":
                for i in check:
                    id = i["b_userid"]
                    id_connect = connection.cursor()
                    id_connect.execute(
                        'SELECT `vdscontract`.`vdshostname`, '
                        '`vds_tariffs`.`tariffname` ,'
                        '`vdscontract`.`status`  FROM  '
                        '`vdscontract`, `vds_tariffs` WHERE '
                        ' `vdscontract`.`vdsid` = `vds_tariffs`.`idvds` AND user_id=%(user_id)s',
                        {'user_id': id})
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
                            vds_text += f'{num}. {i["vdshostname"]}, ' \
                                        f'Tarif: <b>{i["tariffname"]}</b>, ' \
                                        f'Holat: <b>{i["status"]}</b>\n\n'
                            num += 1
                        bot.send_message(message.chat.id, vds_text, parse_mode='html')
                    else:
                        bot.send_message(message.chat.id, "Sizda vds yo'q")

                bot.register_next_step_handler(message, uslugi_uz)
            elif message.text == 'Mening serverlarim':
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
                                i["status"] = 'Active'
                            elif i["status"] == 2:
                                i["status"] = 'Block'
                            ser_text += f'{num}. <b>{i["colhostname"]}</b>, Holat: <b>{i["status"]}</b>\n\n'
                            num += 1
                        bot.send_message(message.chat.id, ser_text, parse_mode='html')
                    else:
                        bot.send_message(message.chat.id, "Sizda server yo'q")

                bot.register_next_step_handler(message, uslugi_uz)
            elif message.text == 'Qaytish':
                markup_uz = types.InlineKeyboardMarkup(row_width=2)
                lg1 = types.InlineKeyboardButton("Mening xizmatlarim", callback_data='xizmatlarim')
                lg2 = types.InlineKeyboardButton("Mening kontaktlarim", callback_data='kontaktlarim')
                lg3 = types.InlineKeyboardButton("Ro'yxatdan o'tish", callback_data="ro'yxatdan_o'tish")
                lg4 = types.InlineKeyboardButton("Menejer bilan aloqa", callback_data="connect_admin",
                                                 url='https://t.me/hostmaster_support')
                lg5 = types.InlineKeyboardButton("Saytga o'tish", callback_data="site", url='https://hostmaster.uz/')
                lg6 = types.InlineKeyboardButton("Sozlamalar", callback_data='sozlamalar')
                markup_uz.add(lg1, lg2, lg3, lg4, lg5, lg6)
                bot.send_message(message.chat.id,
                                 "Bu <b>Hostmaster</b> kompaniyasining "
                                 "axborot boti. Hostmaster - Xosting "
                                 "provayderi va domen registratori "
                                 "O'zbekiston,Toshkentda. "
                                 "Bizning telefon: <b>71-202-55-11</b>",
                                 reply_markup=markup_uz, parse_mode='html')

        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
        lg1 = types.KeyboardButton('Mening xostinglarim')
        lg2 = types.KeyboardButton('Mening domenlarim')
        lg3 = types.KeyboardButton("Mening VDS'larim")
        lg4 = types.KeyboardButton('Mening serverlarim')

        lg5 = types.KeyboardButton('Qaytish')
        markup.add(lg1, lg2, lg3, lg4, lg5)
        bot.send_message(call.message.chat.id, 'Mening xizmatlarim', reply_markup=markup)
        bot.register_next_step_handler(call.message, uslugi_uz)
    elif call.data == 'kontaktlarim':
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
                text += f'{num}. {i["contactname"]}, Balans: <b>{i["balance"]} sum</b>\n'
            else:
                text += f'{num}. {i["contactcompany"]}, Balans: <b>{i["balance"]} sum</b>\n'
            num += 1
        bot.send_message(call.message.chat.id, 'Kontaktlar')
        bot.send_message(call.message.chat.id, text, parse_mode='html')
    elif call.data == 'sozlamalar':
        mark = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        lg1 = types.KeyboardButton('🇷🇺Russian🇷🇺')
        lg2 = types.KeyboardButton('🇺🇿Uzbek🇺🇿')
        mark.add(lg1, lg2)
        bot.send_message(call.message.chat.id, 'Til ozgartirish', reply_markup=mark)

        bot.register_next_step_handler(call.message, language)
    else:
        bot.send_message(call.message.chat.id, 'Неопознанная команда')


def job2():
    day_of_month = datetime.now().day
    print(day_of_month)
    if day_of_month == 13:
        bot.send_message(332749197, 'hello')


def schedule_checker():
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    schedule.every().day.at("09:16").do(domen_60_days_schedule)
    schedule.every().day.at("19:00").do(domen_30_days_schedule)
    schedule.every().day.at("19:00").do(domen_10_days_schedule)
    schedule.every().day.at("19:00").do(domen_1_days_schedule)
    schedule.every().day.at('12:14').do(vds_schedule)
    schedule.every().day.at("12:15").do(hosting_schedule)
    Thread(target=schedule_checker).start()
# while True:
#     try:
bot.polling(none_stop=True)

# except Exception as e:
#     telebot.logger.error(e)  # или просто print(e) если у вас логгера нет,
#     # или import traceback; traceback.print_exc() для печати полной инфы
#     time.sleep(5)
