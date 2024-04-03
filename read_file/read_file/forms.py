from django import forms

from .models import UploadedFile


class UploadedFileForm(forms.ModelForm):
    """Модель формы для загрузки файла."""

    class Meta:
        model = UploadedFile
        fields = ['file']
