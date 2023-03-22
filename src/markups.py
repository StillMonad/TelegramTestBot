from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from tools import tr

datata = {
    'Алина Харламова':
        ('Тайцзи', 'Цигун'),
    'Вадим Черноусов':
        ('Тайцзи', 'Цигун'),
    'Роман Ляшенко':
        ('Массаж',),
    'Ксения Ицкович':
        ('Китайский язык',)
}


class my_markup:
    def __init__(self, db):
        # главное меню
        main = InlineKeyboardMarkup()
        main.add(InlineKeyboardButton("Записаться на занятия", callback_data=tr("Записаться на занятия")))
        main.add(InlineKeyboardButton("Афиша мероприятий и семинаров", callback_data="but_2"))
        r3 = InlineKeyboardButton("Расписание", callback_data="but_3")
        r4 = InlineKeyboardButton("Прайс-лист", callback_data="but_4")
        r5 = InlineKeyboardButton("Контакты", callback_data="but_5")
        r6 = InlineKeyboardButton("Акции", callback_data="but_6")
        r7 = InlineKeyboardButton("Аренда залов", callback_data="but_7")
        r8 = InlineKeyboardButton("Лавка студии", callback_data="but_8")
        main.row(r3, r4, r5)
        main.row(r5, r7, r8)
        self.main = main

        # запись на занятия (выбор мастера)
        lessons = InlineKeyboardMarkup()
        raw_data = db.get_masters()
        data = dict()
        for v in raw_data:
            data[v[0]] = v[1:]
        for key in data.keys():
            lessons.add(InlineKeyboardButton(key + ' (' + ', '.join(data[key]) + ')', callback_data=tr(key)))
        lessons.add(InlineKeyboardButton("Назад", callback_data=tr("Назад1")))
        self.lessons = lessons

        # Афиша
        activities = InlineKeyboardMarkup()
        activities.add(InlineKeyboardButton("Назад", callback_data=tr("Назад1")))
        self.activities = activities
