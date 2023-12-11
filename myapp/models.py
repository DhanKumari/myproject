from django.db import models

# Create your models here.
class Profile(models.Model):
    def nameFile(instance, filename):
        return '/'.join(['docs',str(instance.name),filename])
    name=models.CharField(max_length=200)
    #picture= models.ImageField(upload_to="my_picture",blank=True)
    picture= models.ImageField(upload_to=nameFile,blank=True)
    file = models.FileField(upload_to="my_pdf",blank=True)