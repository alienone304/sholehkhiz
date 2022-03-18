from django import forms
from products.models import ProductsModel


class ProductsForm(forms.ModelForm):


    class Meta:
        model = ProductsModel
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class':'uk-input fHarmattan','placeholder':'نام محصول'},),
            'picture': forms.FileInput(attrs={'class':'uk-button','id':'picture'},),
            'description': forms.Textarea(attrs={'class':'uk-textarea fHarmattan','rows':'5','placeholder':'توضیحات'},),
            'cataloge': forms.FileInput(attrs={'class':'uk-button','id':'cataloge'},),
            'size_1': forms.TextInput(attrs={'class':'uk-input fHarmattan','placeholder':'مدل اول'},),
            'size_2': forms.TextInput(attrs={'class':'uk-input fHarmattan','placeholder':'مدل دوم'},),
            'size_3': forms.TextInput(attrs={'class':'uk-input fHarmattan','placeholder':'مدل سوم'},),
            'size_4': forms.TextInput(attrs={'class':'uk-input fHarmattan','placeholder':'مدل چهارم'},),
            'size_5': forms.TextInput(attrs={'class':'uk-input fHarmattan','placeholder':'مدل پنجم'},),
            'size_6': forms.TextInput(attrs={'class':'uk-input fHarmattan','placeholder':'مدل ششم'},),
            'size_7': forms.TextInput(attrs={'class':'uk-input fHarmattan','placeholder':'مدل هفتم'},),
            'size_8': forms.TextInput(attrs={'class':'uk-input fHarmattan','placeholder':'مدل هشتم'},),
            'size_9': forms.TextInput(attrs={'class':'uk-input fHarmattan','placeholder':'مدل نهم'},),
            'size_10': forms.TextInput(attrs={'class':'uk-input fHarmattan','placeholder':'مدل دهم'},),
            'size_11': forms.TextInput(attrs={'class':'uk-input fHarmattan','placeholder':'مدل یازدهم'},),
            'size_12': forms.TextInput(attrs={'class':'uk-input fHarmattan','placeholder':'مدل دوازدهم'},),
            'size_13': forms.TextInput(attrs={'class':'uk-input fHarmattan','placeholder':'مدل سیزدهم'},),
            'size_14': forms.TextInput(attrs={'class':'uk-input fHarmattan','placeholder':'مدل چهاردهم'},),

        }
