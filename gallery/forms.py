from django import forms

# handmade
from gallery.models import GalleryModel, VideoModel

class GalleryForm(forms.ModelForm):
    class Meta():
        model = GalleryModel
        fields = ('picture','description','for_product','for_factory','for_workers','for_sundry','for_excebition')
        widgets = {
            'picture': forms.FileInput(attrs={'class':'uk-button',},),
            'for_product': forms.CheckboxInput(attrs={'class':'uk-checkbox fHarmattan '},),
            'for_factory': forms.CheckboxInput(attrs={'class':'uk-checkbox fHarmattan '},),
            'for_workers': forms.CheckboxInput(attrs={'class':'uk-checkbox fHarmattan '},),
            'for_sundry': forms.CheckboxInput(attrs={'class':'uk-checkbox fHarmattan '},),
            'for_excebition': forms.CheckboxInput(attrs={'class':'uk-checkbox fHarmattan '},),
            'description': forms.Textarea(attrs={'class':'uk-textarea fHarmattan','rows':'2','placeholder':'توضیحات'},),
        }


class VideoForm(forms.ModelForm):
    class Meta():
        model = VideoModel
        fields = '__all__'
        widgets = {
            'video': forms.FileInput(attrs={'class':'uk-button',},),
            'description': forms.Textarea(attrs={'class':'uk-textarea fHarmattan','rows':'2','placeholder':'توضیحات'},),  
            }
