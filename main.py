import crypt
from datetime import timedelta

import telebot

from telebot import types
import pymysql

# tgbot


bot = telebot.TeleBot('1978328105:AAEVkuJU2V7GYXwuXj9dGYTXWNaW41BrzNk')

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


# cur3 = connection.cursor()
# cur3.execute(
#     'SELECT `user`.`id`, `user`.`username`, `contact`.`balance` FROM `user`, `contact` WHERE `user`.`id` = `contact`.`userid` AND `contact`.`balance` < 0 ORDER BY `user`.`id`, `user`.`username`, `contact`.`balance` DESC')
# rows3 = cur3.fetchall()

# i["created_at"] = datetime.fromtimestamp(i["created_at"]).strftime('%d.%B.%Y: %H:%M')


def func(message):
    if message.text == 'Главное меню':
        markup = types.InlineKeyboardMarkup(row_width=2)
        lg1 = types.InlineKeyboardButton('Мои домены', callback_data='my_domains')
        lg2 = types.InlineKeyboardButton('Мои хостинги', callback_data='my_hostings')
        lg3 = types.InlineKeyboardButton('Мои VDS', callback_data='my_vds')
        lg4 = types.InlineKeyboardButton('Мои контакты', callback_data='my_contacts')
        lg5 = types.InlineKeyboardButton('Вход/Регистрация', callback_data='cabinet')

        lg6 = types.InlineKeyboardButton('Оплата', callback_data='pay_services')
        lg7 = types.InlineKeyboardButton('Настройки', callback_data='settings')
        lg8 = types.InlineKeyboardButton('Связь с менедежером', callback_data='connect')

        markup.add(lg1, lg2, lg3, lg4, lg5, lg6, lg7, lg8)
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


@bot.message_handler(commands=['start', 'menu'])
def send_welcome(message):
    text = f'<b>{message.from_user.first_name}</b> пишет боту'
    markup = types.InlineKeyboardMarkup(row_width=2)
    lg1 = types.InlineKeyboardButton('Мои домены', callback_data='my_domains')
    lg2 = types.InlineKeyboardButton('Мои хостинги', callback_data='my_hostings')
    lg3 = types.InlineKeyboardButton('Мои VDS', callback_data='my_vds')
    lg4 = types.InlineKeyboardButton('Мои контакты', callback_data='my_contacts')
    lg5 = types.InlineKeyboardButton('Вход/Регистрация', callback_data='cabinet')

    lg6 = types.InlineKeyboardButton('Оплата', callback_data='pay_services')
    lg7 = types.InlineKeyboardButton('Настройки', callback_data='settings')
    lg8 = types.InlineKeyboardButton('Связь с менедежером', callback_data='connect')

    markup.add(lg1, lg2, lg3, lg4, lg5, lg6, lg7, lg8)

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
        lg1 = types.InlineKeyboardButton('Мои домены', callback_data='my_domains')
        lg2 = types.InlineKeyboardButton('Мои хостинги', callback_data='my_hostings')
        lg3 = types.InlineKeyboardButton('Мои VDS', callback_data='my_vds')
        lg4 = types.InlineKeyboardButton('Мои контакты', callback_data='my_contacts')
        lg5 = types.InlineKeyboardButton('Вход/Регистрация', callback_data='cabinet')

        lg6 = types.InlineKeyboardButton('Оплата', callback_data='pay_services')
        lg7 = types.InlineKeyboardButton('Настройки', callback_data='settings')
        lg8 = types.InlineKeyboardButton('Связь с менедежером', callback_data='connect')

        markup.add(lg1, lg2, lg3, lg4, lg5, lg6, lg7, lg8)
        bot.send_message(message.chat.id,
                         'Главное меню',
                         reply_markup=markup)
        bot.register_next_step_handler(message, language)


