from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm
from .models import Gallery



# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send an email (configure EMAIL settings in settings.py)
            send_mail(
                f'Contact Request from {name}',
                message,
                email,  # From email
                ['jesusmunoz0402@email.com'],  
                fail_silently=False,
            )
            return redirect('success_page')  
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')

# def gallery(request):
#     return render(request, 'pages/gallery.html')



def gallery(request):
    images = Gallery.objects.all()
    return render(request, 'pages/gallery.html', {'images': images})
