import crypt
import requests
import schedule as schedule
import telebot
from telebot import types
import pymysql

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


#             # show alert
#             bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
#                                       text="NEW LINE SOLUTIONS")

# i["created_at"] = datetime.fromtimestamp(i["created_at"]).strftime('%d.%B.%Y: %H:%M')

def func(message):
    if message.text == 'Главное меню':
        markup = types.InlineKeyboardMarkup(row_width=2)
        lg1 = types.InlineKeyboardButton('Поддержка клиентов', callback_data='support')
        lg2 = types.InlineKeyboardButton('Веб-сайт компании', callback_data='web', url='https://www.hostmaster.uz/')
        lg3 = types.InlineKeyboardButton('Экспресс-оплата устлу', callback_data='payment',
                                         url='https://www.hostmaster.uz/pay')
        lg4 = types.InlineKeyboardButton('Баланс', callback_data='cabinet')
        lg5 = types.InlineKeyboardButton('Канал новостей', callback_data='tg_channel',
                                         url='https://t.me/hostmasteruz')

        lg6 = types.InlineKeyboardButton('Услуги и платежи', callback_data='pay_services')
        lg7 = types.InlineKeyboardButton('Настройки', callback_data='settings')

        markup.add(lg1, lg2, lg3, lg4, lg5, lg6, lg7)
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


# time
def telegram_bot_sendtext(bot_message):
    bot_token = '1978328105:AAFXdSFd7-1voK87s7WBxu5a-DKPGmW1JN0'
    bot_chatID = '332749197'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


def report():
    with connection:
        min = connection.cursor()
        min.execute(
            'SELECT `user`.`id`, `user`.`username`, `contact`.`balance` FROM `user`, `contact` WHERE'
            ' `user`.`id` = `contact`.`userid` AND `contact`.`balance` < 0'
            ' ORDER BY `user`.`id`, `user`.`username`, `contact`.`balance` DESC')
        check = min.fetchall()
        list = []
        for i in check:
            list.append(f'usernmae: {i["username"]} | balance: {i["balance"]}')

        my_balance = list[:3]
        my_message = 'Уважаемый "Наименование контакта"!\n' \
                     'Ваш баланс: -ХХХХ сум\nУбедительно просим погасить задолженность и ' \
                     'внести оплату за используемые услуги!\n' \
                     'По вопросам просим обращаться @hostmaster_support!'
        telegram_bot_sendtext(my_message)


# schedule.every().day.at("11:53").do(report)
# --------------------------------------------

