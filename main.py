from requests import Request
import src.globals as globals
from flask import Flask
from threading import Thread
import os
import requests
try:
    import src.config
except:
    pass

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>Greetings!</h1>"

def run():
    app.run(host='0.0.0.0', port=80)

def keep_alive():
    t = Thread(target=run)
    t.start()


if __name__ == "__main__":
    globals.InitGlobals()
    keep_alive()
    globals.bot.polling(non_stop=True, interval=0) #запуск бота