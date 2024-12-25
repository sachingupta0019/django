from django import forms
from .models import ImgBoxDB

class ImageUploaderForm(forms.ModelForm):
    class Meta:
        model = ImgBoxDB
        fields = ['photo']
        labels = {'photo' : ''}
        widgets = {
            'photo' : forms.ClearableFileInput(
                attrs = {
                    'class':'p-5 border border-4 text-black bg-body-tertiary form-control-lg custom-file-input',
                    }
                )
            }
                             