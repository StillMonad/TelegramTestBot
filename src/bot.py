from telebot import TeleBot, types

from config import BOT_TOKEN, GS_LINK
from gsconnect import gsdb
from markups import my_markup
from tools import tr

bot = TeleBot(BOT_TOKEN)
db = gsdb(GS_LINK)
markup = my_markup(db)


@bot.message_handler(commands=['uid'])
def get_uid(msg: types.Message):
    """
    получение user_id через /uid
    """
    bot.send_message(chat_id=msg.chat.id, text=f"UID: {msg.from_user.id}")


@bot.message_handler(commands=['promote'])
def promote(msg: types.Message):
    """
    Добавление нового администратора через /promote user_id

    user_id можно получить через /uid
    """
    try:
        uid = int(msg.text.split(' ')[1])
    except IndexError:
        return

    if not db.is_admin(msg.from_user):
        bot.send_message(chat_id=msg.chat.id,
                         text=f"У вас не достаточно привелегий.\nПопросите помощи у администратора.")
        return
    if db.add_admin(uid):
        bot.send_message(chat_id=msg.chat.id, text=f"Добавление успешно")
    else:
        bot.send_message(chat_id=msg.chat.id, text=f"Ошибка добавления:\nПользователь уже существует.")


@bot.message_handler(commands=['start', 'menu', 'меню', 'начало', 'старт'])
def start(msg: types.Message):
    bot.send_message(chat_id=msg.chat.id, text=f"Привет {msg.chat.username}, чем я могу помочь?",
                     reply_markup=markup.main)


@bot.callback_query_handler(func=lambda call: call.data == tr("Назад1"))
def but_menu_pressed(call: types.CallbackQuery):
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text=f"Привет {call.message.chat.username}, чем я могу помочь?",
                          reply_markup=markup.main)


@bot.callback_query_handler(func=lambda call: call.data == tr("Записаться на занятия"))
def but1_pressed(call: types.CallbackQuery):
    global data

    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text='К кому вы хотите записаться?', reply_markup=markup.lessons)


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
