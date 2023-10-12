import telebot
from decouple import config

from .models import TelegramProfile


class TelegramService:

    @staticmethod
    def send_message(user, message_body):
        """Отправляет сообщение пользователю в Telegram."""
        telegram_profile = TelegramProfile.objects.filter(user=user).first()

        if not telegram_profile:
            return f"No Telegram profile found for user: {user}"

        message = f"{user.first_name}, я получил от тебя сообщение:\n{message_body}"
        bot_token = config('TELEGRAM_BOT_TOKEN')
        bot = telebot.TeleBot(bot_token)

        try:
            bot.send_message(chat_id=telegram_profile.telegram_id, text=message)
            return "Message sent successfully"
        except Exception as e:
            # Здесь может быть логирование ошибки
            return f"Failed to send message due to: {e}"


class TelegramProfileService:
    """Webhook telegram."""

    @staticmethod
    def handle_webhook(update):
        if 'message' not in update:
            return

        user_data = update['message']['from']
        telegram_id = user_data['id']
        token = update['message']['text']

        try:
            profile = TelegramProfile.objects.get(token=token)
            profile.telegram_id = telegram_id
            profile.save()
        except TelegramProfile.DoesNotExist:
            pass

