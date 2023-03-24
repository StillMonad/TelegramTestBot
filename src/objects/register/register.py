from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot import types, TeleBot
from src.objects.register.regnewuser import RegisterStep2

import src.tools as tools


@tools.show_call
class Register:
    def __init__(self, bot: TeleBot, db):
        self.call_data = "Зарегистрироваться"
        self.commands = []
        self.text = \
            """
            Извините. Похоже, мы с вами не знакомы. 😅🔫\n
            Ответьте пожалуйста на пару вопросов, прежде чем продолжить.
            """

        self.markup = self.__make_markup(db)
        self.__init_handlers(bot)
        self.step_2 = RegisterStep2(bot, db)

    def __make_markup(self, db):
        markup = InlineKeyboardMarkup()
        r1 = InlineKeyboardButton("В главное меню", callback_data="Главное меню")
        r2 = InlineKeyboardButton("Продолжить", callback_data="Заполнение данных")
        markup.row(r1, r2)
        return markup

    def __init_handlers(self, bot: TeleBot):
        @bot.callback_query_handler(func=lambda call: call.data == self.call_data)
        def cb(call: types.CallbackQuery):
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=self.text,
                                  reply_markup=self.markup, parse_mode="HTML")

        @bot.message_handler(commands=self.commands)
        def message(msg: types.Message):
            bot.send_message(chat_id=msg.chat.id, text=self.text,
                             reply_markup=self.markup, parse_mode="HTML")
