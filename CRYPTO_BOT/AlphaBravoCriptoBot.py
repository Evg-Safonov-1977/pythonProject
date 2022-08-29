import telebot
from config_AlphaBravoCriptoBot import keys, TOKEN
from extensions import APIException, CriptoConverter

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def welcome(message: telebot.types.Message):
    text = f'Здравствуйте, {message.chat.first_name}, я помогу сконвертировать интересующие вас валюты.' \
           f'\nДля этого прошу ввести через пробел:'\
           f'\n<из какой валюты> <в какую валюту> <количество>'\
           f'\nОбразец: рубль фунт_стерлингов 50'\
           f'\nНачать работу: /start'\
           f'\nПомощь: /help'\
           f'\nСписок доступных валют: /values'
    print(message.text)
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        if len(values) > 3:
            raise APIException('Вы ввели лишние значения. /help')
        elif len(values) < 3:
            raise APIException('Вы не ввели все необходимые значения, как в образце. /help')
        else:
            quote, base, amount = values
            total_base = CriptoConverter.get_price(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f'Я не могу сконвертировать, так как \n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'{message.chat.first_name}, {amount} {quote} составит {total_base} единиц в валюте {base}.'
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)