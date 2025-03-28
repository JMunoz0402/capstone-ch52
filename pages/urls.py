from django.urls import path
from .views import home, about, services, gallery, contact
from .views import contact_view
from .views import success_view
urlpatterns = [
    path("", home, name="root"),
    path("home", home, name="home"),
    path("about", about, name="about"),
    path("services", services, name="services"),
    path("gallery", gallery, name="gallery"),
    path("contact", contact, name="contact"),
    path('contact/', contact_view, name='contact'),
    path('success/', success_view, name='success_page'),
]