from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

class Profile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
   profile_picture = models.ImageField(upload_to='images/')
   bio = models.TextField(max_length=700)
   name = models.CharField(max_length=200)
   def __str__(self):
       return self.name
   @classmethod
   def search_profile(cls, username):
       return cls.objects.filter(name__icontains=username)
   def save_profile(self):
       self.user
   def delete_profile(self):
       self.delete()

class Image(models.Model):
    image= models.ImageField(upload_to = 'image/')
    img_name = models.CharField(max_length =30)
    img_caption = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    comments= models.TextField()

    def __str__(self):
        return self.img_name

    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()

    @classmethod
    def get_all_images(cls):
       images=cls.objects.all().prefetch_related('comment_set')
       return images

    def total_likes(self):
       self.likes.count()

class Comment(models.Model):
   posted_by=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
   comment_pic=models.ForeignKey(Image,on_delete=models.CASCADE,null=True)
   comment=models.CharField(max_length=20,null=True)
   def __str__(self):
       return self.posted_by





