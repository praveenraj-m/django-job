
from django import forms
from uploadapp.models import Uploads, UploadFile


class Uploadform(forms.ModelForm):
    class Meta:
        model = Uploads
        fields = '__all__'

class UPloadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = '__all__'        