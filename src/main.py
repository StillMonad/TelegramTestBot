import globals


if __name__ == '__main__':
    g = globals.InitGlobals()
    globals.bot.infinity_polling(skip_pending=True)
