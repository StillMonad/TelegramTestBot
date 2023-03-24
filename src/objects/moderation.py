import urllib
from telebot import types
import src.tools as tools


@tools.show_call
class Moderation:
    def __init__(self, bot, db):
        @bot.message_handler(commands=['uid'])
        def get_uid(msg: types.Message):
            """
            получение user_id через /uid
            """
            bot.send_message(chat_id=msg.chat.id, text=f"UID: {msg.from_user.id}")

        @bot.message_handler(commands=['promote'])
        def promote(msg: types.Message):
            """
            Добавление нового администратора через /promote user_id

            user_id можно получить через /uid или базу данных
            """
            if not Moderation.is_admin(db, msg.from_user.id):
                bot.send_message(chat_id=msg.chat.id,
                                 text=f"У вас не достаточно привелегий.\nПопросите помощи у администратора.")
                return

            try:
                uid = int(msg.text.split(' ')[1])
            except IndexError:
                bot.send_message(chat_id=msg.chat.id, text=f"Команда должна быть вида /promote uid")
                return

            if Moderation.add_admin(db, uid):
                bot.send_message(chat_id=msg.chat.id, text=f"Добавление успешно")
            else:
                bot.send_message(chat_id=msg.chat.id, text=f"Ошибка добавления:\nПользователь уже существует.")

        @bot.message_handler(commands=['demote'])
        def demote(msg: types.Message):
            """
            Удаление администратора через /demote user_id

            user_id можно получить через /uid или базу данных
            """
            if not Moderation.is_admin(db, msg.from_user.id):
                bot.send_message(chat_id=msg.chat.id,
                                 text=f"У вас не достаточно привелегий.\nПопросите помощи у администратора.")
                return

            try:
                uid = int(msg.text.split(' ')[1])
            except IndexError:
                bot.send_message(chat_id=msg.chat.id, text=f"Команда должна быть вида /demote uid")
                return

            if Moderation.del_admin(db, uid):
                bot.send_message(chat_id=msg.chat.id, text=f"Удаление успешно")
            else:
                bot.send_message(chat_id=msg.chat.id, text=f"Администраторов с таким UID не найдено.")

    @staticmethod
    def get_users(db):
        users_table = db.get_sheet_data("Пользователи")
        users = dict()
        for user in users_table[1:]:
            users[user[0]] = {"username": user[1],
                              "first_name": user[2],
                              "last_name": user[3],
                              "email": user[4],
                              "phone": user[5]
                              }
        return users

    @staticmethod
    def get_admins(db):
        adm_table = db.get_sheet_data("Администраторы")
        admins = [i[0] for i in adm_table if i[0] != '']
        return admins

    @staticmethod
    def is_admin(db, uid):
        admins = Moderation.get_admins(db)
        if str(uid) in admins:
            return True
        return False
    @staticmethod
    def add_admin(db, uid):
        admins = Moderation.get_admins(db)
        print(admins)
        if str(uid) in admins:
            return False
        db.add_data("Администраторы", [uid])
        return True

    @staticmethod
    def del_admin(db, uid):
        sheet = db.db.worksheet('Администраторы')
        cell = sheet.find(str(uid))
        if cell is None:
            return False
        sheet.update_cell(cell.row, cell.col, '')
        return True