@bot.message_handler(content_types=['text'])
def log(message):
    def password(message):
        def after_login(message):
            def order(message):
                def hosting_check(message):
                    def list_tarif(message):
                        def finish(message):

                            if message.text == 'Главное меню':
                                mark = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True,
                                                                 one_time_keyboard=True)
                                domen = types.KeyboardButton('Домен')
                                hosting = types.KeyboardButton('Хостинг')
                                vds_vps = types.KeyboardButton('VDS/VPS')
                                menu = types.KeyboardButton('Главное меню')
                                mark.add(domen, hosting, vds_vps, menu)
                                bot.send_message(message.chat.id, 'Главное меню', reply_markup=mark)
                                bot.register_next_step_handler(message, order)
                            else:
                                text_host = f'name: <b>{message.from_user.first_name}\nusername: @{message.from_user.username}</b>\nnumber: {message.contact.phone_number}\nзаказал Хостинг <b>{tarif}</b>'
                                mark = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True,
                                                                 one_time_keyboard=True)
                                con = types.KeyboardButton('Связаться с менеджером!')
                                menu = types.KeyboardButton('Главное меню')
                                mark.add(con, menu)
                                bot.send_message(message.chat.id,
                                                 'Заказ успешно принят, в ближайшее время наш менеджер свяжется с Вами.',
                                                 reply_markup=mark)
                                bot.send_message(332749197, text_host, parse_mode='html')
                                bot.register_next_step_handler(message, order)

                        if message.text == 'Главное меню':
                            mark = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
                            domen = types.KeyboardButton('Домен')
                            hosting = types.KeyboardButton('Хостинг')
                            vds_vps = types.KeyboardButton('VDS/VPS')
                            menu = types.KeyboardButton('Главное меню')
                            mark.add(domen, hosting, vds_vps, menu)
                            bot.send_message(message.chat.id, 'Главное меню', reply_markup=mark)
                            bot.register_next_step_handler(message, order)
                        else:
                            tarif = message.text
                            keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True,
                                                                 one_time_keyboard=True)
                            reg_btn = types.KeyboardButton(text='Отправить номер телефона', request_contact=True)
                            menu = types.KeyboardButton('Главное меню')
                            keyboard.add(reg_btn, menu)
                            bot.send_message(message.chat.id, 'оставьте свой номер телефона', reply_markup=keyboard)
                            bot.register_next_step_handler(message, finish)

                    if message.text == 'Главное меню':
                        mark = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
                        domen = types.KeyboardButton('Домен')
                        hosting = types.KeyboardButton('Хостинг')
                        vds_vps = types.KeyboardButton('VDS/VPS')
                        menu = types.KeyboardButton('Главное меню')
                        mark.add(domen, hosting, vds_vps, menu)
                        bot.send_message(message.chat.id, 'Главное меню', reply_markup=mark)
                        bot.register_next_step_handler(message, order)
                    else:
                        host_name = message.text
                        tarifs = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
                        start = types.KeyboardButton('Start 60 000 сум')
                        universal = types.KeyboardButton('Universal 120 000 сум')
                        active = types.KeyboardButton('Active 216 000 сум')
                        super = types.KeyboardButton('Super 300 000 сум')
                        mega = types.KeyboardButton('Mega 480 000 сум')
                        menu = types.KeyboardButton('Главное меню')
                        tarifs.add(start, universal, active, super, mega, menu)
                        bot.send_message(message.chat.id, 'Выберите тариф:', reply_markup=tarifs)
                        bot.register_next_step_handler(message, list_tarif)

                def domen_check(message):
                    def domain_order(message):
                        def finish3(message):
                            def payment(message):
                                if message.text == 'Главное меню':
                                    mark = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True,
                                                                     one_time_keyboard=True)
                                    domen = types.KeyboardButton('Домен')
                                    hosting = types.KeyboardButton('Хостинг')
                                    vds_vps = types.KeyboardButton('VDS/VPS')
                                    menu = types.KeyboardButton('Главное меню')
                                    mark.add(domen, hosting, vds_vps, menu)
                                    bot.send_message(message.chat.id, 'Главное меню', reply_markup=mark)
                                    bot.register_next_step_handler(message, order)

                            if message.text == 'Главное меню':
                                mark = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True,
                                                                 one_time_keyboard=True)
                                domen = types.KeyboardButton('Домен')
                                hosting = types.KeyboardButton('Хостинг')
                                vds_vps = types.KeyboardButton('VDS/VPS')
                                menu = types.KeyboardButton('Главное меню')
                                mark.add(domen, hosting, vds_vps, menu)
                                bot.send_message(message.chat.id, 'Главное меню', reply_markup=mark)
                                bot.register_next_step_handler(message, order)

                            else:
                                text_dom = f'name: <b>{message.from_user.first_name}\nusername: @{message.from_user.username}</b>\nnumber: {message.contact.phone_number}\nзабронирован Домен <b>{dom}</b>'
                                bot.send_message(332749197, text_dom, parse_mode='html')
                                mark = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True,
                                                                 one_time_keyboard=True)
                                yes = types.KeyboardButton('Да')
                                later = types.KeyboardButton('Позже')
                                con = types.KeyboardButton('Связаться с менеджером!')
                                menu = types.KeyboardButton('Главное меню')
                                mark.add(yes, later, con, menu)
                                bot.send_message(message.chat.id, 'Домен успешно забронирован! Перейти к оплате.',
                                                 reply_markup=mark)
                                bot.register_next_step_handler(message, payment)

                        if message.text == 'Да':
                            vds = message.text
                            keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True,
                                                                 one_time_keyboard=True)
                            reg_btn = types.KeyboardButton(text='Отправить номер телефона', request_contact=True)
                            menu = types.KeyboardButton('Главное меню')
                            keyboard.add(reg_btn, menu)
                            bot.send_message(message.chat.id, 'оставьте свой номер телефона', reply_markup=keyboard)
                            bot.register_next_step_handler(message, finish3)

                        elif message.text == 'Нет':
                            mark = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
                            domen = types.KeyboardButton('Домен')
                            hosting = types.KeyboardButton('Хостинг')
                            vds_vps = types.KeyboardButton('VDS/VPS')
                            menu = types.KeyboardButton('Главное меню')
                            mark.add(domen, hosting, vds_vps, menu)
                            bot.send_message(message.chat.id, 'Что вы хотите заказать?', reply_markup=mark)
                            bot.register_next_step_handler(message, order)

                    dom = message.text
                    if message.text == 'Главное меню':
                        mark = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
                        domen = types.KeyboardButton('Домен')
                        hosting = types.KeyboardButton('Хостинг')
                        vds_vps = types.KeyboardButton('VDS/VPS')
                        menu = types.KeyboardButton('Главное меню')
                        mark.add(domen, hosting, vds_vps, menu)
                        bot.send_message(message.chat.id, 'Chto xotite zakazat?', reply_markup=mark)
                        bot.register_next_step_handler(message, order)
                    else:
                        domain = connection.cursor()
                        domain.execute(
                            'SELECT mydomainname FROM mydomain')

                        check = domain.fetchall()
                        list = []
                        for i in check:
                            list.append(i["mydomainname"])

                        if dom.lower() in list:
                            bot.send_message(message.chat.id, 'Домен занят')
                            bot.register_next_step_handler(message, domen_check)
                        else:
                            mark = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
                            yes = types.KeyboardButton('Да')
                            no = types.KeyboardButton('Нет')
                            mark.add(yes, no)
                            bot.send_message(message.chat.id, 'Домен свободен! Забронировать ?', reply_markup=mark)
                            bot.register_next_step_handler(message, domain_order)
                            bot.send_message(message.from_user.first_name, 'Order domain')

                def vds_vps(message):
                    def finish2(message):
                        if message.text == 'Главное меню':
                            mark = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
                            domen = types.KeyboardButton('Домен')
                            hosting = types.KeyboardButton('Хостинг')
                            vds_vps = types.KeyboardButton('VDS/VPS')
                            menu = types.KeyboardButton('Главное меню')
                            mark.add(domen, hosting, vds_vps, menu)
                            bot.send_message(message.chat.id, 'Главное меню', reply_markup=mark)
                            bot.register_next_step_handler(message, order)
                        else:

                            text_host = f'name: <b>{message.from_user.first_name}\nusername: @{message.from_user.username}</b>\nnumber: {message.contact.phone_number}\nзаказал vds <b>{vds}</b>'
                            mark = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True,
                                                             one_time_keyboard=True)
                            con = types.KeyboardButton('Связаться с менеджером!')
                            menu = types.KeyboardButton('Главное меню')
                            mark.add(con, menu)
                            bot.send_message(message.chat.id,
                                             'Заказ успешно принят, в ближайшее время наш менеджер свяжется с Вами.',
                                             reply_markup=mark)

                            bot.send_message(332749197, text_host, parse_mode='html')
                            bot.register_next_step_handler(message, order)

                    if message.text == 'Главное меню':
                        mark = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
                        domen = types.KeyboardButton('Домен')
                        hosting = types.KeyboardButton('Хостинг')
                        vds_vps = types.KeyboardButton('VDS/VPS')
                        menu = types.KeyboardButton('Главное меню')
                        mark.add(domen, hosting, vds_vps, menu)
                        bot.send_message(message.chat.id, 'Главное меню', reply_markup=mark)
                        bot.register_next_step_handler(message, order)
                    else:
                        vds = message.text
                        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True,
                                                             one_time_keyboard=True)
                        reg_btn = types.KeyboardButton(text='Отправить номер телефона', request_contact=True)
                        menu = types.KeyboardButton('Главное меню')
                        keyboard.add(reg_btn, menu)
                        bot.send_message(message.chat.id, 'оставьте свой номер телефона', reply_markup=keyboard)
                        bot.register_next_step_handler(message, finish2)

                if message.text == 'Домен':
                    mark = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                    back = types.KeyboardButton('Главное меню')
                    mark.add(back)
                    bot.send_message(message.chat.id, f'Заказ новго домена UZ\nВведите домен: ……. .UZ. ',
                                     reply_markup=mark)
                    bot.register_next_step_handler(message, domen_check)
                elif message.text == 'Хостинг':
                    mark = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
                    back = types.KeyboardButton('Главное меню')
                    mark.add(back)
                    bot.send_message(message.chat.id, f'Введите название домена, для которого Вы желаете хостинг:',
                                     reply_markup=mark)
                    bot.register_next_step_handler(message, hosting_check)
                elif message.text == 'VDS/VPS':
                    vds_tarif = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
                    vds1 = types.KeyboardButton('VDS-1')
                    vds2 = types.KeyboardButton('VDS-2')
                    vds3 = types.KeyboardButton('VDS-3')
                    vds4 = types.KeyboardButton('VDS-4')
                    vds5 = types.KeyboardButton('VDS-5')
                    back = types.KeyboardButton('Главное меню')
                    vds_tarif.add(vds1, vds2, vds3, vds4, vds5, back)

                    bot.send_message(message.chat.id, f'Выберите тариф:',
                                     reply_markup=vds_tarif)
                    bot.register_next_step_handler(message, vds_vps)
                elif message.text == 'Главное меню':
                    markup_ru = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
                    lg1 = types.KeyboardButton('Мои домены')
                    lg2 = types.KeyboardButton('Мои хостинги')
                    lg3 = types.KeyboardButton('Мои VDS')
                    lg4 = types.KeyboardButton('Мои контакты')
                    lg5 = types.KeyboardButton('Заказать')
                    lg6 = types.KeyboardButton('Оплата')
                    lg7 = types.KeyboardButton('Настройки')
                    lg8 = types.KeyboardButton('Связь с менедежером')
                    markup_ru.add(lg1, lg2, lg3, lg4, lg5, lg6, lg7, lg8)
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
            elif message.text == 'Мои хостинги':
                for i in check:
                    id = i["id"]
                    id_connect = connection.cursor()
                    id_connect.execute(
                        'SELECT * FROM hostcontract WHERE status=1 and user_id=%(user_id)s', {'user_id': id})
                    checkContact = id_connect.fetchall()
                    num = 1
                    if checkContact:
                        for i in checkContact:
                            if i["status"] == 1:
                                i["status"] = 'Active'
                            bot.send_message(message.chat.id,
                                             f'{num}.{i["hostcontractdomain"]}, Тариф: {i["cptariff"]}, Статус: {i["status"]}\n')
                            num+=1
                    else:
                        bot.send_message(message.chat.id, "У вас нет хостингов")

                bot.register_next_step_handler(message, after_login)
            elif message.text == 'Мои домены':
                for i in check:
                    id = i["id"]
                    id_connect = connection.cursor()
                    id_connect.execute(
                        'SELECT * FROM mydomain WHERE status IN (-2,0,1,3) and userid=%(userid)s', {'userid': id})
                    checkContact = id_connect.fetchall()
                    num = 1
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
                            bot.send_message(message.chat.id,
                                             f'{num}.{i["mydomainname"]}, Статус: {i["status"]}, Дата окончания: {(i["expired"] + timedelta(hours=5)).strftime("%d/%m/%Y")}\n')
                            num+=1
                    else:
                        bot.send_message(message.chat.id, 'У вас нет доменов')

                bot.register_next_step_handler(message, after_login)
            elif message.text == 'Мои VDS':
                for i in check:
                    id = i["id"]
                    id_connect = connection.cursor()
                    id_connect.execute(
                        'SELECT `vdscontract`.`vdshostname`, `vds_tariffs`.`tariffname` ,`vdscontract`.`status`  FROM `user`, `vdscontract`, `vds_tariffs` WHERE   username=%(username)s AND `user`.`id` = `vdscontract`.`user_id` AND `vdscontract`.`vdsid` = `vds_tariffs`.`idvds` ORDER BY `vdscontract`.`vdshostname`;',
                        {'username': login})
                    checkContact = id_connect.fetchall()
                    num = 1
                    if checkContact:
                        for i in checkContact:
                            if i["status"] == 1:
                                i["status"] = 'Active'
                            elif i["status"] == 0:
                                i["status"] = 'Block'
                            else:
                                i["status"] = 'Deleted'

                            bot.send_message(message.chat.id,
                                             f'vds{num}-{i["vdshostname"]}, Тариф: {i["tariffname"]} , Статус: {i["status"]}')
                            num += 1
                    else:
                        bot.send_message(message.chat.id, 'У вас нет VDS')

                bot.register_next_step_handler(message, after_login)
            elif message.text == 'Заказать':
                mark = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
                domen = types.KeyboardButton('Домен')
                hosting = types.KeyboardButton('Хостинг')
                vds_vps = types.KeyboardButton('VDS/VPS')
                menu = types.KeyboardButton('Главное меню')
                mark.add(domen, hosting, vds_vps, menu)
                bot.send_message(message.chat.id, 'Chto xotite zakazat?', reply_markup=mark)
                bot.register_next_step_handler(message, order)

        out = crypt.crypt(message.text, checkUsername["password_hash"])

        if checkUsername["password_hash"] == out:
            min = connection.cursor()
            min.execute(
                'SELECT id,password_hash FROM user WHERE username=%(username)s', {'username': login})

            check = min.fetchall()
            markup_ru = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
            lg1 = types.KeyboardButton('Мои домены')
            lg2 = types.KeyboardButton('Мои хостинги')
            lg3 = types.KeyboardButton('Мои VDS')
            lg4 = types.KeyboardButton('Мои контакты')
            lg5 = types.KeyboardButton('Заказать')

            lg6 = types.KeyboardButton('Оплата')
            lg7 = types.KeyboardButton('Настройки')
            lg8 = types.KeyboardButton('Связь с менедежером')

            markup_ru.add(lg1, lg2, lg3, lg4, lg5, lg6, lg7, lg8)

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
            lg1 = types.InlineKeyboardButton('Мои домены', callback_data='my_domains')
            lg2 = types.InlineKeyboardButton('Мои хостинги', callback_data='my_hostings')
            lg3 = types.InlineKeyboardButton('Мои VDS', callback_data='my_vds')
            lg4 = types.InlineKeyboardButton('Мои контакты', callback_data='my_contacts')
            lg5 = types.InlineKeyboardButton('Вход/Регистрация', callback_data='cabinet')

            lg6 = types.InlineKeyboardButton('Оплата', callback_data='pay_services')
            lg7 = types.InlineKeyboardButton('Настройки', callback_data='settings')
            lg8 = types.InlineKeyboardButton('Связь с менедежером', callback_data='connect')

            markup.add(lg1, lg2, lg3, lg4, lg5, lg6, lg7, lg8)
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
        lg1 = types.InlineKeyboardButton('Мои домены', callback_data='my_domains')
        lg2 = types.InlineKeyboardButton('Мои хостинги', callback_data='my_hostings')
        lg3 = types.InlineKeyboardButton('Мои VDS', callback_data='my_vds')
        lg4 = types.InlineKeyboardButton('Мои контакты', callback_data='my_contacts')
        lg5 = types.InlineKeyboardButton('Вход/Регистрация', callback_data='cabinet')

        lg6 = types.InlineKeyboardButton('Оплата', callback_data='pay_services')
        lg7 = types.InlineKeyboardButton('Настройки', callback_data='settings')
        lg8 = types.InlineKeyboardButton('Связь с менедежером', callback_data='connect')

        markup_ru.add(lg1, lg2, lg3, lg4, lg5, lg6, lg7, lg8)

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
        lg1 = types.InlineKeyboardButton('Мои домены', callback_data='my_domains')
        lg2 = types.InlineKeyboardButton('Мои хостинги', callback_data='my_hostings')
        lg3 = types.InlineKeyboardButton('Мои VDS', callback_data='my_vds')
        lg4 = types.InlineKeyboardButton('Мои контакты', callback_data='my_contacts')
        lg5 = types.InlineKeyboardButton('Вход/Регистрация', callback_data='cabinet')

        lg6 = types.InlineKeyboardButton('Оплата', callback_data='pay_services')
        lg7 = types.InlineKeyboardButton('Настройки', callback_data='settings')
        lg8 = types.InlineKeyboardButton('Связь с менедежером', callback_data='connect')

        markup_ru.add(lg1, lg2, lg3, lg4, lg5, lg6, lg7, lg8)

        bot.send_message(message.chat.id,
                         'Это информационный бот компании Hostmaster.'
                         '\nHostmaster – Хостинг провайдер и регистратор доменов в'
                         '\nУзбекистане, в Ташкенте.\nНаш телефон: 71-202-55-11',
                         reply_markup=markup_ru)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == 'pay_services':
        mark = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True, one_time_keyboard=True)
        veb_host2_0 = types.KeyboardButton('Veb-хостинг 2.0')
        vip_host = types.KeyboardButton('VIP хостинг')
        wordpress = types.KeyboardButton('Wordpress хостинг')
        resellerlar = types.KeyboardButton('Хостинг для Reseller ')
        vds = types.KeyboardButton('Тарифы VDS')
        back = types.KeyboardButton('Назад')
        mark.add(veb_host2_0, vip_host, wordpress, resellerlar, vds, back)
        bot.send_message(call.message.chat.id, 'Что вас интересует ?', reply_markup=mark)

    elif call.data == 'cabinet':
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


bot.polling(none_stop=True)
