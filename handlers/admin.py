from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup
from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from data_base import sql_db
from keyboards import keyboard as kb

kb1 = []
character = ReplyKeyboardMarkup()
class FSMAdmin(StatesGroup):   #машина состояний
    photo = State()
    name = State()
    history = State()
    weapon = State()

#@dp.message_handler(commands=['add'],state=None)
async def add(message: types.Message):
    await FSMAdmin.photo.set()
    await message.reply('Загрузи фото')

#@dp.message_handler(state="*",commands='stop')
#@dp.message_handler(Text(equals='stop', ignore_case=True), state="*")
async def cancel(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('OK')

#@dp.message_handler(content_types=['photo'],state=FSMAdmin.photo)
async def load(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.reply('Введи имя и роль')

#@dp.message_handler(state=FSMAdmin.name)
async def name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.reply('Введи предысторию')

#@dp.message_handler(state=FSMAdmin.history)
async def history(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['history'] = message.text
    await FSMAdmin.next()
    await message.reply('Введи оружие')

#@dp.message_handler(state=FSMAdmin.weapon)
async def weapon(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['weapon'] = message.text

    await sql_db.sql_add_command(state)
    await state.finish()






def register_handlers_admin(dp : Dispatcher):
    dp.register_message_handler(add, commands=['add'], state=None)
    dp.register_message_handler(cancel, state='*', commands='stop')
    dp.register_message_handler(cancel, Text(equals='stop', ignore_case=True), state='*')
    dp.register_message_handler(load, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(name, state=FSMAdmin.name)
    dp.register_message_handler(history, state=FSMAdmin.history)
    dp.register_message_handler(weapon, state=FSMAdmin.weapon)

