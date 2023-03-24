from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot import types, TeleBot
from src.tools import tr
import src.tools as tools


@tools.show_call
class Lessons:
    def __init__(self, bot: TeleBot, db):
        self.call_data = "Записаться на занятия"
        self.commands = ["записаться", "lessons"]
        self.text = "К кому вы хотите записаться?"

        self.markup = self.__make_markup(db)
        self.__init_handlers(bot)

    def __make_markup(self, db):
        # запись на занятия (выбор мастера)
        lessons = InlineKeyboardMarkup()
        raw_data = self.get_masters(db)
        data = dict()
        for v in raw_data:
            data[v[0]] = v[1:]
        for key in data.keys():
            lessons.add(InlineKeyboardButton(key + ' (' + ', '.join(data[key]) + ')', callback_data=tr(key)))
        lessons.add(InlineKeyboardButton("Назад", callback_data="Главное меню"))
        return lessons

    def __init_handlers(self, bot: TeleBot):
        @bot.callback_query_handler(func=lambda call: call.data == self.call_data)
        def cb(call: types.CallbackQuery):
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=self.text,
                                  reply_markup=self.markup, parse_mode="HTML")

        @bot.message_handler(commands=self.commands)
        def message(msg: types.Message):
            bot.send_message(chat_id=msg.chat.id, text=self.text,
                             reply_markup=self.markup, parse_mode="HTML")

    def get_masters(self, db):
        sheet = db.worksheet_workers
        i = 1
        row = sheet.row_values(i)
        masters = []
        while row:
            masters += [row]
            i += 1
            row = sheet.row_values(i)
        return masters
