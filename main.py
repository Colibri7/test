import crypt
import time
import requests
import schedule as schedule
import telebot
from telebot import types
import pymysql
# tgbot
bot = telebot.TeleBot('1978328105:AAFXdSFd7-1voK87s7WBxu5a-DKPGmW1JN0')

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

        markup.add(lg1, lg2, lg3, lg4, lg5, lg6, lg7,lg8)
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
def log(message):
    def password(message):
        out = crypt.crypt(message.text, checkUsername["password_hash"])
        key = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        back = types.KeyboardButton('Главное меню')
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
                        text += f'{num}. {i["contactname"]}, баланс: {i["balance"]} сум\n\n'
                    else:
                        text += f'{num}.{i["contactcompany"]}, баланс: {i["balance"]} сум\n\n'
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
        elif message.text == "Главное меню":
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
        else:
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

    elif message.text == 'Back':
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
    elif message.text == 'Зарегистрировать':
        bot.send_message(message.chat.id, 'Вам следует зарегистрироваться hostmaster.uz')

    else:
        key = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

        lg1 = types.KeyboardButton('Зарегистрировать')
        lg2 = types.KeyboardButton("Back")
        key.add(lg1, lg2)
        bot.send_message(message.chat.id, 'Povtorite popitku ', reply_markup=key)
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
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=f'Введите адрес электронной почты:',
                              reply_markup=None, parse_mode='html')
        bot.register_next_step_handler(call.message, log)
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
