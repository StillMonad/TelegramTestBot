import urllib

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot import types, TeleBot
from src.classes.slider import slider
from src.classes.data import data
import src.tools as tools
import os


@tools.show_call
class Activities:

    def __init__(self, bot: TeleBot, db):
        self.call_data = "Афиша мероприятий и семинаров"
        self.commands = ["мероприятия", "семинары", "афиша", "activities"]
        self.text = "Список мероприятий"

        self.markup = self.__make_markup(bot, db)
        self.__init_handlers(bot)

    def __make_markup(self, bot, db):
        self.slider = slider(bot, self.get_activities(db), parent="Главное меню")
        return self.slider.markup

    def __init_handlers(self, bot: TeleBot):

        @bot.callback_query_handler(func=lambda call: call.data == self.call_data)
        def cb(call: types.CallbackQuery):
            if self.slider.get_data().media is None:
                bot.edit_message_text(chat_id=call.message.chat.id,
                                      message_id=call.message.message_id,
                                      text=self.text,
                                      reply_markup=self.markup,
                                      parse_mode="HTML")
            else:
                self.slider.pos = 0
                bot.send_photo(photo=open(self.slider.get_data().media, "rb"),
                               chat_id=call.message.chat.id,
                               caption=self.slider.get_data().text,
                               reply_markup=self.markup,
                               parse_mode="HTML")

        @bot.message_handler(commands=self.commands)
        def message(msg: types.Message):
            self.slider.pos = 0
            bot.send_message(chat_id=msg.chat.id,
                             text=self.text,
                             reply_markup=self.markup,
                             parse_mode="HTML")

    def get_activities(self, db):
        raw_data = db.get_sheet_data("Мероприятия")
        acts = []
        for i, row in enumerate(raw_data):
            if len(row) == 1:
                acts += [data(row[0], media=None)]
                continue
            name = os.path.join("resources", "tmp", "act_img" + str(i) + '.jpg')
            img = None
            try:
                img = open(name, 'wb')
                img.write(urllib.request.urlopen(row[1]).read())
            except Exception:
                name = os.path.join("resources", row[1])
            finally:
                if not img is None:
                    img.close()
            acts += [data(row[0], media=name)]
        return acts
