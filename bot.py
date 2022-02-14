#PROGRAMA QUE SE EJECUTA
# CON UN BOT DE TELEGRAM
# BY @juandinet
# DEBE INSTALAR EN PYTHON: pip install python-telegram-bot
#  debe cambiar el token por el que le corresponda en la configuración
# y cambiar el nombre del archivo a config.json

import json
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def start(update, context):
    update.message.reply_text('Hola Mundo!')
    print('Hola Mundo!')

def otra(update, context):
    update.message.reply_text('ejecutando otra funcion')
    print('Ejecutó otra función')

def salir(update, context):
    update.message.reply_text('Saliendo...')
    print('Salida')
    exit()

def main():
    with open('config.json') as config_file:
        config = json.load(config_file)['configuracion']
        #print(config['token'])
    updater = Updater(config['token'], use_context=True)
    dp = updater.dispatcher
    #se agregan los Handler que reciben los comandos
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('otra', otra))
    dp.add_handler(CommandHandler('salir', salir))
    #Se queda escuchando los comandos
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
    