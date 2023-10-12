from django.urls import path

from telegram_bot.views import GenerateTokenView, TelegramWebhook

urlpatterns = [
    path('generate-token/', GenerateTokenView.as_view(), name='generate_token'),
    path('webhook/', TelegramWebhook.as_view(), name='telegram_webhook'),
]
