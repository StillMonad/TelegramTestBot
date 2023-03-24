from globals import bot, db
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

if __name__ == '__main__':
    print("Initialising objects... ", end='')

    moderation = Moderation(bot, db)
    menu = MainMenu(bot)
    lessons = Lessons(bot, db)
    activities = Activities(bot, db)
    schedule = Schedule(bot, db)
    prices = Prices(bot, db)
    contacts = Contacts(bot, db)
    promotions = Promotions(bot, db)
    rent = Rent(bot, db)
    shop = Shop(bot, db)
    commands = Commands(bot, db)

    print("...Done")
    print("Bot started.")
    bot.infinity_polling(skip_pending=True)
    bot.send_invoice()
