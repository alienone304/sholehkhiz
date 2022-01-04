from django import forms
from order.models import OrderingModel
from django.core import validators

class OrderingForm(forms.ModelForm):
    Hfield = forms.CharField(required=False,widget =forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
    class Meta:
        model = OrderingModel
        fields = ('description', 'number')
        widgets = {
            'number': forms.NumberInput(attrs={'class':'uk-input fHarmattan redC-text','placeholder':'تعداد'},),
            'description': forms.Textarea(attrs={'class':'uk-textarea fHarmattan','rows':'4','placeholder':'توضیحات'},),
        }
