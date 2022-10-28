from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from write_log import *

async def student(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'hi {update.effective_user.first_name}')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'/hi\n/time\n/help\n/sum\n/sub\n/mult\n/div')

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    z = x + y
    await update.message.reply_text(f'{x} + {y} = {z}')

async def div_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    z = x / y
    await update.message.reply_text(f'{x} / {y} = {z}')

async def sub_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    z = x - y
    await update.message.reply_text(f'{x} - {y} = {z}')

async def mult_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    z = x * y
    await update.message.reply_text(f'{x} * {y} = {z}')