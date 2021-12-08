from django.contrib import admin
from chat.models import ChatSessionModel, ChatMessageModel

admin.site.register(ChatSessionModel)
admin.site.register(ChatMessageModel)
