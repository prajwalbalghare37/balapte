from django.db import models

# Create your models here.

class links(models.Model):
    sno = models.AutoField(primary_key=True)
    websiteName = models.CharField(default="",max_length=10000)
    websiteLink = models.CharField(default="",max_length=10000)

    def __str__(self):
        return self.websiteName