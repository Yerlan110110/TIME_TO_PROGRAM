import telebot

bot = telebot.TeleBot('8475840146:AAFV6jH14M1Bma-gPT0PoXpULRw-KF8AgKc')


@bot.message_handler()
def hello(message):
    if message.text.lower() == 'привет':
        start(message)



@bot.message_handler(commands =['start'])
def start(message):
    bot.send_message(message.chat.id,f'<b>Привет {message.from_user.first_name}!</b>',parse_mode='html')


@bot.message_handler(commands =['help'])
def hp(message):
    bot.send_message(message.chat.id,'<b><u>/start</u> - начать</b>',parse_mode='html')


bot.infinity_polling()











