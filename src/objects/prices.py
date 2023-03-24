from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot import types, TeleBot
from src.tools import tr
import src.tools as tools


@tools.show_call
class Prices:
    def __init__(self, bot: TeleBot, db):
        self.call_data = "Прайс-лист"
        self.commands = ["прайс", "price"]
        self.text = \
            """
            ПРАЙС-ЛИСТ
            
            Групповые занятия:
            🔸Разовое посещение - 1100 ₽
            
            Абонементы:
            🔸5 занятий - 4 900 ₽ 
            🔸10 занятий - 9 500 ₽
            
            Индивидуальные занятия
            Цигун, Тайцзи:
            🔸60 мин - 4 500 ₽
            🔸90 мин - 6 000 ₽
            🔸120 мин - 8 000 ₽
            
            Массаж:
            🔸90 мин - 6 000 ₽
            🔸120 мин - 8 000 ₽
            
            Китайский язык:
            🔸45 мин - 2 500 ₽
            🔸10 занятий (45 мин) - 22 500 ₽
            
            Абонементы на индивидуальные занятия и массаж:
            🔸10 занятий (60 мин) - 40 000 ₽
            🔸10 занятий (90 мин) - 54 000 ₽
            🔸10 занятий (120 мин) - 72 000 ₽
            """

        self.markup = self.__make_markup(db)
        self.__init_handlers(bot)

    def __make_markup(self, db):
        markup = InlineKeyboardMarkup()
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
