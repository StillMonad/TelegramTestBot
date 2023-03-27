import urllib
import src.tools as tools

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot import types, TeleBot
from src.objects.moderation import Moderation
import os


@tools.show_call
class Commands:
    def __init__(self, bot, db):
        @bot.message_handler(commands=['download'])
        def download(msg: types.Message):
            if not Moderation.is_admin(db, msg.from_user.id):
                bot.send_message(chat_id=msg.chat.id, text=f"У вас не достаточно привелегий.\n")
                return
            text = msg.text.split(' ')
            if (len(text) != 3):
                bot.send_message(chat_id=msg.chat.id, text="Используйте /download file_name url")
                return
            try:
                name = os.path.join('resources', text[1])
                img = open(name, 'wb')
                print(f"Trying to download {name} from {text[2]}")
                file = urllib.request.urlopen(text[2]).read()
                print("Done")
                img.write(file)
                bot.send_message(chat_id=msg.chat.id, text="Скачивание успешно")
            except Exception as e:
                bot.send_message(chat_id=msg.chat.id, text="Ошибка скачивания")
            finally:
                img.close()

        @bot.message_handler(commands=['help'])
        def help(msg: types.Message):
            text = """
/menu - главное меню
/uid - uid пользователя
/contacts - контакты
/prices - прайс-лист

<b>Административные:</b>
/reboot - перезагрузка
/promote uid - добавление администратора в бд
/demote uid - удаление администратора из бд
/download fname url - скачивание файла в папку resources для использования в бд
            """
            bot.send_message(chat_id=msg.chat.id, text=text, parse_mode="HTML")

        # этот обработчик должен стоять в самом конце, так как он наиболее общий
        @bot.message_handler(func=lambda message: message.text[0] == '/')
        def unknown_command(msg: types.Message):
            #if msg.reply_to_message:
            #    bot.send_message(chat_id=msg.chat.id, text=f"👿")
            bot.send_message(chat_id=msg.chat.id, text=f"Я не знаю такой команды. 👿")


