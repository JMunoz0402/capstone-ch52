from django.shortcuts import render
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

# def gallery(request):
#     return render(request, 'pages/gallery.html')



def gallery(request):
    images = Gallery.objects.all()
    return render(request, 'pages/gallery.html', {'images': images})
