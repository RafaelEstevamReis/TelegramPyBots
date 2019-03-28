# -*- coding: utf-8 -*-
#import pyserial pip install pyserial


token = ''

import serial
import logging
from time     import sleep
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler,MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

ser = serial.Serial('COM4', timeout=0)  # open first serial port | timeout={None:wait forever, 0: non-blocking mode, x: x seconds }

def start(bot, update):
    update.message.reply_text("Olá, {}!".format(update.message.from_user.first_name))

def liga(bot, update):
    serial("1")
    update.message.reply_text("Feito");
def desliga(bot, update):
    serial("2")
    update.message.reply_text("Feito");
    
def readPotentiometer(bot, job):
    ser.read(512) # eat entire buffer
    serial("p")
    sleep(0.5)
    cc=str(ser.readline())
    line = cc[3:-5]
    vFloat = int(line)/1024.0
    bot.send_message(chat_id=119947806, text="Valor Atual: {:.1f}".format(vFloat*40-10))

def monitorar(bot, update, job_queue,chat_data,args):
    job = job_queue.run_repeating(sayhi, 5, context=update)
    
def serial(content):
    ser.write(content.encode('utf-8'))      # write a string
    
def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater(token)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('help', start))
    
    
    updater.dispatcher.add_handler(CommandHandler('abre', liga))
    updater.dispatcher.add_handler(CommandHandler('fecha', desliga))
    
    updater.dispatcher.add_handler(CommandHandler('ler', readPotentiometer))
    
    updater.dispatcher.add_handler(CommandHandler("monitorar", monitorar,
                                                  pass_args=True,
                                                  pass_job_queue=True,
                                                  pass_chat_data=True))
    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()
    
    

if __name__ == '__main__':
    main()
    ser.close()
