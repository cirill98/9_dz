from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_command import *




app = ApplicationBuilder().token("5408029107:AAGXJsWM_VkhRkMrli7H5jWq8mX66Q9qwOk").build()

app.add_handler(CommandHandler("hi", student))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("sub", sub_command))
app.add_handler(CommandHandler("mult", mult_command))
app.add_handler(CommandHandler("div", div_command))


print('Сервер запустился')

app.run_polling()