import telebot
import webbrowser

bot = telebot.TeleBot('7231229744:AAHr_YKtl71tcigXqZGX358tpLViXIK6q-Q')

@bot.message_handler(commands = ['site', 'website'])
def site(message):
    webbrowser.open('http://itproger.com')

@bot.message_handler(commands=['start', 'main', 'hello'])
def main(message):
    bot.send_message(message.chat.id,f'Hello!, {message.from_user.first_name} {message.from_user.last_name}')

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Help</b> <em><u>information</u></em>', parse_mode='html')

@bot.message_handler()
def info(message):
    if message.text.lower() == '':
        bot.send_message(message.chat.id,f'Hello!, {message.from_user.first_name} {message.from_user.last_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')
    elif message.text.lower() == '/start':
           bot.send_message(message.chat.id,f'Hello!, {message.from_user.first_name} {message.from_user.last_name}')


bot.polling(non_stop=True)