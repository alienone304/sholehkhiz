from django.urls import include, path
from chat.views import (CreateChatSessionView, ChattingView, PendingChatSessionListView,
                        ActivateChatSessionView, SendMessage, GetUserMessage,
                        CheckActivity, DeleteChatSessionView)

app_name ='chat'
urlpatterns = [
    path('create-chat/', CreateChatSessionView, name='createchatsession'),
    path('chatting/<int:pk>/', ChattingView, name='chatting'),
    path('pending-chats/', PendingChatSessionListView, name='pendingchatsessionlist'),
    path('activate-chat/<int:pk>/', ActivateChatSessionView, name='activatechat'),
    path('send-message/<int:pk>/', SendMessage, name='sendmessage'),
    path('get-user-message/<int:pk>/', GetUserMessage, name='getusermessage'),
    path('check-activity/<int:pk>/', CheckActivity, name='checkactivity'),
    path('delete-session/<int:pk>/', DeleteChatSessionView, name='deletechatsession'),

]
