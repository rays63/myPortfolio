from django.shortcuts import render
from .models import *
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from .models import Cheatsheet

# Create your views here.
def home(requests):
    return render(requests, 'home/index.html')

def download_cheatsheet(request, cheatsheet_id):
    cheatsheet = get_object_or_404(Cheatsheet, pk=cheatsheet_id)
    file_path = cheatsheet.file.path
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = f'attachment; filename="{cheatsheet.title}"'
    return response
 
def cheatsheet(request):
    files = Cheatsheet.objects.all()
    print(files)
    context = {
        'files' : files
    }
    return render(request, 'download.html', context)