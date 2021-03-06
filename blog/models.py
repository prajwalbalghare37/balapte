from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.utils.timezone import now

# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(default="बाळासाहेब आपटे",max_length=1000)
    author = models.CharField(default="",max_length=37)
    slug = models.CharField(default="",max_length=137)
    image = models.ImageField(upload_to="allImages")
    content = models.TextField(default="बाळासाहेब आपटे")
    timeStamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title

class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timeStamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:-10] + "by " + self.user.username
    