from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot import types, TeleBot
from src.tools import tr
import src.tools as tools


@tools.show_call
class Contacts:
    def __init__(self, bot: TeleBot, db):
        self.call_data = "Контакты"
        self.commands = ["контакты", "contacts", "о нас"]
        self.text = \
            """<b>Мы - Студия Цигун "Ма Дар Гита"</b>
            
<b>Наши контакты:</b>
сайт: http://madargita.ru/
whatsapp: https://wa.me/message/FSMR5CGPMHVIH1
telegram: https://t.me/madargita
vk: https://vk.com/madargita
instagram: https://instagram.com/madargita
youtube: https://youtube.com/@Madargita

<b>Как пройти:</b>
Студия «Ма Дар Гита» метро Новослободская/Менделеевская/Достоевская (1-й Щемиловский переулок 16с2), 4-й подъезд. 

Код от двери внизу 9813, потом направо на 3-й этаж, код от двери 7539, третья дверь справа. 

У входа есть бесплатная стихийная парковка. Вход/въезд в переулок только с ул. Селезневская, будьте внимательны 🙏🏻✨

<b>Карта:</b>
https://maps.google.com/maps/place/55.77892010751724+37.6071349569397/@55.77892010751724,37.6071349569397
"""

        self.markup = self.__make_markup(db)
        self.__init_handlers(bot)

    def __make_markup(self, db):
        markup = InlineKeyboardMarkup()
        markup.add(
        InlineKeyboardButton("Начать диалог с администратором", callback_data="Чат"))
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
