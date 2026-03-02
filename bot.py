import os
import telebot
import random  # Librería para la función del dado

BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

# Registrar manejadores de mensajes
@bot.message_handler(commands=['start', 'hola'])
def enviar_bienvenida(mensaje):
    bot.reply_to(mensaje, "Hola, ¿cómo estás? Soy SRbot ¿En que puedo ayudarte?")

# Comando /info
@bot.message_handler(commands=['info'])
def enviar_info(mensaje):
    info_text = (
        "🤖 **Ficha Técnica de SRbot**\n\n"
        "🔹 **Desarrollador:** Serafín Roldán Esteban\n"
        "🔹 **Entorno:** Contenedor Docker (Python 3)\n"
        "🔹 **Librería:** pyTelegramBotAPI\n"
        "🔹 **Estado:** Operativo y aprendiendo."
    )
    bot.reply_to(mensaje, info_text, parse_mode='Markdown')

# Comando /dado 
@bot.message_handler(commands=['dado'])
def lanzar_dado(mensaje):
    numero = random.randint(1, 6)
    bot.reply_to(mensaje, f"🎲 Has lanzado el dado y ha salido un: {numero}")


@bot.message_handler(func=lambda msg: True)
def enviar_echo(mensaje):
    bot.reply_to(mensaje, mensaje.text)

# Escuchar peticiones
bot.infinity_polling()