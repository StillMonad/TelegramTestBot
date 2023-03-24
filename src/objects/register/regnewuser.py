from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot import types, TeleBot
from src.objects.moderation import Moderation

import src.tools as tools


@tools.show_call
class RegisterStep2:
    def __init__(self, bot: TeleBot, db):
        self.call_data = "Заполнение данных"
        self.commands = []
        self.text = \
            """
            Введите пожалуйста свое имя:
            """
        self.curr_reg = 0
        self.user_data = []
        self.markup = self.__make_markup(db)
        self.__init_handlers(bot, db)

    def __make_markup(self, db):
        markup = InlineKeyboardMarkup()
        r1 = InlineKeyboardButton("Отмена регистрации", callback_data="Главное меню")
        markup.row(r1)
        return markup

    def __init_handlers(self, bot: TeleBot, db):
        @bot.callback_query_handler(func=lambda call: call.data == self.call_data)
        def ask_first_name(call: types.CallbackQuery):
            sent_msg = bot.send_message(chat_id=call.message.chat.id, text='Введите пожалуйста свое имя:',
                                        reply_markup=self.markup, parse_mode="HTML")
            bot.register_next_step_handler(sent_msg, ask_last_name)

        def ask_last_name(prev_msg):
            sent_msg = bot.send_message(chat_id=prev_msg.chat.id, text=f"Введите пожалуйста свою фамилию:",
                                        reply_markup=self.markup, parse_mode="HTML")
            bot.register_next_step_handler(sent_msg, ask_phone, [prev_msg.text])

        def ask_phone(prev_msg, data):
            sent_msg = bot.send_message(chat_id=prev_msg.chat.id, text=f"Введите пожалуйста свой телефон для связи:",
                                        reply_markup=self.markup, parse_mode="HTML")
            bot.register_next_step_handler(sent_msg, ask_email, data + [prev_msg.text])

        def ask_email(prev_msg, data):
            sent_msg = bot.send_message(chat_id=prev_msg.chat.id, text=f"Введите пожалуйста свою почту:",
                                        reply_markup=self.markup, parse_mode="HTML")
            bot.register_next_step_handler(sent_msg, finalize, data + [prev_msg.text])

        def finalize(prev_msg, data):
            data = data + [prev_msg.text]
            data_str = "\n".join(data)
            self.user_data.append(data)
            self.curr_reg += 1
            markup = InlineKeyboardMarkup()
            r1 = InlineKeyboardButton("Отмена регистрации", callback_data="Главное меню")
            r2 = InlineKeyboardButton("Подтвердить", callback_data="Подтверждение правильности данных")
            markup.row(r1, r2)

            bot.send_message(chat_id=prev_msg.chat.id, text=f"Подтвердите введенные данные:\n" + data_str,
                             reply_markup=markup, parse_mode="HTML")

        @bot.callback_query_handler(func=lambda call: call.data == "Подтверждение правильности данных")
        def register_to_db(call: types.CallbackQuery):
            db.add_data("Пользователи", [call.from_user.id, call.from_user.username] + self.user_data[self.curr_reg - 1])
            self.user_data.pop(-1)
            self.curr_reg -= 1
            db.users = Moderation.get_users(db)

            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton("Главное меню", callback_data="Главное меню"))

            bot.send_message(chat_id=call.message.chat.id, text='Вы были успешно зарегистрированы! 🥳',
                             reply_markup=markup, parse_mode="HTML")
