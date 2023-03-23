from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from src.tools import tr


class my_markup:
    def __init__(self, db):
        self.db = db
        self.main = self.__make_main_markup()
        self.lessons = self.__make_lessons_markup()
        self.activities = self.__make_activities_markup()

    def __make_main_markup(self):
        # главное меню
        main = InlineKeyboardMarkup()
        main.add(InlineKeyboardButton("Записаться на занятия", callback_data="Записаться на занятия"))
        main.add(InlineKeyboardButton("Афиша мероприятий и семинаров", callback_data="Афиша"))
        r3 = InlineKeyboardButton("Расписание", callback_data="but_3")
        r4 = InlineKeyboardButton("Прайс-лист", callback_data="but_4")
        r5 = InlineKeyboardButton("Контакты", callback_data="but_5")
        r6 = InlineKeyboardButton("Акции", callback_data="but_6")
        r7 = InlineKeyboardButton("Аренда залов", callback_data="but_7")
        r8 = InlineKeyboardButton("Лавка студии", callback_data="but_8")
        main.row(r3, r4, r5)
        main.row(r5, r7, r8)
        return main

    def __make_lessons_markup(self):
        # запись на занятия (выбор мастера)
        lessons = InlineKeyboardMarkup()
        raw_data = self.db.get_masters()
        data = dict()
        for v in raw_data:
            data[v[0]] = v[1:]
        for key in data.keys():
            lessons.add(InlineKeyboardButton(key + ' (' + ', '.join(data[key]) + ')', callback_data=tr(key)))
        lessons.add(InlineKeyboardButton("Назад", callback_data="Главное меню"))
        return lessons

    def __make_activities_markup(self):
        # Афиша
        activities = InlineKeyboardMarkup()
        r3 = InlineKeyboardButton("123")
        r4 = InlineKeyboardButton("123")
        r5 = InlineKeyboardButton("123")
        activities.row(r3, r4, r5)
        #activities.add(InlineKeyboardButton("Назад", callback_data="Главное меню"))
        return activities
