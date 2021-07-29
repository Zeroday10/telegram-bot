from telegram.ext import Updater, CommandHandler

token = '860529509:AAGGFqxvfW67TFK5VKpHyv-Ky1axKBNsF5E'

def start_handler(bot, update):
    chat_id = update.message.chat_id
    first_name = update.message.chat.first_name
    last_name = update.message.chat.last_name
    bot.send_message(chat_id = chat_id, text = 'سلام {} {} /n به ربات ما خوش آمدید'.format(first_name, last_name))


updater = Updater(token = token)

start_command = CommandHandler('start', start_handler)

updater.dispatcher.add_handler(start_command)

updater.start_polling()

updater.idle()