import urllib
import gspread
from telebot import types
from src.classes.data import data

class gsdb:
    def __init__(self, link):
        gs = gspread.service_account()
        self.db = gs.open_by_url(link)

        self.worksheet_admins = self.db.worksheet('Администраторы')
        self.worksheet_users = self.db.worksheet('Пользователи')
        self.worksheet_booking = self.db.worksheet('Оформление заказа')
        self.worksheet_workers = self.db.worksheet('Мастера')
        self.worksheet_activities = self.db.worksheet('Мероприятия')
        self.worksheet_goods = self.db.worksheet('Товары')
        self.update_admins()

    @staticmethod
    def get_coord(x, y):
        return chr(x + 64) + str(y)

    def set(self, sheet, coord: str, val):
        if type(sheet) == int:
            sheet = self.db.get_worksheet(sheet)
            sheet.update(coord, val)
        else:
            sheet = self.db.worksheet(sheet)
            sheet.update(coord, val)

    def get(self, sheet, coord):
        """
        Getting value from coords, coords starts from 1
        """
        s = None
        if type(sheet) == type(1):
            s = self.db.get_worksheet(sheet)
        else:
            s = self.db.worksheet(sheet)

        if type(coord) == type("str"):
            return s.get(coord).first()
        else:
            return s.cell(*coord).value

    def update_admins(self):
        sheet = self.worksheet_admins
        self.admins = sheet.col_values(1)[1:]
        self.admins = [int(a) for a in self.admins]

    def get_admins(self):
        return self.admins

    def add_admin(self, uid):
        self.update_admins()
        self.admins = self.get_admins()
        sheet = self.worksheet_admins
        pos = (len(self.admins) + 2)
        if uid in self.admins:
            return False
        sheet.update(self.get_coord(1, pos), [[uid]])
        self.update_admins()
        return True

    def is_admin(self, user: types.User):
        if user.id in self.admins:
            return True
        return False

