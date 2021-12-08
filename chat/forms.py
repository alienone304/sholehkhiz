from django import forms
from chat.models import ChatMessageModel

class ChatForm(forms.ModelForm):
    class Meta():
        model = ChatMessageModel
        fields = ('message',)
        widgets = {
            'message': forms.Textarea(attrs={'name':'message','id':'message','class':'uk-textarea fHarmattan','rows':'2','placeholder':'متن'},),
        }
