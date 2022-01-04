from django import forms
from django.core import validators
from company.models import ContactUsModel, ComplaintModel

class ContactUsForm(forms.ModelForm):
    Hfield = forms.CharField(required=False,widget =forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    class Meta():
        model = ContactUsModel
        fields = ('name','email','phone_number','request')
        widgets = {
            'name': forms.TextInput(attrs={'class':'uk-input fHarmattan redC-text','placeholder':'نام و نام خانوادگی'},),
            'phone_number': forms.TextInput(attrs={'class':'uk-input fHarmattan','placeholder':'شماره تماس'},),
            'request': forms.Textarea(attrs={'class':'uk-textarea fHarmattan','rows':'4','placeholder':'متن درخواست یا پیشنهاد'},),
            'email': forms.EmailInput(attrs={'class':'uk-input fHarmattan','placeholder':'ایمیل'},),

        }

class ComplaintForm(forms.ModelForm):
    Hfield = forms.CharField(required=False,widget =forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
    class Meta():
        model = ComplaintModel
        fields = ('name','picture','phone_number','request')
        widgets = {
            'name': forms.TextInput(attrs={'class':'uk-input fHarmattan redC-text','placeholder':'نام و نام خانوادگی'},),
            'phone_number': forms.TextInput(attrs={'class':'uk-input fHarmattan','placeholder':'شماره تماس'},),
            'request': forms.Textarea(attrs={'class':'uk-textarea fHarmattan','rows':'4','placeholder':'متن شکایت'},),
            'picture': forms.FileInput(attrs={'class':'uk-button',},),
        }
