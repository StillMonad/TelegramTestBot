from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot import types, TeleBot
from src.tools import tr
import src.tools as tools
from src.objects.moderation import Moderation


@tools.show_call
class Chat:
    def __init__(self, bot: TeleBot, db):
        self.call_data = "Чат"
        self.commands = ["chat"]
        self.stop_conversation = ['завершить', 'конец', 'завершить диалог', 'Завершить диалог', 'Закончить диалог',
                                  'закончить диалог']
        self.text = "Вы начали диалог с администратором бота 🙌"

        self.markup_user = self.__make_markup_user_chat(db)
        self.markup_user_end = self.__make_markup_user_chat_end(db)
        self.markup_admin = self.__make_markup_admin_chat(db)
        self.__init_handlers_user(bot, db)
        self.__init_handlers_admin(bot, db)

    def __make_markup_user_chat(self, db):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Закончить диалог'))
        return markup

    def __make_markup_user_chat_end(self, db):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Перейти в меню'))
        return markup

    def __make_markup_admin_chat(self, db):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Закончить диалог'))
        return markup

    def __init_handlers_user(self, bot: TeleBot, db):
        @bot.message_handler(func=lambda msg: msg.text in self.stop_conversation)
        def init_chat_message(msg):
            bot.send_message(chat_id=msg.chat.id, text="У вас в данный момент нет открытых диалогов",
                             reply_markup=self.markup_user)

        @bot.callback_query_handler(func=lambda call: call.data == self.call_data)
        def init_chat_message(call: types.CallbackQuery):
            admin_id = db.get_line_by_data('Администраторы', 'Администратор')[0]
            admin_chat_id = db.get_line_by_data('Пользователи', admin_id)[1]
            bot.send_message(chat_id=admin_chat_id, text=f"{call.from_user.first_name} начал диалог",
                             disable_notification=False)
            sent_msg = bot.send_message(chat_id=call.message.chat.id, text=self.text,
                                        reply_markup=self.markup_user)
            bot.register_next_step_handler(sent_msg, next_message)

        def next_message(msg: types.Message):
            admin_id = db.get_line_by_data('Администраторы', 'Администратор')[0]
            admin_chat_id = db.get_line_by_data('Пользователи', admin_id)[1]
            if msg.text in self.stop_conversation:
                bot.send_message(chat_id=admin_chat_id, text=f"{msg.from_user.first_name} закончил диалог",
                                 disable_notification=False)
                bot.send_message(chat_id=msg.chat.id, text="Вот и поговорили. 😈", reply_markup=self.markup_user_end)
                return
            try:
                bot.forward_message(admin_chat_id, msg.chat.id, msg.message_id, disable_notification=False)
            except:
                bot.send_message(chat_id=msg.chat.id,
                                 text="По неизвестным мне причинам я не могу доставить это сообщение... \nПопробуйте еще раз позднее.")
            bot.register_next_step_handler(msg, next_message)

    def __init_handlers_admin(self, bot: TeleBot, db):
        @bot.message_handler(func=lambda msg: msg.reply_to_message is not None)
        def cb(msg: types.Message):
            if not Moderation.is_admin(db, msg.from_user.id):
                return
            try:
                ch_id = msg.reply_to_message.json['forward_from']['id']
                bot.send_message(chat_id=msg.reply_to_message.json['forward_from']['id'], text=msg.text,
                                 disable_notification=False)
            except KeyError:
                bot.send_message(chat_id=msg.chat.id, text="Отправка ответа не удалась.",
                                 disable_notification=False)
