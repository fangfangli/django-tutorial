from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm

# Imaginary function to handle an uploaded file.
def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'fileupload/upload.html', {'form': form})
    

## easier use
# #views.py
# Import os
# 
# from django.conf import settings
# 
# 
# def file_upload(request):
#     save_path = os.path.join(settings.MEDIA_ROOT, 'uploads', request.FILES['file'])
#     path = default_storage.save(save_path, request.FILES['file'])
#     return default_storage.path(path)