@bot.message_handler(commands=['start', 'menu'])
def send_welcome(message):
    text = f'<b>{message.from_user.first_name}</b> пишет боту'
    markup = types.InlineKeyboardMarkup(row_width=2)
    lg1 = types.InlineKeyboardButton('Веб-сайт компании', callback_data='web', url='https://www.hostmaster.uz/')
    lg2 = types.InlineKeyboardButton('Поддержка клиентов', callback_data='support')

    lg3 = types.InlineKeyboardButton('Экспресс-оплата устлу', callback_data='payment',
                                     url='https://www.hostmaster.uz/pay')
    lg4 = types.InlineKeyboardButton('Баланс', callback_data='cabinet')
    lg5 = types.InlineKeyboardButton('Канал новостей', callback_data='tg_channel',
                                     url='https://t.me/hostmasteruz')

    lg6 = types.InlineKeyboardButton('Услуги и платежи', callback_data='pay_services')
    lg7 = types.InlineKeyboardButton('Настройки', callback_data='settings')

    markup.add(lg1, lg2, lg3, lg4, lg5, lg6, lg7)

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
                    text += f'Наименование контакта {num}: {i["contactname"]}, баланс: {i["balance"]} сум\n\n'
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
            lg1 = types.InlineKeyboardButton('Поддержка клиентов', callback_data='support')
            lg2 = types.InlineKeyboardButton('Веб-сайт компании', callback_data='web', url='https://www.hostmaster.uz/')
            lg3 = types.InlineKeyboardButton('Экспресс-оплата устлу', callback_data='payment',
                                             url='https://www.hostmaster.uz/pay')
            lg4 = types.InlineKeyboardButton('Баланс', callback_data='cabinet')
            lg5 = types.InlineKeyboardButton('Канал новостей', callback_data='tg_channel',
                                             url='https://t.me/hostmasteruz')

            lg6 = types.InlineKeyboardButton('Услуги и платежи', callback_data='pay_services')
            lg7 = types.InlineKeyboardButton('Настройки', callback_data='settings')

            markup.add(lg1, lg2, lg3, lg4, lg5, lg6, lg7)
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

    if message.text in list:
        cursor.execute('SELECT password_hash FROM user WHERE username=%(username)s', {'username': login})
        checkUsername = cursor.fetchone()
        bot.send_message(message.chat.id, 'Введите пароль:')
        bot.register_next_step_handler(message, password)

    elif message.text == 'Back':
        markup_ru = types.InlineKeyboardMarkup(row_width=2)
        lg1 = types.InlineKeyboardButton('Поддержка клиентов', callback_data='support')
        lg2 = types.InlineKeyboardButton('Веб-сайт компании', callback_data='web', url='https://www.hostmaster.uz/')
        lg3 = types.InlineKeyboardButton('Экспресс-оплата устлу', callback_data='payment',
                                         url='https://www.hostmaster.uz/pay')
        lg4 = types.InlineKeyboardButton('Баланс', callback_data='cabinet')
        lg5 = types.InlineKeyboardButton('Канал новостей', callback_data='tg_channel',
                                         url='https://t.me/hostmasteruz')

        lg6 = types.InlineKeyboardButton('Услуги и платежи', callback_data='pay_services')
        lg7 = types.InlineKeyboardButton('Настройки', callback_data='settings')
        markup_ru.add(lg1, lg2, lg3, lg4, lg5, lg6, lg7)

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
                    text += f'Shartnoma nomi {num}: {i["contactname"]}, balans: {i["balance"]} sum\n\n'
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
    if message.text in list:
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
        lg1 = types.InlineKeyboardButton('Поддержка клиентов', callback_data='support')
        lg2 = types.InlineKeyboardButton('Веб-сайт компании', callback_data='web', url='https://www.hostmaster.uz/')
        lg3 = types.InlineKeyboardButton('Экспресс-оплата устлу', callback_data='payment',
                                         url='https://www.hostmaster.uz/pay')
        lg4 = types.InlineKeyboardButton('Баланс', callback_data='cabinet')
        lg5 = types.InlineKeyboardButton('Канал новостей', callback_data='tg_channel',
                                         url='https://t.me/hostmasteruz')

        lg6 = types.InlineKeyboardButton('Услуги и платежи', callback_data='pay_services')
        lg7 = types.InlineKeyboardButton('Настройки', callback_data='settings')
        markup_ru.add(lg1, lg2, lg3, lg4, lg5, lg6, lg7)

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
        bot.register_next_step_handler(call.message, tarifs)
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


