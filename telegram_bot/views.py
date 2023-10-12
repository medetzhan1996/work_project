import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

from rest_framework import generics, permissions
from rest_framework.response import Response

from .models import TelegramProfile
from .serializers import TelegramProfileSerializer
from .services import TelegramProfileService


class GenerateTokenView(generics.CreateAPIView):
    queryset = TelegramProfile.objects.all()
    serializer_class = TelegramProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        profile, created = TelegramProfile.objects.get_or_create(user=request.user)
        profile.generate_token()
        return Response({"token": profile.token})


class TelegramWebhook(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        json_str = request.body.decode('UTF-8')
        update = json.loads(json_str)
        TelegramProfileService.handle_webhook(update)
        return JsonResponse({"status": "ok"})
