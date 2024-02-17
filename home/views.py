from django.shortcuts import render , redirect
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from .models import CV
from .forms import ContactForm
from .models import ContactMessage

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

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process form data here, like sending emails
            ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message']
            )
            return render(request, 'home/thankyou.html')
    else:
        form = ContactForm()
    return render(request, 'home/contact.html', {'form': form})
