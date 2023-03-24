from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot import types, TeleBot
from src.tools import tr
import src.tools as tools


@tools.show_call
class Schedule:
    def __init__(self, bot: TeleBot, db):
        self.call_data = "Расписание"
        self.commands = ["расписание", "schedule"]
        self.text = \
            """Групповые занятия в студии:
            
            Пн
            🔸19:30 Основы Тайцзи
            (Алина Харламова)
            
            Ср
            🔸11:00 Цигун 
            (Алина Харламова)
            🔸19:00 Цигун-терапия
            (Алина Харламова)
            🔸20:30 Творческий вечер (раз в две недели, смотрите афишу мероприятий)
            
            Чт
            🔸19:00 Туйшоу клуб 
            (Николай Николаев)
            
            И индивидуальные классы в удобное вам время:
            
            Алина Харламова (Цигун, Тайцзи)
            Роман Ляшенко (Массаж)
            Ксения Ицкович (Китайский язык)
            
            
            Для записи на мероприятия и семинары студии перейдите в раздел Афиши)
            """

        self.markup = self.__make_markup(db)
        self.__init_handlers(bot)

    def __make_markup(self, db):
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("Записаться на занятия", callback_data="Записаться на занятия"))
        markup.add(InlineKeyboardButton("Прайс-лист", callback_data="Прайс-лист"))
        markup.add(InlineKeyboardButton("Афиша мероприятий и семинаров", callback_data="Афиша мероприятий и семинаров"))
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
