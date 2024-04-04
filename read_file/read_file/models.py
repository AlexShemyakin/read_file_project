from django.db import models


class UploadedFile(models.Model):
    """Модель загрузочного файла."""
    file = models.FileField(upload_to='uploaded_files/')
    upload_date = models.DateTimeField(auto_now_add=True)
