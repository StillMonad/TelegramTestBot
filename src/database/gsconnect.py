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

    @staticmethod
    def get_coord(x, y):
        return chr(x + 64) + str(y)

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

    def get_sheet_data(self, name):
        sheet = self.db.worksheet(name)
        return sheet.get_values()

    def add_data(self, name, data):
        sheet = self.db.worksheet(name)
        sheet.append_row(data)