from rest_framework import serializers
from .models import TelegramProfile


class TelegramProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramProfile
        fields = ['user', 'telegram_id', 'token']

