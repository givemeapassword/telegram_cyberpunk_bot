from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from data_base import sql_db as sq

kb1 = ['a','b','c']
character = ReplyKeyboardMarkup()
for i in kb1:
    character.add(i)
