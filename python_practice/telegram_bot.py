import telebot

TOKEN = '5413692022:AAEAZz7cbJDwZ2gS3NxvazpHL7kHexg0tgo'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['voice'])
def repeat(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'Привет!')

@bot.message_handler(commands=['start', 'help'])
def hendle_start_help(message: telebot.types.Message):
    bot.reply_to(message, f"Привет, {message.chat.username}")
    print(message.text)

@bot.message_handler(content_types=['photo', ])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, 'Nice meme XDD')

@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message: telebot.types.Message):
    bot.reply_to(message, 'Привет, загружено')


bot.polling(none_stop=True)