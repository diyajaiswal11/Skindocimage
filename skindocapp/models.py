from django.db import models

# Create your models here.

class ImageUpload(models.Model):
    image=models.FileField(upload_to='images/')