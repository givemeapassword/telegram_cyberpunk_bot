import sqlite3 as sq

from create_bot import bot
from aiogram.types import ReplyKeyboardMarkup,ReplyKeyboardRemove
character = ReplyKeyboardMarkup()
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
async def names(message):
    for ret in cur.execute('SELECT name FROM menu').fetchall():
        character.insert(ret[0])
        ret1.append(ret[0])
    character.add('Назад')
async def cleans():
    character.delete()

async def info_out(name): #для выписки данных имени
    r = cur.execute('SELECT img,history,weapon FROM menu WHERE name == ?', (str(name))).fetchall()
    base.commit()
    print(r)
    return r

async def del_obj(message):
    cur.execute('DELETE FROM menu WHERE name == ?', (message.text,))
    base.commit()

async def delete_all(message):
    cur.execute('DELETE FROM menu')
    base.commit()
    await bot.send_message(message.from_user.id,"СОВЕРШЕННА ПОЛНАЯ ЛИКВИДАЦИЯ!!!")


