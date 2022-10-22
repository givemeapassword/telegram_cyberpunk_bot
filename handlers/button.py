from keyboards import keyboard as kb
from aiogram import Dispatcher
from create_bot import bot
from data_base import sql_db
from aiogram.types import ReplyKeyboardRemove
from handlers.admin import add

#@dp.message_handler(content_types=['text'])
async def text(message):
	global mes
	if message.text == 'Удалить персонажа':
		mes = message.text
		await bot.send_message(message.chat.id, 'Персонажи на удаление:', reply_markup=sql_db.character)
	elif (message.text == "Добавить персонажа"):
		await bot.send_message(message.chat.id, 'Пропиши /stop если не хочешь продолжать добавление:')
		await add(message)
	elif message.text == 'Посмотреть всех персонажей':
		await persona(message)
	elif message.text == 'Назад':
		await bot.send_message(message.chat.id,'Возвращаю',reply_markup=kb.character1)
	elif message.text in sql_db.ret1:
		if mes == 'Удалить персонажа':
			print('tut'+message.text)
			await sql_db.del_obj(message)
			await bot.send_message(message.chat.id, str(message.text) + ' УДАЛЕН!!!',reply_markup=ReplyKeyboardRemove())
	else:
		await bot.send_message(message.chat.id,'Удалили ехехехехеххе')


#@dp.message_handler(commands=['pers'])
async def persona(message):
	await sql_db.sql_read(message)
#@dp.message_handler(commands=['start'])
async def start(message):
	await sql_db.cleans()
	await sql_db.names(message)
	await bot.send_message(message.chat.id, 'Здарова,чумба', reply_markup=kb.character1)

#@dp.message_handler(commands = ['del_all'])
async def delete(message):
	await bot.send_message(message.chat.id, 'Здарова,чумба', reply_markup=sql_db.character)
	await sql_db.delete_all(message)

#@dp.message_handler(commands = ['del_name'])
async def delete_name(message):
	await sql_db.del_obj(message)

def register_handler_buttton(dp : Dispatcher):
	dp.register_message_handler(persona, commands=['pers'])
	dp.register_message_handler(start, commands=['start'])
	dp.register_message_handler(delete, commands=['del_all'])
	dp.register_message_handler(delete_name, commands=['del_name'])
	dp.register_message_handler(text)