from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot import types, TeleBot
import src.tools as tools


@tools.show_call
class MainMenu:
    def __init__(self, bot: TeleBot):
        self.call_data = "Главное меню"
        self.commands = ["menu", "start"]
        self.text = "Я супер-пупер крутой тестовый бот без половины функций! 😭\nЧем я могу помочь?"
        self.markup = self.__make_markup()
        self.__init_handlers(bot)

    def __make_markup(self):
        # главное меню
        main = InlineKeyboardMarkup()
        main.add(InlineKeyboardButton("Записаться на занятия", callback_data="Записаться на занятия"))
        main.add(InlineKeyboardButton("Афиша мероприятий и семинаров", callback_data="Афиша мероприятий и семинаров"))
        r3 = InlineKeyboardButton("Расписание", callback_data="Расписание")
        r4 = InlineKeyboardButton("Прайс-лист", callback_data="Прайс-лист")
        r5 = InlineKeyboardButton("Контакты", callback_data="Контакты")
        r6 = InlineKeyboardButton("Акции", callback_data="Акции")
        r7 = InlineKeyboardButton("Аренда залов", callback_data="Аренда залов")
        r8 = InlineKeyboardButton("Лавка студии", callback_data="Лавка студии")
        main.row(r3, r4, r5)
        main.row(r6, r7, r8)
        return main

    def __init_handlers(self, bot: TeleBot):
        @bot.callback_query_handler(func=lambda call: call.data == self.call_data)
        def cb(call: types.CallbackQuery):
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=f"Привет, {call.message.chat.first_name}!\n" + self.text,
                                  reply_markup=self.markup, parse_mode="HTML")

        @bot.callback_query_handler(func=lambda call: call.data == self.call_data + "new")
        def cb(call: types.CallbackQuery):
            bot.send_message(chat_id=call.message.chat.id,
                             text=f"Привет, {call.message.chat.first_name}!\n" + self.text,
                             reply_markup=self.markup, parse_mode="HTML")

        @bot.message_handler(commands=self.commands)
        def message(msg: types.Message):
            bot.send_message(chat_id=msg.chat.id, text=f"Привет, {msg.chat.first_name}!\n" + self.text,
                             reply_markup=self.markup, parse_mode="HTML")

