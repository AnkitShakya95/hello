from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Define your list of authorized user IDs
AUTHORIZED_USERS = [123456789, 987654321]  # Replace with actual Telegram user IDs

# Function to handle the /start command
def start(update: Update, context: CallbackContext):
    user_id = update.effective_user.id

    if user_id in AUTHORIZED_USERS:
        update.message.reply_text(f"Welcome, {update.effective_user.first_name}! You are authorized.")
    else:
        update.message.reply_text("You are not authorized to use this bot.")
        # Optionally stop further handling for unauthorized users
        return

# Function to handle any other command
def unknown(update: Update, context: CallbackContext):
    user_id = update.effective_user.id

    if user_id not in AUTHORIZED_USERS:
        update.message.reply_text("You are not authorized to use this bot.")
        return

    update.message.reply_text("Sorry, I didn't understand that command.")

def main():
    # Replace 'YOUR_TOKEN' with your actual bot token from BotFather
    TOKEN = "YOUR_TOKEN"

    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Register handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("unknown", unknown))

    # Start the bot
    updater.start_polling()
    print("Bot is running...")
    updater.idle()

if __name__ == "__main__":
    main()
