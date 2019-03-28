# -*- coding: utf-8 -*-
#import pyserial pip install pyserial


token = ''

import serial
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram.ext import MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

ser = serial.Serial('COM3')  # open first serial port

def start(bot, update):
    update.message.reply_text("Olá, {}!".format(update.message.from_user.first_name))

def liga(bot, update):
    serial("1");
    update.message.reply_text("Feito");
    
def desliga(bot, update):
    serial("2");
    update.message.reply_text("Feito");

def serial(content):
    ser.write(content.encode('utf-8'))      # write a string
    
def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater(token)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('help', start))
    
    
    updater.dispatcher.add_handler(CommandHandler('on', liga))
    updater.dispatcher.add_handler(CommandHandler('abre', liga))
    
    updater.dispatcher.add_handler(CommandHandler('off', desliga))
    updater.dispatcher.add_handler(CommandHandler('fecha', desliga))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()
    ser.close()
