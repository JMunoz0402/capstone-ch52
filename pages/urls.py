from django.urls import path
from .views import home, about, services, gallery, contact

urlpatterns = [
    path("", home, name="root"),
    path("home", home, name="home"),
    path("about", about, name="about"),
    path("services", services, name="services"),
    path("gallery", gallery, name="gallery"),
    path("contact", contact, name="contact")
]