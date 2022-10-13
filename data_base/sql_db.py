import sqlite3 as sq
from create_bot import bot
from keyboards import keyboard as kb

def sql_start():
    global base, cur
    base = sq.connect('persona.db')
    cur = base.cursor()
    if base:
        print("Data base OK")
    base.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT,name TEXT PRIMARY KEY,history TEXT,weapon TEXT)')
    base.commit()

async def sql_name(message):
    for ret in cur.execute('SELECT * FROM menu').fetchall():
        kb.kb1.append(ret[1])

async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()

async def sql_read(message):
    for ret in cur.execute('SELECT * FROM menu').fetchall():
        await bot.send_photo(message.from_user.id,ret[0],ret[1])
        await bot.send_message(message.from_user.id, ret[2])
        await bot.send_message(message.from_user.id, ret[3])
