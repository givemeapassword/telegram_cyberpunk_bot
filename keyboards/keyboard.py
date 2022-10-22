from aiogram.types import ReplyKeyboardMarkup
character1 = ReplyKeyboardMarkup()
main_menu = ["Удалить персонажа",
             "Добавить персонажа",
             "Посмотреть всех персонажей",
             "Назад"
             ]
for i in main_menu:
    character1.add(i)