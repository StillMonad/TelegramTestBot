from telebot import TeleBot, types
from config import BOT_TOKEN, GS_LINK
from database.gsconnect import gsdb
from markups import MyMarkup
from src.objects.moderation import Moderation

# ============ globals ===============
print("Initialising globals... ", end='')
bot = TeleBot(BOT_TOKEN)
db = gsdb(GS_LINK)
markup = MyMarkup(db)
users = Moderation.get_users(db)
print("Done")
