import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from src.classes.base import base
from src.classes.data import data


class slider(base):
    def __init__(self, bot, data_arr: data, parent=None):
        self.bot = bot
        super().__init__(parent=parent, type='slider')
        self.len = len
        self.pos = 0
        self.data = data_arr
        self.markup = self.markup_slider()
        self.init_callbacks()

    def get_data(self):
        return self.data[self.pos]

    def markup_slider(self):
        slider_markup = InlineKeyboardMarkup() if (self.data[self.pos].markup is None) else self.data[self.pos].markup
        r1 = InlineKeyboardButton("←", callback_data=self.name + "_but_left")
        r2 = InlineKeyboardButton(str(self.pos + 1) + " / " + str(len(self.data)), callback_data=self.name + "_pass")
        r3 = InlineKeyboardButton("→", callback_data=self.name + "_but_right")
        slider_markup.row(r1, r2, r3)
        if not (self.parent is None):
            slider_markup.add(InlineKeyboardButton("Назад к меню", callback_data=self.parent))
        return slider_markup

    def init_callbacks(self):
        bot: telebot.TeleBot = self.bot

        @bot.callback_query_handler(func=lambda call: call.data == self.name + "_but_left")
        def but_left(call: types.CallbackQuery):
            if self.pos <= 0:
                return
            self.pos -= 1
            self.__show(call)

        @bot.callback_query_handler(func=lambda call: call.data == self.name + "_but_right")
        def but_right(call: types.CallbackQuery):
            if self.pos >= len(self.data) - 1:
                return
            self.pos += 1
            self.__show(call)

    def __show(self, call: types.CallbackQuery):
        bot: telebot.TeleBot = self.bot
        markup = self.markup_slider()
        if self.data[self.pos].media is None:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=self.data[self.pos].text, reply_markup=markup, parse_mode="HTML")
        else:
            name = self.data[self.pos].media
            with open(name, "rb") as file:
                bot.edit_message_media(media=types.InputMediaPhoto(file), chat_id=call.message.chat.id,
                                       message_id=call.message.message_id, reply_markup=markup)
                bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.id,
                                         caption=self.data[self.pos].text, reply_markup=markup, parse_mode="HTML")
