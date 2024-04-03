from django.shortcuts import render, redirect

from .forms import UploadedFileForm
from .utils import processing_file


def index(request):
    """Вьюшка основной страницы,

    темплейту передаем форму.
    """
    form = UploadedFileForm()
    return render(request, 'index.html', {'form': form})


def upload_file(request):
    """Вьюшка обработки файла."""
    form = UploadedFileForm(
        request.POST,
        files=request.FILES
    )
    if form.is_valid():
        form.save()
        result_of_proc = processing_file(form.instance.file)

        return render(request, 'uploaded_file.html', {'file': result_of_proc})

    return render(request, 'index.html', {'form': form})
