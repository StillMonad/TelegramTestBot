from telebot import types
from src.tools import tr

class reg_inline_handler:
    def __init__(self, bot, db, markup):
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
