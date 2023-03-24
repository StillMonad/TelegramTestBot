import urllib

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot import types, TeleBot
from src.tools import tr
import src.tools as tools

@tools.show_call
class Commands:
    def __init__(self, bot, db):
        @bot.message_handler(commands=['download'])
        def message(msg: types.Message):
            text = msg.text.split(' ')
            if (len(text) != 3):
                bot.send_message(chat_id=msg.chat.id, text="Используйте /download file_name url")
                return
            try:
                name = "tmp\\" + text[1] + ".jpg"
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


        @bot.message_handler(func=lambda message: message.text[0] == '/')
        def message(msg):
            bot.send_message(chat_id=msg.chat.id, text=f"Я не знаю такой команды. 👿")
