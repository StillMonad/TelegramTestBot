from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from src.tools import tr

class textbox:
    def __init__(self, len, parent=None, markup=None):
        super().__init__(parent=parent, type='slider')
        self.len = len
        self.pos = 1
        self.markup = self.markup_text(markup)

    def markup_text(self, markup):
        textbox = InlineKeyboardMarkup() if (markup is None) else markup
        if not (self.parent is None):
            textbox.add(InlineKeyboardButton("Назад", callback_data=self.parent))
        return textbox
