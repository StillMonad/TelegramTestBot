from telebot import types, TeleBot
from src.classes.slider import slider
from src.classes.data import data
class reg_inline_handler:
    def __init__(self, bot: TeleBot, db, markup):
        @bot.callback_query_handler(func=lambda call: call.data == "Главное меню")
        def but_menu_pressed(call: types.CallbackQuery):
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=f"Привет {call.message.chat.username}, чем я могу помочь?",
                                  reply_markup=markup.main)


        @bot.callback_query_handler(func=lambda call: call.data == "Записаться на занятия")
        def but1_pressed(call: types.CallbackQuery):
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='К кому вы хотите записаться?', reply_markup=markup.lessons)


        @bot.callback_query_handler(func=lambda call: call.data == "Афиша")
        def but2_pressed(call: types.CallbackQuery):
            arr = db.activities
            my_slider = slider(bot, data_arr=arr)
            if arr[0].media is None:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=arr[0].text, reply_markup=my_slider.markup)
            else:
                with open(arr[0].media, "rb") as file:
                    bot.send_photo(call.message.chat.id, file, caption=arr[0].text, reply_markup=my_slider.markup)


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
