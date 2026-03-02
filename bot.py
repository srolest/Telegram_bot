import os
import telebot

BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

# Registrar manejadores de mensajes
@bot.message_handler(commands=['start', 'hola'])
def enviar_bienvenida(mensaje):
    bot.reply_to(mensaje, "Hola, ¿cómo estás?")

@bot.message_handler(func=lambda msg: True)
def enviar_echo(mensaje):
    bot.reply_to(mensaje, mensaje.text)

# Escuchar peticiones
bot.infinity_polling()