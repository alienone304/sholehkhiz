from django.db import models
from accounts.models import UserModel
import datetime
from django.utils import timezone
import django


class ChatSessionModel(models.Model):
    superuser = models.ForeignKey(UserModel, null = True, on_delete = models.CASCADE)
    is_active = models.BooleanField(default = True)
    started_at = models.DateTimeField(null = False, default = django.utils.timezone.now)
    last_message_datetime = models.DateTimeField(null = False, default = django.utils.timezone.now)


class ChatMessageModel(models.Model):
    chatsession = models.ForeignKey(ChatSessionModel, null = False, on_delete = models.CASCADE, related_name='messages')
    message = models.TextField(null = True, blank = True)
    of_superuser = models.BooleanField(default = False)
    message_datetime = models.DateTimeField(null = False, default = django.utils.timezone.now)
