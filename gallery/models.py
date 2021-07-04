from django.db import models

# Create your models here.
class Image(models.Model):
    sno = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100,default='Bal Apate')
    image = models.ImageField(upload_to="allImages")
    imageName = models.CharField(max_length=100,default='Bal Apate')
    desc = models.CharField(default="Bal Apate",max_length=1000)
    timeStamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.imageName
    