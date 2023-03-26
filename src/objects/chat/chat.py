from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot import types, TeleBot
from src.tools import tr
import src.tools as tools


@tools.show_call
class Chat:
    def __init__(self, bot: TeleBot, db):
        self.call_data = "Чат"
        self.commands = ["chat"]
        self.text = "Вы начали диалог с администратором бота 🙌"

        self.markup_user = self.__make_markup_user_chat(db)
        self.markup_admin = self.__make_markup_admin_chat(db)
        self.__init_handlers_user(bot)
        self.__init_handlers_admin(bot)

    def __make_markup_user_chat(self, db):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton("Завершить диалог"))
        return markup

    def __make_markup_admin_chat(self, db):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton("Завершить диалог"))
        return markup


    def __init_handlers_user(self, bot: TeleBot):
        @bot.callback_query_handler(func=lambda call: call.data == self.call_data)
        def init_chat_message(call: types.CallbackQuery):
            sent_msg = bot.send_message(chat_id=call.message.chat.id, text='Введите пожалуйста свое имя:',
                                        reply_markup=self.markup, parse_mode="HTML")
            bot.register_next_step_handler(sent_msg, next_message)

        def next_message(msg):
            sent_msg = bot.send_message(chat_id=msg.chat.id, text=f"Введите пожалуйста свою фамилию:",
                                        reply_markup=self.markup, parse_mode="HTML")
            bot.register_next_step_handler(sent_msg, next_message(), [msg.text])


    def __init_handlers_admin(self, bot: TeleBot):
        @bot.callback_query_handler(func=lambda call: call.data == self.call_data)
        def cb(call: types.CallbackQuery):
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=self.text,
                                  reply_markup=self.markup_user, parse_mode="HTML")