from rest_framework import generics, permissions
from rest_framework import status

from telegram_bot.services import TelegramService
from .models import UserMessage
from .serializers import UserMessageSerializer


class UserMessageListView(generics.ListAPIView):
    queryset = UserMessage.objects.all()
    serializer_class = UserMessageSerializer
    permission_classes = [permissions.IsAuthenticated]


class CreateUserMessageView(generics.CreateAPIView):
    queryset = UserMessage.objects.all()
    serializer_class = UserMessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """Сохраняет сообщение и отправляет его в Telegram."""
        serializer.save(user=self.request.user)
        self.status_message = TelegramService.send_message(
            self.request.user, serializer.validated_data['message_body'])

    def create(self, request, *args, **kwargs):
        """Создает новое сообщение и возвращает ответ с дополнительным статусом."""
        response = super().create(request, *args, **kwargs)

        if response.status_code == status.HTTP_201_CREATED:
            response.data['status_message'] = self.status_message
        return response
