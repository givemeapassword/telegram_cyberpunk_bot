import sqlite3 as sq
from create_bot import bot
from keyboards import keyboard as kb
from aiogram.types import KeyboardButton,ReplyKeyboardMarkup
kb1 = 0
character = ReplyKeyboardMarkup()
character.add('a')
ret1 = []
def sql_start():
    global base, cur
    base = sq.connect('persona.db')
    cur = base.cursor()
    if base:
        print("Data base OK")
    base.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT,name TEXT PRIMARY KEY,history TEXT,weapon TEXT)')
    base.commit()



async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()

async def sql_read(message):
    for ret in cur.execute('SELECT * FROM menu').fetchall():
        await bot.send_photo(message.from_user.id,ret[0],ret[1])
        await bot.send_message(message.from_user.id, ret[2])
        await bot.send_message(message.from_user.id, ret[3])
async def names():
    for ret in cur.execute('SELECT name FROM menu').fetchall():
        character.add(str(ret[0]))
        ret1.append(ret)
    print(ret1)
    return ret1

async def info_out(name): #для выписки данных имени
    r = cur.execute('SELECT img,history,weapon FROM menu WHERE name == ?', (str(name))).fetchall()
    await bot.send_photo(message.from_user.id, r[0])
    print(r)
    return r

async def del_obj(message):
async def delete_all(message):
    cur.execute('DELETE * FROM menu')
    bot.send_message(message.from_user.id,"СОВЕРШЕННА ПОЛНАЯ ЛИКВИДАЦИЯ!!!")
    pass
async def delete():
    pass

