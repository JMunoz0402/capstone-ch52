from django.db import models

# Create your models here.
class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery_images/')
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.description or 'Image'