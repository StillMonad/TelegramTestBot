from telebot import TeleBot, types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_TOKEN, GS_LINK
from transliterate import translit
from gsconnect import gsdb

bot = TeleBot(BOT_TOKEN)
db = gsdb(GS_LINK)

data = {
    'Алина Харламова':
        ('Тайцзи', 'Цигун'),
    'Вадим Черноусов':
        ('Тайцзи', 'Цигун'),
    'Роман Ляшенко':
        ('Массаж',),
    'Ксения Ицкович':
        ('Китайский язык',)
}


def tr(s):
    return translit(s, reversed=True)


@bot.message_handler(commands=['start', 'menu', 'меню', 'начало', 'старт'])
def start(msg: types.Message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Записаться на занятия", callback_data=tr("Записаться на занятия")))
    markup.add(InlineKeyboardButton("Афиша мероприятий и семинаров", callback_data="but_2"))
    markup.add(InlineKeyboardButton("Расписание", callback_data="but_3"))
    markup.add(InlineKeyboardButton("Прайс-лист", callback_data="but_4"))
    markup.add(InlineKeyboardButton("Контакты", callback_data="but_5"))
    markup.add(InlineKeyboardButton("Акции", callback_data="but_6"))
    markup.add(InlineKeyboardButton("Аренда залов", callback_data="but_7"))
    markup.add(InlineKeyboardButton("Лавка студии", callback_data="but_8"))
    bot.send_message(chat_id=msg.chat.id, text=f"Привет {msg.chat.first_name}, чем я могу вам помочь?",
                     reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == tr("Назад1"))
def but_menu_pressed(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Записаться на занятия", callback_data=tr("Записаться на занятия")))
    markup.add(InlineKeyboardButton("Афиша мероприятий и семинаров", callback_data="but_2"))
    markup.add(InlineKeyboardButton("Расписание", callback_data="but_3"))
    markup.add(InlineKeyboardButton("Прайс-лист", callback_data="but_4"))
    markup.add(InlineKeyboardButton("Контакты", callback_data="but_5"))
    markup.add(InlineKeyboardButton("Акции", callback_data="but_6"))
    markup.add(InlineKeyboardButton("Аренда залов", callback_data="but_7"))
    markup.add(InlineKeyboardButton("Лавка студии", callback_data="but_8"))
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text=f"Привет {call.message.chat.first_name}, чем я могу вам помочь?",
                          reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == tr("Записаться на занятия"))
def but1_pressed(call: types.CallbackQuery):
    global data
    markup = InlineKeyboardMarkup()

    [markup.add(InlineKeyboardButton(key + ' (' + ', '.join(data[key]) + ')' \
                                     , callback_data=tr(key))) for key in data.keys()]

    markup.add(InlineKeyboardButton("Назад", callback_data=tr("Назад1")))

    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text='К кому вы хотите записаться?', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "but_2")
def but2_pressed(call: types.CallbackQuery):
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text='Some text2, for example')


@bot.callback_query_handler(func=lambda call: call.data == "but_3")
def but3_pressed(call: types.CallbackQuery):
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text='Some text3, for example')


@bot.callback_query_handler(func=lambda call: call.data == "but_4")
def but4_pressed(call: types.CallbackQuery):
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text='Some text4, for example')


@bot.callback_query_handler(func=lambda call: call.data == "but_5")
def but5_pressed(call: types.CallbackQuery):
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text='Some text5, for example')


@bot.callback_query_handler(func=lambda call: call.data == "but_6")
def but6_pressed(call: types.CallbackQuery):
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text='Some text6, for example')


@bot.callback_query_handler(func=lambda call: call.data == "but_7")
def but7_pressed(call: types.CallbackQuery):
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text='Some text7, for example')


@bot.callback_query_handler(func=lambda call: call.data == "but_8")
def but8_pressed(call: types.CallbackQuery):
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text='Some text8, for example')


if __name__ == '__main__':
    bot.infinity_polling(skip_pending=True)
