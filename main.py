from email import message
import telebot
import config
import text as tx
import button as bt

bot = telebot.TeleBot(config.TOKEN)

check = 0


#начальный список всех персонажей
@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, tx.start1 ,reply_markup=bt.Base)



#Описание персонажей
@bot.message_handler(content_types=['text'])
def bot_message(message):
	if message.chat.type =='private':
		if message.text == 'Фрейзер':
			check = 1
			bot.send_message(message.chat.id, tx.Freizer,reply_markup=bt.characterisation)
		elif message.text == 'Гриз':
			check = 2
			bot.send_message(message.chat.id, tx.Griz,reply_markup=bt.characterisation)
		elif message.text == 'Кептер':
			check = 3
			bot.send_message(message.chat.id, tx.Kepter,reply_markup=bt.characterisation)
		elif message.text == 'Двейн':
			check = 4
			bot.send_message(message.chat.id, tx.Dvain,reply_markup=bt.characterisation)
		elif message.text == 'Вано':
			check = 5
			bot.send_message(message.chat.id, tx.Vano,reply_markup=bt.characterisation)
		elif message.text == 'Рауль':
			check = 6
			bot.send_message(message.chat.id, tx.Raul,reply_markup=bt.characterisation)
		else:
			bot.send_message(message.chat.id, "как ты это сделал, чумб?!")
	

@bot.callback_query_handler(func=lambda call:True)
def call_back(call):
	if call.data=='1':
		bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Пыщь")

#постоянный пуллинг данных
if __name__ == '__main__':
    bot.polling(none_stop=True)

