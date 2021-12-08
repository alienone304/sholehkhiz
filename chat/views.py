from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
import datetime
from django.utils import timezone

import pytz
from django.contrib.auth.decorators import login_required

from chat.models import ChatSessionModel, ChatMessageModel
from commonuser.decorators import commonuser_required
from accounts.decorators import superuser_required
from chat.forms import ChatForm


def CreateChatSessionView(request):
    ChatSession = ChatSessionModel.objects.create(is_active = False)
    return render(request,'chat/createsession.html',{'chatsession':ChatSession})


@login_required
@superuser_required
def PendingChatSessionListView(request):
    DeleteInactiveChats(request)
    ChatSessions = ChatSessionModel.objects.all()
    return render(request,'chat/pendingchatsessionlist.html',
                      {'chatsession_list':ChatSessions})


@login_required
@superuser_required
def ActivateChatSessionView(request, pk):
    ChatSession = get_object_or_404(ChatSessionModel, pk= pk)
    ChatSession.is_active = True
    ChatSession.superuser = request.user
    ChatSession.save()
    return HttpResponseRedirect(reverse('chat:chatting',kwargs={'pk':ChatSession.pk}))



def ChattingView(request, pk):
    ChatSession = get_object_or_404(ChatSessionModel, pk = pk)
    return render(request,'chat/chatting.html',
                  {'chatsession':ChatSession})

def SendMessage(request,pk):
    ChatSession = get_object_or_404(ChatSessionModel, pk = pk)
    now = timezone.now()
    if request.method == 'POST':
        if request.user.is_superuser:
            message = request.POST['message']
            new_message = ChatMessageModel(message = message, chatsession = ChatSession, of_superuser = True, message_datetime = now)
            new_message.save()
            ChatSession.last_message_datetime = now
            ChatSession.save()
            return HttpResponse(message)
        else:
            message = request.POST['message']
            new_message = ChatMessageModel(message = message, chatsession = ChatSession, of_superuser = False, message_datetime = now)
            new_message.save()
            ChatSession.last_message_datetime = now
            ChatSession.save()
            return HttpResponse(message)


def GetUserMessage(request,pk):
    ChatSession = get_object_or_404(ChatSessionModel, pk = pk)
    Messages = ChatMessageModel.objects.filter(chatsession = ChatSession)
    return JsonResponse({"messages":list(Messages.values())})


def CheckActivity(request,pk):
    ChatSession = get_object_or_404(ChatSessionModel, pk = pk)
    is_active = ChatSession.is_active
    return JsonResponse({"is_active":is_active})


@login_required
@superuser_required
def DeleteInactiveChats(request):
    ChatSessions = ChatSessionModel.objects.all()
    now = timezone.now()

    for ChatSession in ChatSessions:
        message_dead_line = ChatSession.last_message_datetime + datetime.timedelta(minutes = 30)
        #message_dead_line = utc.localize(message_dead_line)
        dead_line = ChatSession.started_at + datetime.timedelta(minutes = 30)
        if (ChatSession.is_active and now > message_dead_line) or ((not ChatSession.is_active) and now > dead_line):
            ChatSession.delete()


@login_required
@superuser_required
def DeleteChatSessionView(request,pk):
    ChatSession = get_object_or_404(ChatSessionModel, pk = pk)
    ChatSession.delete()
    return HttpResponseRedirect(reverse('chat:pendingchatsessionlist'))
