import telegram
from telegram.ext import (
    Updater, Dispatcher, Filters,
    CommandHandler, MessageHandler,
    InlineQueryHandler, CallbackQueryHandler,
    ChosenInlineResultHandler, PollAnswerHandler,
)
from ic_bot.settings import BOT_TOKEN
from tgbot.handlers import commands

def setup_dispatcher(dp):
    """
    Adding handlers for events from Telegram
    """

    dp.add_handler(CommandHandler('start', commands.command_start))
    dp.add_handler(CommandHandler('health', commands.health))
    dp.add_handler(CommandHandler('lang', commands.lang))
    dp.add_handler(CommandHandler('mute', commands.mute))

    return dp

def process_telegram_event(update_json):
    update = telegram.Update.de_json(update_json, bot)
    dispatcher.process_update(update)

bot = telegram.Bot(BOT_TOKEN)
dispatcher = setup_dispatcher(Dispatcher(bot, None, workers=0, use_context=True))
