from keyboards import keyboard as kb
from aiogram import Dispatcher
from create_bot import bot
from data_base import sql_db


#@dp.message_handler(commands=['pers'])
async def persona(message):
	await sql_db.sql_read(message)
#@dp.message_handler(commands=['start'])
async def start(message):
	await sql_db.sql_name(message)
	await bot.send_message(message.chat.id, 'dsdadadada', reply_markup=kb.character)

def register_handler_buttton(dp : Dispatcher):
	dp.register_message_handler(persona, commands=['pers'])
	dp.register_message_handler(start, commands=['start'])