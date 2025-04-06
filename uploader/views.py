from django.shortcuts import render, redirect
from .forms import DocumentUploadForm

def upload_files(request):
    if request.method == 'POST':
        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'uploader/success.html')
    else:
        form = DocumentUploadForm()
    return render(request, 'uploader/upload.html', {'form': form})
