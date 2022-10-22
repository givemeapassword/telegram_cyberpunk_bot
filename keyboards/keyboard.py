from aiogram.types import ReplyKeyboardMarkup
character = ReplyKeyboardMarkup()
main_menu = ["Удалить персонажа💀",
             "Добавить персонажа✅",
             "Посмотреть всех персонажей🦕",
             "Назад↩"
             ]
for i in main_menu:
    character.add(i)