import telebot
from telebot import types
bot = telebot.TeleBot('8475840146:AAFV6jH14M1Bma-gPT0PoXpULRw-KF8AgKc')


@bot.message_handler(func=lambda message: message.text == 'Алгебра')
def algebra(message):
    books(message)



@bot.message_handler(content_types=['photo'])
def get_photo(message):
    bot.reply_to(message, 'good photo')


@bot.message_handler(commands =['start'])
def start(message):
    bot.send_message(message.chat.id,f'<b>Привет {message.from_user.first_name}!</b>',parse_mode='html')
    bot.send_message(message.chat.id, '<a href="https://zastavki.gas-kvas.com/uploads/posts/2024-09/zastavki-gas-kvas-com-ypzi-p-zastavki-na-telefon-smeshnie-s-nadpisyami-1.jpg"><b>Заходи!</b></a>', parse_mode='html', disable_web_page_preview=True)


@bot.message_handler(commands =['help'])
def hp(message):
    bot.send_message(message.chat.id,'<b><u>/start</u> - начать</b>',parse_mode='html')


@bot.message_handler(commands =['books'])
def books(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Алгебра', callback_data='Algebra'))
    bot.send_message(message.chat.id, 'Вот книги👇', reply_markup=markup)



@bot.callback_query_handler(lambda callback: True)
def callback_message(callback):
    if callback.data == 'Algebra':
            with open('Algebra.pdf','rb') as file:
                bot.send_document(callback.message.chat.id, file)

@bot.message_handler(commands =['site','website'])
def site(message):
    markup = types.InlineKeyboardMarkup()
    url = 'https://photofile.ru/wp-content/uploads/2024/04/79b9dpy0sag.jpg'
    markup.add(types.InlineKeyboardButton('Открыть сайт',url = url))
    bot.send_message(message.chat.id, 'Вот сайт👇',reply_markup=markup)

@bot.message_handler()
def hello(message):
    if message.text.lower() == 'привет':
        start(message)
    elif message.text.lower() == 'id':
        bot.reply_to(message,message.from_user.id)


bot.infinity_polling()











