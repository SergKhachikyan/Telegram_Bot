import telebot
from telebot import types

bot = telebot.TeleBot('7231229744:AAHr_YKtl71tcigXqZGX358tpLViXIK6q-Q')

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Go to site', url = 'https://google.com'))
    markup.add(types.InlineKeyboardButton('Delete photo', callback_data = 'delete'))
    markup.add(types.InlineKeyboardButton('Change the text', callback_data = 'edit'))

    bot.reply_to(message, 'What a beautiful picture',reply_markup = markup)

bot.polling(non_stop=True)