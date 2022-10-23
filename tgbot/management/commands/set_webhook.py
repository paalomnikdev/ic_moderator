from django.core.management.base import BaseCommand, CommandError
import telegram
from ic_bot.settings import BOT_TOKEN, BOT_DOMAIN


class Command(BaseCommand):
    def handle(self, *args, **options):
        bot = telegram.Bot(BOT_TOKEN)
        webhook = '{}/tg/{}/'.format(BOT_DOMAIN, BOT_TOKEN)
        bot.set_webhook(webhook)

        print('Webhook set to: {}'.format(webhook))
