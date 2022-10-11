from telebot import types



#ОСНОВА
Base = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
persona1=types.KeyboardButton('Гриз',)
persona2=types.KeyboardButton('Фрейзер')
persona3=types.KeyboardButton('Кептер')
persona4=types.KeyboardButton('Двейн')
persona5=types.KeyboardButton('Вано')
persona6=types.KeyboardButton('Рауль')
persona7=types.KeyboardButton('Новый персонаж')
#persona8=types.KeyboardButton('')
Base.add(persona1,persona2,persona3,persona4,persona5,persona6,persona7)


#Вся характеристика
characterisation = types.InlineKeyboardMarkup()
characteristic = types.InlineKeyboardButton('Характеристики',callback_data='1')
skill = types.InlineKeyboardButton('Навыки',callback_data='1')
weapon = types.InlineKeyboardButton('Оружие и броня',callback_data='1')
history_and_character = types.InlineKeyboardButton('История и характер',callback_data='1')
characterisation.add(characteristic,skill,weapon,history_and_character)



#Отдельная для каждого перса