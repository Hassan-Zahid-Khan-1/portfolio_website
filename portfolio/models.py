from django.db import models

class form(models.Model):
    username=models.CharField(max_length=150)
    email=models.EmailField()
    message=models.TextField(max_length=1500)
    def __str__(self) -> str:
        return self.username

# Create your models here.
class projects(models.Model):
    image=models.ImageField( upload_to="photos/", height_field=None, width_field=None, max_length=None)
    title=models.CharField( max_length=80)
    description=models.CharField( max_length=8000)
    link=models.URLField( max_length=200)