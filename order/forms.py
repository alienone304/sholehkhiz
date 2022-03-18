from django import forms
from order.models import OrderingModel
from django.core import validators

class OrderingForm(forms.ModelForm):
    Hfield = forms.CharField(required=False,widget =forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
    class Meta:
        model = OrderingModel
        fields = ('number','description','number_1','number_2','number_3','number_4','number_5',
            'number_6','number_7','number_8','number_9','number_10','number_11','number_12',
            'number_13','number_14',)
        widgets = {
            'number': forms.NumberInput(attrs={'class':'uk-input fHarmattan redC-text','placeholder':'تعداد'},),
            'description': forms.Textarea(attrs={'class':'uk-textarea fHarmattan','rows':'4','placeholder':'توضیحات'},),
            'number_1': forms.TextInput(attrs={'class':'uk-input fHarmattan','placeholder':'تعداد سفارش از این مدل'},),
            'number_2': forms.TextInput(attrs={'class':'uk-input fHarmattan','placeholder':'تعداد سفارش از این مدل'},),
            'number_3': forms.TextInput(attrs={'class':'uk-input fHarmattan','placeholder':'تعداد سفارش از این مدل'},),
            'number_4': forms.TextInput(attrs={'class':'uk-input fHarmattan','placeholder':'تعداد سفارش از این مدل'},),
            'number_5': forms.TextInput(attrs={'class':'uk-input fHarmattan','placeholder':'تعداد سفارش از این مدل'},),
            'number_6': forms.TextInput(attrs={'class':'uk-input fHarmattan','placeholder':'تعداد سفارش از این مدل'},),
            'number_7': forms.TextInput(attrs={'class':'uk-input fHarmattan','placeholder':'تعداد سفارش از این مدل'},),
            'number_8': forms.TextInput(attrs={'class':'uk-input fHarmattan','placeholder':'تعداد سفارش از این مدل'},),
            'number_9': forms.TextInput(attrs={'class':'uk-input fHarmattan','placeholder':'تعداد سفارش از این مدل'},),
            'number_10': forms.TextInput(attrs={'class':'uk-input fHarmattan','placeholder':'تعداد سفارش از این مدل'},),
            'number_11': forms.TextInput(attrs={'class':'uk-input fHarmattan','placeholder':'تعداد سفارش از این مدل'},),
            'number_12': forms.TextInput(attrs={'class':'uk-input fHarmattan','placeholder':'تعداد سفارش از این مدل'},),
            'number_13': forms.TextInput(attrs={'class':'uk-input fHarmattan','placeholder':'تعداد سفارش از این مدل'},),
            'number_14': forms.TextInput(attrs={'class':'uk-input fHarmattan','placeholder':'تعداد سفارش از این مدل'},),
        }
