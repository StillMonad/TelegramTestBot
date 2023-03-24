from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot import types, TeleBot
from src.tools import tr
import src.tools as tools


@tools.show_call
class Rent:
    def __init__(self, bot: TeleBot, db):
        self.call_data = "Аренда залов"
        self.commands = ["аренда", "rent"]
        self.text = \
            """<b>Мы - Студия Цигун "Ма Дар Гита"</b>
            
5 минут от м.Новослободская/Достоевская

<b>Доступны два зала для аренды:</b>
- Большой (50 кв м) 
- Маленький (10 кв м). 

Студия в самом центре Москвы, тихая(!), уютная, с высокими потолками (3 м), серые стены идеальны для съемок, есть бесплатная стихийная парковка у входа. 
Студия оборудована всем необходимым для практик, семинаров, конференций, мастер-классов:

- коврики (16 шт)
- подушки, одеяла
- мат для массажа 2х2 метра
- тайцзи бан для цигун
- ролики для МФР (6 шт)
- стулья (20 шт)
- белая стена для проектора
- проектор (+1000 ₽)
- флипчарт
- планшеты для бумаги А4
- bluetooth колонка
- штатив для телефона
- вода, чай
- с/у на этаже

Большой зал, 50 кв м. 
Цены на аренду: 
- будни до 18:00 - 800 р/60 мин, 
- будни после 18:00 и выходные - 1300 р/60 мин.

Маленький зал, 10 кв м. 
Цена на аренду: 
- 500 р/60 мин

⚡При аренде большого зала длительностью от 4 часов - малый зал в подарок, то есть вся студия ваша ) ⚡

<b>Правила брони и оплаты:</b>
- Для брони предоплата 50% 
- Вторая часть может быть оплачена день в день

<b>Правила отмены:</b>
- при аренде более 4 часов: полный возврат средств за 2 недели до аренды, позднее - 30 % остаётся студии
- при аренде менее 4 часов: полный возврат средств за 2 дня до аренды, позднее - 30 % остаётся студии
"""

        self.markup = self.__make_markup(db)
        self.__init_handlers(bot)

    def __make_markup(self, db):
        markup = InlineKeyboardMarkup()
        markup.add(
            InlineKeyboardButton("Начать диалог с администратором", callback_data="Начать диалог с администратором"))
        markup.add(InlineKeyboardButton("Контакты", callback_data="Контакты"))
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
