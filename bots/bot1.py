from telebot import *
from gtts import *

TOKEN = "1633084074:AAH3nAZRGMYT6hZo5NYOoGfyT1cPvzGiul8"

bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def greeting(message):
        print(message)
        keyboard = types.ReplyKeyboardMarkup(True)
        btn1 = types.KeyboardButton(text="Hello")
        keyboard.add(btn1)
        btn2 = types.KeyboardButton(text="Bye")
        keyboard.add(btn2)
        bot.send_message(message.chat.id, "HEllO", reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def handling(message):
    if message.text == 'month':
        keyboard = types.InlineKeyboardMarkup()
        bt1 = types.InlineKeyboardButton(text="January", callback_data="jan")
        bt2 = types.InlineKeyboardButton(text="February", callback_data="feb")
        bt3 = types.InlineKeyboardButton(text="March", callback_data="mar")
        bt4 = types.InlineKeyboardButton(text="April", callback_data="apr")
        keyboard.add(bt1)
        keyboard.add(bt2)
        keyboard.add(bt3)
        keyboard.add(bt4)
        bot.send_message(message.chat.id, "Choose, month:", reply_markup=keyboard)
    # text = message.text
    # speech = gTTS(text=text, lang='en', slow=False)
    # speech.save("audio.mp3")
    # f = open("audio.mp3", 'rb')
    # bot.send_audio(message.chat.id, f)

@bot.callback_query_handler(func=lambda call: True)
def month_handler(call):
    print(call)
    if call.data == 'jan':
        bot.send_message(call.message.chat.id, "In January 31 days")
    elif call.data == 'feb':
        bot.send_message(call.message.chat.id, "In February 28-29 days")
    elif call.data == 'mar':
        bot.send_message(call.message.chat.id, "In March 31 days")
    elif call.data == 'apr':
        bot.send_message(call.message.chat.id, "In April 30 days")


bot.polling()