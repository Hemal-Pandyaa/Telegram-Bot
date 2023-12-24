from telegram import Update
from telegram.ext import ApplicationBuilder,CommandHandler,ContextTypes

TOKEN = r"6769810228:AAE6YQZ10aOaroCk_a6sb8tQOlwYCNDUytk"

async def start(update : Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hello There, This bot will give you help you get your favorite minecraft mod"
    )
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="How may I help You. Use /help for more information"
    )

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Type name of any mod"
    )

if __name__ == "__main__":
    print("Bot Started")
    bot = ApplicationBuilder().token(token=TOKEN).build()

    start_command_handler = CommandHandler("start",start)
    help_command_handler = CommandHandler("help",help)
    bot.add_handlers([start_command_handler,help_command_handler])

    print("Started Polling!")
    bot.run_polling()