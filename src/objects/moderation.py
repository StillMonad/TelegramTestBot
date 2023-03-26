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

    @staticmethod
    def is_registered(db, uid):
        users = Moderation.get_users(db)
        if id in users.keys():
            return True
        return False

    @staticmethod
    def get_user_data(db, uid):
        line = db.get_line_by_data('Пользователи', uid)
        return {"uid": line[0],
                "username": line[1],
                "first_name": line[2],
                "last_name": line[3],
                "email": line[4],
                "phone": line[5]
                }

    @staticmethod
    def get_all_users_data(db):
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
    def log_message(db, sheet_name, msg: types.Message):
        line_ind = db.get_line_index_by_data(sheet_name, msg.from_user.id)
        if line_ind is None:
            db.add_data(sheet_name, [msg.from_user.id, msg.message_id])
            db.add_data(sheet_name, [msg.from_user.username, msg.text])
        line = db.get_line_by_data(sheet_name, msg.from_user.id)
        sheet = db.db.worksheet(sheet_name)
        sheet.update_cell(line_ind, len(line) + 1, msg.message_id)
        sheet.update_cell(line_ind + 1, len(line) + 1, msg.text)