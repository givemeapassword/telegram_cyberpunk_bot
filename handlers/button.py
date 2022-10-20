from keyboards import keyboard as kb
from aiogram import Dispatcher
from create_bot import bot
from data_base import sql_db


#@dp.message_handler(commands=['pers'])
async def persona(message):
	await sql_db.sql_read(message)
#@dp.message_handler(commands=['start'])
async def start(message):
	await sql_db.names()
	await bot.send_message(message.chat.id, 'Здарова,чумба', reply_markup=sql_db.character)

#@dp.message_handler(commands = ['del_all'])
async def delete(message):
	await bot.send_message(message.chat.id, 'Здарова,чумба', reply_markup=sql_db.character)
	await sql_db.delete_all(message)

#@dp.message_handler(commands = ['del_name'])
async def delete_name(message):
	await sql_db.del_obj(message)
	pass

def register_handler_buttton(dp : Dispatcher):
	dp.register_message_handler(persona, commands=['pers'])
	dp.register_message_handler(start, commands=['start'])
	dp.register_message_handler(delete, commands=['del_all'])
	dp.register_message_handler(delete_name, commands=['del_name'])