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

            user_id можно получить через /uid
            """
            try:
                uid = int(msg.text.split(' ')[1])
            except IndexError:
                return

            if not db.is_admin(msg.from_user):
                bot.send_message(chat_id=msg.chat.id,
                                 text=f"У вас не достаточно привелегий.\nПопросите помощи у администратора.")
                return
            if db.add_admin(uid):
                bot.send_message(chat_id=msg.chat.id, text=f"Добавление успешно")
            else:
                bot.send_message(chat_id=msg.chat.id, text=f"Ошибка добавления:\nПользователь уже существует.")

    @staticmethod
    def get_users(db):
        pass
