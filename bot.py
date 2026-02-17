import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Get the bot token from environment variables
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Create the application
app = ApplicationBuilder().token(BOT_TOKEN).build()

# Command handler for the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Bot chal raha hai 24x7')

# Add the command handler to the application
app.add_handler(CommandHandler('start', start))

# Run the application
app.run_polling()