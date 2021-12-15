import sys
import telebot
import telebot.types

bot = telebot.TeleBot('5050007938:AAGTbhz9ufiRgIfDuiw0SS1eMd6DdNJTQ6k')

@bot.message_handler(content_types=['text'])
def compiler(message: telebot.types.Message):
    msgformatted = '\n'.join([f'\t{i}' for i in message.text.split('\n')])
    exec(f'jpxfrd = sys.stdout\nsys.stdout = open("output.txt", "w", encoding = "utf-8")\nsys.stderr = open("output.txt", "a", encoding = "utf-8")\ndef f():\n{msgformatted}\nf()\nsys.stdout = jpxfrd\nsys.stderr = jpxfrd2\n')
    output = open('output.txt', encoding='utf-8')
    bot.send_message(message.chat.id, output.read())
    output.close()

bot.infinity_polling()
