from django.urls import path

from .views import CreateUserMessageView, UserMessageListView

urlpatterns = [
    path('send_message/', CreateUserMessageView.as_view(), name='send_message'),
    path('user_messages/', UserMessageListView.as_view(), name='user_message_list'),
]
