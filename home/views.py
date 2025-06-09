from django.shortcuts import render , redirect
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from .models import CV
from .forms import ContactForm
from .models import ContactMessage
from .github_api import get_github_repos

# Create your views here.
def home(request):
    message_sent = False  # Initialize the flag
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message']
            )
            message_sent = True  # Set the flag to True after message is sent
            form = ContactForm()  # Reset the form after successful submission
    else:
        form = ContactForm()
    
    files = CV.objects.all()
    context = {
        'files': files,
        'form': form,
        'message_sent': message_sent  # Pass the flag to the template context
    }

    github_username = 'rays63'
    github_token = None  # Optional: Add token to avoid rate limits
    repos = get_github_repos(github_username, github_token)
    print("DEBUG - fetched repos:", len(repos))  # Optional debug

    context = {
        'files': files,
        'form': form,
        'message_sent': message_sent,
        'repos': repos,  # ⬅️ include in context
    }

    return render(request, 'home/index.html', context)


def download_cv(request, cv_id):
    cv = get_object_or_404(CV, pk=cv_id)
    file_path = cv.file.path
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = f'attachment; filename="{cv.title}"'
    return response


