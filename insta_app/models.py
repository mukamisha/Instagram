from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

class Image(models.Model):
    image= models.ImageField(upload_to = 'image/')
    img_name = models.CharField(max_length =30)
    img_caption = models.TextField()
    post = HTMLField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    # profile = models.ForeignKey(Profile)
    # likes = models.IntField(max_length =20)
    # comments= models.TextField()

    def __str__(self):
        return self.img_name
