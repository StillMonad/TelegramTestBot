from telebot import TeleBot, types
from config import BOT_TOKEN, GS_LINK
from database.gsconnect import gsdb
from markup.markups import my_markup
from src.classes.data import data

# ============ globals ===============
print("Initialising globals... ", end='')
bot = TeleBot(BOT_TOKEN)
db = gsdb(GS_LINK)
markup = my_markup(db)
print("Done")