from telebot import TeleBot, types
from config import BOT_TOKEN, GS_LINK
from database.gsconnect import gsdb
from markups import MyMarkup
from src.objects.moderation import Moderation
from src.objects.main_menu import MainMenu
from src.objects.lessons import Lessons
from src.objects.activities import Activities
from src.objects.schedule import Schedule
from src.objects.prices import Prices
from src.objects.contacts import Contacts
from src.objects.promotions import Promotions
from src.objects.rent import Rent
from src.objects.shop import Shop
from src.commands import Commands
from src.objects.register.register import Register

bot = None
db = None
markup = None
users = None
moderation = None
menu = None
lessons = None
activities = None
schedule = None
prices = None
contacts = None
promotions = None
rent = None
shop = None
commands = None
register = None


class InitGlobals:
    def __init__(self):
        global bot, db, markup, users, moderation, menu, lessons, activities, \
            schedule, prices, promotions, contacts, rent, shop, commands, register
        # ============ globals ===============
        print("Initialising globals... ", end='')
        bot = TeleBot(BOT_TOKEN)
        db = gsdb(GS_LINK)
        markup = MyMarkup(db)
        print("Done")

        self.register_reboot_handler()

        print("Initialising objects... ", end='')
        moderation = Moderation(bot, db)
        register = Register(bot, db)
        menu = MainMenu(bot)
        lessons = Lessons(bot, db, register)
        activities = Activities(bot, db)
        schedule = Schedule(bot, db)
        prices = Prices(bot, db)
        contacts = Contacts(bot, db)
        promotions = Promotions(bot, db)
        rent = Rent(bot, db)
        shop = Shop(bot, db)

        # команды должны быть в самом конце
        commands = Commands(bot, db)
        print("...Done")
        print("Bot started.")

    def register_reboot_handler(self):
        @bot.message_handler(commands=['restart', 'init', 'reboot', 'update'])
        def message(msg: types.Message):
            if not db.is_admin(msg.from_user):
                bot.send_message(chat_id=msg.chat.id, text=f"У вас не достаточно привелегий.\n")
                return
            InitGlobals()
            bot.send_message(chat_id=msg.chat.id, text=f"Перезагрузка завершена.")
