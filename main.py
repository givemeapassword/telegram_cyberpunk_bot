from aiogram.utils import executor
from create_bot import dp
from data_base import sql_db
async def on_startup(_):
	print('Бот в онлайне')
	sql_db.sql_start()

from handlers import admin, button

admin.register_handlers_admin(dp)
button.register_handler_buttton(dp)



executor.start_polling(dp, skip_updates=True, on_startup=on_startup)