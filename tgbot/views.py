import json
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from ic_bot.settings import DEBUG

from tgbot.dispatcher import process_telegram_event


def index(request):
    return JsonResponse({"error": "FU hacker"})

class TelegramBotWebhookView(View):
    # WARNING: if fail - Telegram webhook will be delivered again. 
    # Can be fixed with async celery task execution
    def post(self, request, *args, **kwargs):
        process_telegram_event(json.loads(request.body))


        # TODO: there is a great trick to send data in webhook response
        # e.g. remove buttons
        return JsonResponse({"ok": "POST request processed"})
    
    def get(self, request, *args, **kwargs):  # for debug
        return JsonResponse({"ok": True})
