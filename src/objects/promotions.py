from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot import types, TeleBot
from src.tools import tr
import src.tools as tools


@tools.show_call
class Promotions:
    def __init__(self, bot: TeleBot, db):
        self.call_data = "Акции"
        self.commands = ["акции", "promotions"]
        self.text = \
            """⚡ Скидка 10% на абонементы при покупке 
- в день первого визита
- в день рождения 
- студентам и пенсионерам"""

        self.markup = self.__make_markup(db)
        self.__init_handlers(bot)

    def __make_markup(self, db):
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("Начать диалог с администратором", callback_data="Чат"))
        markup.add(InlineKeyboardButton("В главное меню", callback_data="Главное меню"))
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