@bot.message_handler(content_types=['text'])
def info(message):
    but = types.InlineKeyboardMarkup(row_width=1)
    order = types.InlineKeyboardButton('Заказать', callback_data='order',
                                       url='https://www.hostmaster.uz/hosting/')
    but.add(order)
    if message.text == 'Enter':
        bot.send_message(message.chat.id,
                         f'\n<b>При оплате за месяц:</b>\n'
                         f'Для посадочных и персональных страниц\n'
                         f'<b>24 900</b> сум/мес\n'
                         f'<b>1 Gb</b> на диске\nСайтов: <b>unlimited</b>\n'
                         f'SSL: сертификат бесплатно'
                         f'\nТрафик: <b>unlimited</b>\nТестовый период 7 дней'
                         f'\nПри оплате за год:\n'
                         f'<b>24 900</b> сум/мес\n<b>238 800</b> сум/год\n'
                         f'Доменов UZ в подарок 1 шт*', parse_mode='html', reply_markup=but)

    elif message.text == 'Назад':
        mark = types.ReplyKeyboardMarkup(row_width=3,
                                         resize_keyboard=True,
                                         one_time_keyboard=True)
        veb_host2_0 = types.KeyboardButton('Veb-хостинг 2.0')
        vip_host = types.KeyboardButton('VIP хостинг')
        wordpress = types.KeyboardButton('Wordpress хостинг')
        resellerlar = types.KeyboardButton('Хостинг для Reseller ')
        vds = types.KeyboardButton('Тарифы VDS')
        back = types.KeyboardButton('Назад')
        mark.add(veb_host2_0, vip_host, wordpress, resellerlar, vds, back)
        bot.send_message(message.chat.id, 'Что вас интересует ?', reply_markup=mark)
        bot.register_next_step_handler(message, tarifs)
    elif message.text == 'Shift':
        bot.send_message(message.chat.id,
                         'Оптимально для сайта небольшой компании: <b>36 900</b> сум/мес'
                         '\n<b>2 Gb</b> на диске\nСайтов: <b>unlimited</b>'
                         '\nSSL: сертификат бесплатно\nТрафик: <b>unlimited</b>'
                         '\nТестовый период 7 дней'
                         f'\nПри оплате за год:\n'
                         f'<b>29 900</b> сум/мес\n<b>358 800</b> сум/год\n'
                         f'Доменов UZ в подарок 1 шт*', parse_mode='html', reply_markup=but)
    elif message.text == 'Control':
        bot.send_message(message.chat.id,
                         f'Идеально для корпоративного сайта: 49 900 сум/мес'
                         f'\n3 Gb на диске\nСайтов: unlimited'
                         f'\nSSL: сертификат бесплатно\nТрафик: unlimited'
                         '\nТестовый период 7 дней'
                         f'\nПри оплате за год:\n'
                         f'<b>39 900</b> сум/мес\n<b>478 800</b> сум/год\n'
                         f'Доменов UZ в подарок 2 шт*', parse_mode='html')
    elif message.text == 'Space':
        bot.send_message(message.chat.id,
                         f'Для старта интернет-магазина: 59 900 сум/мес'
                         f'\n5 Gb на диске\nСайтов - unlimited'
                         f'\nSSL-сертификат бесплатно\nТрафик - unlimited'
                         '\nТестовый период 7 дней'
                         f'\n<b>При оплате за год:</b>\n'
                         f'<b>49 900</b> сум/мес\n<b>598 800</b> сум/год\n'
                         f'Доменов UZ в подарок 2 шт*', parse_mode='html')
    elif message.text == 'VIP 1':
        bot.send_message(message.chat.id,
                         f'Для интернет-магазина или портала: 109 900 сум/мес'
                         f'\n10 Gb на диске\nСайтов - unlimited'
                         f'\nSSL-сертификат бесплатно\nТрафик - unlimited'
                         f'\nТестовый период 7 дней'
                         f'\n<b>При оплате за год:</b>\n'
                         f'<b>99 900</b> сум/мес\n<b>1 198 800</b> сум/год\n'
                         f'Доменов UZ в подарок 3 шт*', parse_mode='html')

    elif message.text == 'VIP 2':
        bot.send_message(message.chat.id,
                         f'Оптимально для Интернет-портала: 159 900 сум/мес'
                         f'\n20 Gb на диске\nСайтов - unlimited'
                         f'\nSSL-сертификат бесплатно\nТрафик - unlimited'
                         f'\nТестовый период 7 дней'
                         f'\n<b>При оплате за год:</b>\n'
                         f'<b>149 900 </b> сум/мес\n<b>1 798 800</b> сум/год\n'
                         f'Доменов UZ в подарок 3 шт*',
                         parse_mode='html')

    elif message.text == 'VIP 3':
        bot.send_message(message.chat.id,
                         f'Много сайтов и доменов): 219 900 сум/мес'
                         f'\n30 Gb на диске\nСайтов - unlimited'
                         f'\nSSL-сертификат бесплатно\nТрафик - unlimited'
                         f'\nТестовый период 7 дней'
                         f'\n<b>При оплате за год:</b>\n'
                         f'<b>199 900</b> сум/мес\n<b>2 398 800</b> сум/год\n'
                         f'Доменов UZ в подарок 5 шт*',
                         parse_mode='html')

    elif message.text == 'VIP 4':
        bot.send_message(message.chat.id,
                         f'Для крупного портала или интернет-магазина: 269 900 сум/мес'
                         f'\n<b>100 Gb</b> на диске\nСайтов - unlimited'
                         f'\nSSL-сертификат бесплатно\nТрафик - unlimited'
                         f'\nТестовый период 7 дней'
                         f'\n<b>При оплате за год:</b>\n'
                         f'<b>249 900</b> сум/мес\n<b>2 998 800</b> сум/год\n'
                         f'Доменов UZ в подарок 5 шт*',
                         parse_mode='html')

    elif message.text == 'WordPress 1':
        bot.send_message(message.chat.id,
                         f'Легко и доступно: 29 900 сум/мес'
                         f'\n<b>1 Gb</b> на диске\nСайтов - unlimited'
                         f'\nSSL-сертификат бесплатно\nТрафик - unlimited',
                         parse_mode='html')

    elif message.text == 'WordPress 2':
        bot.send_message(message.chat.id,
                         f'Легко и доступно: 44 900 сум/мес'
                         f'\n<b>2 Gb</b> на диске\nСайтов - unlimited'
                         f'\nSSL-сертификат бесплатно\nТрафик - unlimited',
                         parse_mode='html')

    elif message.text == 'WordPress 3':
        bot.send_message(message.chat.id,
                         f'Легко и доступно: 59 900 сум/мес'
                         f'\n<b>3 Gb</b> на диске\nСайтов - unlimited'
                         f'\nSSL-сертификат бесплатно\nТрафик - unlimited',
                         parse_mode='html')
    elif message.text == 'WordPress 4':
        bot.send_message(message.chat.id,
                         f'Легко и доступно: 69 900 сум/мес'
                         f'\n<b>5 Gb</b> на диске\nСайтов - unlimited'
                         f'\nSSL-сертификат бесплатно\nТрафик - unlimited',
                         parse_mode='html')
    elif message.text == 'Reseller 1':
        bot.send_message(message.chat.id,
                         f'Легко и доступно: 88 000 сум/мес'
                         f'\nСайтов - unlimited\nSSL-сертификат бесплатно'
                         f'\nТрафик - unlimited',
                         parse_mode='html')
    elif message.text == 'Reseller 2':
        bot.send_message(message.chat.id,
                         f'Легко и доступно: 69 900 сум/мес'
                         f'\n<b>5 Gb</b> на диске\nСайтов - unlimited'
                         f'\nSSL-сертификат бесплатно\nТрафик - unlimited',
                         parse_mode='html')
    elif message.text == 'Reseller 3':
        bot.send_message(message.chat.id,
                         f'Легко и доступно: 69 900 сум/мес'
                         f'\n<b>5 Gb</b> на диске\nСайтов - unlimited'
                         f'\nSSL-сертификат бесплатно\nТрафик - unlimited',
                         parse_mode='html')
    elif message.text == 'Reseller 4':
        bot.send_message(message.chat.id,
                         f'Легко и доступно: 69 900 сум/мес\n<b>5 Gb</b> на диске'
                         f'\nСайтов - unlimited\nSSL-сертификат бесплатно'
                         f'\nТрафик - unlimited',
                         parse_mode='html')
    elif message.text == 'VDS Start':
        bot.send_message(message.chat.id,
                         f'Легко и доступно: 69 900 сум/мес\n<b>5 Gb</b> на диске'
                         f'\nСайтов - unlimited\nSSL-сертификат бесплатно'
                         f'\nТрафик - unlimited',
                         parse_mode='html')
    elif message.text == 'VDS Universal':
        bot.send_message(message.chat.id,
                         f'Легко и доступно: 69 900 сум/мес\n<b>5 Gb</b> на диске'
                         f'\nСайтов - unlimited\nSSL-сертификат бесплатно'
                         f'\nТрафик - unlimited',
                         parse_mode='html')
    elif message.text == 'VDS Master':
        bot.send_message(message.chat.id,
                         f'Легко и доступно: 69 900 сум/мес\n<b>5 Gb</b> на диске'
                         f'\nСайтов - unlimited\nSSL-сертификат бесплатно'
                         f'\nТрафик - unlimited',
                         parse_mode='html')
    elif message.text == 'VDS Profi':
        bot.send_message(message.chat.id,
                         f'Легко и доступно: 69 900 сум/мес\n<b>5 Gb</b> на диске'
                         f'\nСайтов - unlimited\nSSL-сертификат бесплатно'
                         f'\nТрафик - unlimited',
                         parse_mode='html')


