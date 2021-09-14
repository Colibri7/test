import telebot
import sqlite3
from telebot import types
from telebot.types import Message

bot = telebot.TeleBot('1978328105:AAFXdSFd7-1voK87s7WBxu5a-DKPGmW1JN0')


@bot.callback_query_handler(func=lambda call: True)
# def language(call):
#     try:
#         if call.message:
#             if call.data == 'ru':
#                 bot.send_message(call.message.chat.id, 'Это информационный бот компании Hostmaster.Hostmaster – '
#                                                        'Хостинг провайдер и регистратор доменов в '
#                                                        'Узбекистане, в Ташкенте.Наш телефон: 71-202-55-11')
#                 bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                                       text=f'Выбран язык: <b>Русский</b>',
#                                       reply_markup=None, parse_mode='html')
#                 bot.register_next_step_handler(call.message, uslugi)
#
#
#             elif call.data == 'uz':
#                 bot.send_message(call.message.chat.id,
#                                  """Bu Hostmaster kompaniyasining axborot boti. Hostmaster - Xosting provayderi va domen registratori" O'zbekiston, Toshkentda. Bizning telefon: 71-202-55-11""")
#                 bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                                       text=f'Выбран язык: <b>Узбекский</b>',
#                                       reply_markup=None, parse_mode='html')
#
#             # remove inline buttons
#
#             # show alert
#             bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
#                                       text="NEW LINE SOLUTIONS")
#
#
#     except Exception as e:
#         print(repr(e))

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        if call.data == 'pay_services':
            bot.send_message(call.message.chat.id,
                             'Для получения информации об используемых услугах и платежах - вам необходимо пройти авторизацию')


@bot.message_handler(commands=['us'])
def language(message):
    if message.text == '🇷🇺Russian🇷🇺':
        markup = types.InlineKeyboardMarkup(row_width=1)
        lg1 = types.InlineKeyboardButton('Поддержка клиентов', callback_data='support')
        lg2 = types.InlineKeyboardButton('Веб-сайт компании', callback_data='web', url='https://www.hostmaster.uz/')
        lg3 = types.InlineKeyboardButton('Экспресс-оплата устлу', callback_data='payment',
                                         url='https://www.hostmaster.uz/site/login')
        lg4 = types.InlineKeyboardButton('Персональный кабинет на сайте', callback_data='cabinet',
                                         url='https://www.hostmaster.uz/site/login/')
        lg5 = types.InlineKeyboardButton('Канал новостей', callback_data='tg_channel',
                                         url='https://t.me/hostmasteruz')

        lg6 = types.InlineKeyboardButton('Услуги и платежи', callback_data='pay_services',
                                         )
        markup.add(lg1, lg2, lg3, lg4, lg5, lg6)
        bot.send_message(message.chat.id, 'Что вас интересует ?', reply_markup=markup)
        bot.register_message_handler(message.chat.id, 'Что вас интересует ?', reply_markup=markup)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    text = f'<b>{message.from_user.first_name}</b> пишет боту...'
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
    lg1 = types.KeyboardButton('🇷🇺Russian🇷🇺')
    lg2 = types.KeyboardButton('🇺🇿Uzbek🇺🇿')
    markup.add(lg1, lg2)
    bot.send_message(332749197, text, parse_mode='html')
    bot.reply_to(message, "Iltimos, tilni tanlang\n\nПожалуйста, выберите язык", reply_markup=markup)
    bot.register_next_step_handler(message, language)


bot.polling(none_stop=True)
