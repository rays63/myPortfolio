from django.shortcuts import render
from .models import *
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from .models import CV

# Create your views here.
def home(requests):
    files = CV.objects.all()
    print(files)
    context = {
        'files' : files
    }
    return render(requests, 'home/index.html',context)

def download_cv(request, cv_id):
    cv = get_object_or_404(CV, pk=cv_id)
    file_path = cv.file.path
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = f'attachment; filename="{cv.title}"'
    return response