@bot.message_handler(content_types=['text'])
def tarifs(message):
    if message.text == 'Veb-хостинг 2.0':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        mar = types.KeyboardButton("Enter")
        mar2 = types.KeyboardButton("Shift")
        mar3 = types.KeyboardButton("Control")
        mar4 = types.KeyboardButton("Space")
        back = types.KeyboardButton('Назад')
        markup.add(mar, mar2, mar3, mar4, back)
        bot.send_message(message.chat.id, 'О каком тарифе хотите получить информацию', reply_markup=markup)
        bot.register_next_step_handler(message, info)

    elif message.text == 'VIP хостинг':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        vip1 = types.KeyboardButton("VIP 1")
        vip2 = types.KeyboardButton("VIP 2")
        vip3 = types.KeyboardButton("VIP 3")
        vip4 = types.KeyboardButton("VIP 4")
        back = types.KeyboardButton('Назад')
        markup.add(vip1, vip2, vip3, vip4, back)
        bot.send_message(message.chat.id, 'О каком тарифе хотите получить информацию', reply_markup=markup)
        bot.register_next_step_handler(message, info)

    elif message.text == 'Wordpress хостинг':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        vip1 = types.KeyboardButton("WordPress 1")
        vip2 = types.KeyboardButton("WordPress 2")
        vip3 = types.KeyboardButton("WordPress 3")
        vip4 = types.KeyboardButton("WordPress 4")
        back = types.KeyboardButton('Назад')
        markup.add(vip1, vip2, vip3, vip4, back)
        bot.send_message(message.chat.id, 'О каком тарифе хотите получить информацию', reply_markup=markup)
        bot.register_next_step_handler(message, info)

    elif message.text == 'Хостинг для Reseller':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        vip1 = types.KeyboardButton("Reseller 1")
        vip2 = types.KeyboardButton("Reseller 2")
        vip3 = types.KeyboardButton("Reseller 3")
        vip4 = types.KeyboardButton("Reseller 4")
        back = types.KeyboardButton('Назад')
        markup.add(vip1, vip2, vip3, vip4, back)
        bot.send_message(message.chat.id, 'О каком тарифе хотите получить информацию', reply_markup=markup)
        bot.register_next_step_handler(message, info)

    elif message.text == 'Тарифы VDS':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        vip1 = types.KeyboardButton("VDS Start")
        vip2 = types.KeyboardButton("VDS Universal")
        vip3 = types.KeyboardButton("VDS Master")
        vip4 = types.KeyboardButton("VDS Profi")
        back = types.KeyboardButton('Назад')
        markup.add(vip1, vip2, vip3, vip4, back)
        bot.send_message(message.chat.id, 'О каком тарифе хотите получить информацию', reply_markup=markup)
        bot.register_next_step_handler(message, info)

    elif message.text == 'Назад':
        markup = types.InlineKeyboardMarkup(row_width=1)

        lg1 = types.InlineKeyboardButton('Поддержка клиентов', callback_data='support')
        lg2 = types.InlineKeyboardButton('Веб-сайт компании', callback_data='web', url='https://www.hostmaster.uz/')
        lg3 = types.InlineKeyboardButton('Экспресс-оплата устлу', callback_data='payment',
                                         url='https://www.hostmaster.uz/pay')
        lg4 = types.InlineKeyboardButton('Баланс', callback_data='cabinet')
        lg5 = types.InlineKeyboardButton('Канал новостей', callback_data='tg_channel',
                                         url='https://t.me/hostmasteruz')

        lg6 = types.InlineKeyboardButton('Услуги и платежи', callback_data='pay_services')

        markup.add(lg1, lg2, lg3, lg4, lg5, lg6)
        bot.send_message(message.chat.id,
                         'Главное меню',
                         reply_markup=markup)


bot.polling(none_stop=True)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
