from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from credentials import token
import logging

from dummy_data import dummy_speiseplan


# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


def essenjetzt(update: Update, context: CallbackContext) -> None:
    """
    Replies with current menu options.
    """
    names_and_prices = [f"{menu_option['name']} ({menu_option['preis']})" for menu_option in dummy_speiseplan['gericht']]
    menu_options = '\n'.join(names_and_prices)
    reply = f"Essen Jetzt!\n\n{menu_options}"
    update.message.reply_text(reply)


def unknown(update: Update, context: CallbackContext) -> None:
    """
    Default reply on unknown command.
    """
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hä. Hunger? Versuchs mit /essenjetzt.')


updater = Updater(token)

# Add handlers for incoming commands
updater.dispatcher.add_handler(CommandHandler('essenjetzt', essenjetzt))

# Add handler for unknown command
unknown_handler = MessageHandler(Filters.command, unknown)
updater.dispatcher.add_handler(unknown_handler)

# Start bot
updater.start_polling()
updater.idle()