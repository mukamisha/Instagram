from django.db import models

# Create your models here.

class Image(models.Model):
    image= models.ImageField(upload_to = 'image/')
    img_name = models.CharField(max_length =30)
    img_caption = models.TextField()
    # profile = models.ForeignKey(Profile)
    # likes = models.IntField(max_length =20)
    # comments= models.TextField()

    def __str__(self):
        return self.img_name
