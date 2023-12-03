from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    create_chatroom,
    list_chatrooms,
    leave_chatroom,
    enter_chatroom,
    send_message,
    list_messages,
)

router = DefaultRouter()
router.register(r'create_chatroom', create_chatroom, basename='create_chatroom')

urlpatterns = [
    path('create_chatroom/', create_chatroom, name='create_chatroom'),
    path('list_chatrooms/', list_chatrooms, name='list_chatrooms'),
    path('leave_chatroom/', leave_chatroom, name='leave_chatroom'),
    path('enter_chatroom/', enter_chatroom, name='enter_chatroom'),
    path('send_message/', send_message, name='send_message'),
    path('list_messages/<int:chatroom_id>/', list_messages, name='list_messages'),
]
