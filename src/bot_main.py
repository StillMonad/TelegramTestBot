from globals import bot, db, markup
from src.handlers.message_handlers import reg_message_handler
from src.handlers.inline_handlers import reg_inline_handler


if __name__ == '__main__':
    print("Initialising handlers... ", end='')
    reg_message_handler(bot, db, markup)
    reg_inline_handler(bot, db, markup)
    print("Done")
    print("Bot started.")
    bot.infinity_polling(skip_pending=True)
