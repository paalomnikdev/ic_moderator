from django.urls import path, include
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [  
    # # TODO: make webhook more secure
    path('', views.index, name="index"),
    path('{}/'.format(settings.BOT_TOKEN), csrf_exempt(views.TelegramBotWebhookView.as_view())),
]
