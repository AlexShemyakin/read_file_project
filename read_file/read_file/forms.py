from django import forms

from .models import UploadedFile


class UploadedFileForm(forms.ModelForm):
    """Форма для загрузки файла."""

    class Meta:
        model = UploadedFile
        fields = ['file']
