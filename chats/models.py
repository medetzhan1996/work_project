from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class UserMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    message_body = models.TextField()
